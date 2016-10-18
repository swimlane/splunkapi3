from typing import List
from urllib.parse import urlencode

from splunkapi3.model.options import Options
from splunkapi3.rest import Rest

class Saved(Rest):

    def get_searches(self, options: Options=None)->List[dict]:
        """
        Returns information on all saved searches.
        :return: Collection of Searches
        """
        relative_url = 'saved/searches'
        content = self.connection.get_record(relative_url=relative_url, options=options)
        return content.feed.entry

    def create_search(self, name: str, search: str):
        """
        Creates new search.
        :return: None
        """
        relative_url = 'saved/searches'
        self.connection.post(relative_url=relative_url,
                             data={'name': name, 'search': urlencode(search)})

    def delete_search(self, name: str):
        """
        Delete the search.
        :return: None
        """
        relative_url = 'saved/searches/{name}'.format(name=name)
        self.connection.delete(relative_url=relative_url)

    def get_search(self, name: str)->dict:
        """
         Returns information on a saved search.
        :return: Saved search info.
        """
        relative_url = 'saved/searches/{name}'.format(name=name)
        content = self.connection.get_record(relative_url=relative_url)
        return content.feed.entry

    def update_search(self, name: str, data: dict):
        """
         Update saved search
        :return: None
        """
        relative_url = 'saved/searches/{name}'.format(name=name)
        self.connection.post(relative_url=relative_url, data=data)

    def acknowledge(self, name: str, key: str=None):
        """
        Acknowledge the suppression of the alerts from this saved search and resume
        alerting.
        :param name: Search name.
        :param key: The suppression key used in field-based suppression.
        :return: None
        """
        relative_url = 'saved/searches/{name}/acknowledge/'.format(name=name)
        data = {'key': key} if key else {}
        self.connection.post(relative_url=relative_url, data=data)

    def dispatch(self, name: str, trigger_actions: bool=True):
        """
        Dispatch the saved search just like the scheduler would.
        :param trigger_actions: Indicates whether to trigger alert actions.
        :param name: Search name.
        :return: None
        """
        relative_url = 'saved/searches/{name}/dispatch/'.format(name=name)
        data = {'dispatch.now': True, 'trigger_actions': trigger_actions}
        self.connection.post(relative_url=relative_url, data=data)

    def history(self, name: str)->List[dict]:
        """
        Get a list of available search jobs created from this saved search.
        :param name: Search name.
        :return: Collection of saved search jobs.
        """
        relative_url = 'saved/searches/{name}/history/'.format(name=name)
        content = self.connection.get_record(relative_url=relative_url)
        return content.feed.entry or []

    def reschedule(self, name: str, schedule_time: str=None):
        """
        Provides access to endpoints that tell the scheduler when to next run the search.
        If no schedule_time argument is specified, it is assumed that the search should
        be run as soon as possible.
        :param schedule_time: The time to next run the search. 2012-08-15T14:11:01Z
        :param name: Search name.
        :return: None
        """
        relative_url = 'saved/searches/{name}/reschedule/'.format(name=name)
        data = {'schedule_time': schedule_time} if schedule_time else {}
        self.connection.post(relative_url=relative_url, data=data)

    def scheduled_times(self, name: str, earliest_time: str, latest_time: str):
        """
        Returns the scheduled times for a saved search. Specify a time range for the
        data returned using earliest_time and latest_time parameters.
        :param latest_time: Absolute or relative latest time. -2h
        :param earliest_time: Absolute or relative earliest time. -6h
        :param name: Search name.
        :return: None
        """
        relative_url = 'saved/searches/{name}/scheduled_times/'.format(name=name)
        params = {'earliest_time': earliest_time, 'latest_time': latest_time}
        content = self.connection.get_record(relative_url=relative_url, params=params)
        return content.feed.entry

    # noinspection PyMethodMayBeStatic
    def suppress(self, name: str):
        """
        Check the suppression state of alerts from this saved searc
        :param name:
        :return:
        """
        pass
