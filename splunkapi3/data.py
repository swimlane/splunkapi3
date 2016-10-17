# Copyright 2011-2015 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# File has been modified by Swimlane Inc to be python 3.5 compatible.
# and pep8 compliant
# Copyright 2016

"""The **splunklib.data** module reads the responses from splunkd in Atom Feed
format, which is the format used by most of the REST API.
"""

from xml.etree.ElementTree import XML

__all__ = ["load"]

# L_NAME refers to element names without namespaces; X_NAME is the same
# name, but with an XML namespace.
L_NAME_DICT = "dict"
L_NAME_ITEM = "item"
L_NAME_KEY = "key"
L_NAME_LIST = "list"

X_NAME_REST = "{http://dev.splunk.com/ns/rest}%s"
X_NAME_DICT = X_NAME_REST % L_NAME_DICT
X_NAME_ITEM = X_NAME_REST % L_NAME_ITEM
X_NAME_KEY = X_NAME_REST % L_NAME_KEY
X_NAME_LIST = X_NAME_REST % L_NAME_LIST


def isdict(name):
    return name == X_NAME_DICT or name == L_NAME_DICT


def isitem(name):
    return name == X_NAME_ITEM or name == L_NAME_ITEM


def iskey(name):
    return name == X_NAME_KEY or name == L_NAME_KEY


def islist(name):
    return name == X_NAME_LIST or name == L_NAME_LIST


def hasattrs(element):
    return len(element.attrib) > 0


def localname(x_name):
    r_curly = x_name.find('}')
    return x_name if r_curly == -1 else x_name[r_curly + 1:]


def load(text: str, match: str=None):
    """This function reads a string that contains the XML of an Atom Feed, then
    returns the
    data in a native Python structure (a ``dict`` or ``list``). If you also
    provide a tag name or path to match, only the matching sub-elements are
    loaded.
    :param text: The XML text to load.
    :type text: ``string``
    :param match: A tag name or path to match (optional).
    :type match: ``string``
    """
    if text is None:
        return None
    text = text.strip()
    if len(text) == 0:
        return None
    name_table = {
        'namespaces': [],
        'names': {}
    }
    root = XML(text)
    items = [root] if match is None else root.findall(match)
    count = len(items)
    if count == 0:
        return None
    elif count == 1:
        return load_root(items[0], name_table)
    else:
        return [load_root(item, name_table) for item in items]


def load_attributes(element):
    if not hasattrs(element): 
        return None
    attributes = record()
    for key, value in element.attrib.items():
        attributes[key] = value
    return attributes


def load_dict(element, name_table=None):
    value = record()
    children = list(element)
    for child in children:
        assert iskey(child.tag)
        name = child.attrib["name"]
        value[name] = load_value(child, name_table)
    return value


def load_elem(element, name_table=None):
    name = localname(element.tag)
    attributes = load_attributes(element)
    value = load_value(element, name_table)
    if attributes is None:
        return name, value
    if value is None:
        return name, attributes
    # If value is simple, merge into attributes dict using special key
    if isinstance(value, str):
        attributes["$text"] = value
        return name, attributes
    # Both attributes & value are complex, so merge the two dicts, resolving collisions.
    collision_keys = []
    for key, val in attributes.items():
        if key in value and key in collision_keys:
            value[key].append(val)
        elif key in value and key not in collision_keys:
            value[key] = [value[key], val]
            collision_keys.append(key)
        else:
            value[key] = val
    return name, value


def load_list(element, name_table=None):
    assert islist(element.tag)
    value = []
    children = list(element)
    for child in children:
        assert isitem(child.tag)
        value.append(load_value(child, name_table))
    return value


def load_root(element, name_table=None):
    tag = element.tag
    if isdict(tag): 
        return load_dict(element, name_table)
    if islist(tag): 
        return load_list(element, name_table)
    k, v = load_elem(element, name_table)
    return Record.from_kv(k, v)


def load_value(element, name_table=None):
    children = list(element)
    count = len(children)

    # No children, assume a simple text value
    if count == 0:
        text = element.text
        if text is None:
            return None
        text = text.strip()
        if len(text) == 0:
            return None
        return text

    # Look for the special case of a single well-known structure
    if count == 1:
        child = children[0]
        tag = child.tag
        if isdict(tag): 
            return load_dict(child, name_table)
        if islist(tag): 
            return load_list(child, name_table)

    value = record()
    for child in children:
        name, item = load_elem(child, name_table)
        # If we have seen this name before, promote the value to a list
        if name in value:
            current = value[name]
            if not isinstance(current, list):
                value[name] = [current]
            value[name].append(item)
        else:
            value[name] = item

    return value


class Record(dict):
    """This generic utility class enables dot access to members of a Python
    dictionary.
    Any key that is also a valid Python identifier can be retrieved as a field.
    So, for an instance of ``Record`` called ``r``, ``r.key`` is equivalent to
    ``r['key']``. A key such as ``invalid-key`` or ``invalid.key`` cannot be
    retrieved as a field, because ``-`` and ``.`` are not allowed in
    identifiers.
    Keys of the form ``a.b.c`` are very natural to write in Python as fields. If
    a group of keys shares a prefix ending in ``.``, you can retrieve keys as a
    nested dictionary by calling only the prefix. For example, if ``r`` contains
    keys ``'foo'``, ``'bar.baz'``, and ``'bar.qux'``, ``r.bar`` returns a record
    with the keys ``baz`` and ``qux``. If a key contains multiple ``.``, each
    one is placed into a nested dictionary, so you can write ``r.bar.qux`` or
    ``r['bar.qux']`` interchangeably.
    """
    sep = '.'

    def __call__(self, *args):
        if len(args) == 0: 
            return self
        return Record((key, self[key]) for key in args)

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __delattr__(self, name):
        del self[name]

    def __setattr__(self, name, value):
        self[name] = value

    @staticmethod
    def from_kv(k, v):
        result = record()
        result[k] = v
        return result

    def __getitem__(self, key):
        if key in self:
            return self.get(key)
        key += self.sep
        result = record()
        for k, v in self.items():
            if not k.startswith(key):
                continue
            suffix = k[len(key):]
            if '.' in suffix:
                ks = suffix.split(self.sep)
                z = result
                for x in ks[:-1]:
                    if x not in z:
                        z[x] = record()
                    z = z[x]
                z[ks[-1]] = v
            else:
                result[suffix] = v
        if len(result) == 0:
            raise KeyError("No key or prefix: %s" % key)
        return result


def record(value: dict=None)->Record:
    """
    This function returns a :class:`Record` instance constructed with an
    initial value that you provide.
    :param value: An initial record value.
    :return: Record object.
    """
    if value is None: 
        value = {}
    return Record(value)
