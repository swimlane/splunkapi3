from typing import Union, List

from splunkapi3.rest import Rest


class Util(Rest):

    def parser(self, query: str, parse_only=True)->dict:
        """
        Parses Splunk search language and returns semantic map.

        :param parse_only: If true, disables expansion of search due evaluation of
        subsearches, time term expansion, lookups, tags, eventtypes, sourcetype alias.

        :param query: The search string to parse.
        :return: Semantic map.
        """
        relative_url = 'search/parser/'
        params = {'q': query, 'parse_only': parse_only}
        return self.connection.get_record(relative_url=relative_url, params=params)

    def is_scheduler_enabled(self)->bool:
        """
        Get current search scheduler enablement status.
        :return: True if enabled, false otherwise.
        """
        relative_url = 'search/scheduler/'
        content = self.connection.get_record(relative_url=relative_url)
        return bool(content.feed.entry.content.saved_searches_disabled)

    def scheduler_status_change(self, disable: bool):
        """
        Enable or disable the search scheduler.

        :param disable: Indicates whether to disable the search scheduler. 0 enables the
        search scheduler. 1 disables the search scheduler.
        :return: True if enabled, false otherwise.
        """
        relative_url = 'search/scheduler/'
        data = {'disabled': disable}
        self.connection.post(relative_url=relative_url, data=data)

    def time_parser(self, time: List[str])->dict:
        """
        Get a lookup table of time arguments to absolute timestamps.
        :param time: The time argument to parse.
        Acceptable inputs are either a relative time identifier or an absolute time.
        Multiple time arguments can be passed by specifying multiple time parameters.
        :return:
        """
        relative_url = 'search/timeparser/'
        params = [('time', t) for t in time]
        content = self.connection.get_record(relative_url=relative_url, params=params)
        return content.response

    def type_ahead(self, prefix: str, count: int)->dict:
        """
        Get search string auto-complete suggestions.
        :param count: The number of items to return for this term.
        :param prefix: The term for which to return typeahead results.
        :return: csv encoded list
        """
        relative_url = 'search/typeahead/'
        params = {'prefix': prefix, 'count': count}
        self.connection.get(relative_url=relative_url, params=params)
        return self.connection.get(relative_url=relative_url, params=params)
