from typing import List

from splunkapi3.model.model import Model


class SearchResultOptions(Model):

    name_map = {'fields': 'f'}

    def __init__(self, add_summary_to_metadata: bool=None,
                 count: int=None, fields: List[str]=None, offset: int=None, search: str=None):
        """
        c-tor

        :param add_summary_to_metadata: Set the value to "true" to include field
        summary statistics in the response.

        :param count: The maximum number of results to return. If value is set to 0,
        then all available results are returned.

        :param fields: A field to return for the event set.
        You can pass multiple POST f arguments if multiple field are required.

        :param offset: The first result (inclusive) from which to begin returning data.
        This value is 0-indexed. Default value is 0.
        In 4.1+, negative offsets are allowed and are added to count to compute the
        absolute offset (for example, offset=-1 is the last available offset).

        :param search: he post processing search to apply to results. Can be any valid
        search language string.
        """
        self.add_summary_to_metadata = add_summary_to_metadata
        self.count = count
        self.fields = fields
        self.offset = offset
        self.search = search

    @property
    def dict(self) -> dict:
        data = [(self.map(k), v) for k, v in self.__dict__.items() if v is not None]
        if self.fields:
            data.extend(('f', f) for f in self.fields)
        return data
