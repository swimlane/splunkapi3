from typing import List

from splunkapi3.model import ViewEdit
from splunkapi3.model.options import Options
from splunkapi3.rest import Rest

class View(Rest):

    def get_views(self, options: Options=None)->List[dict]:
        """
        Lists all scheduled view objects.
        :return: View objects.
        """
        relative_url = 'scheduled/views/'
        content = self.connection.get_record(relative_url=relative_url, options=options)
        return content.feed.entry or []

    def delete_view(self, name: str):
        """
        Delete a scheduled view
        :return: None
        """
        relative_url = 'scheduled/views/{name}'.format(name=name)
        self.connection.delete(relative_url=relative_url)

    def get_view(self, name: str)->dict:
        """
        List one scheduled view object.
        :return: None
        """
        relative_url = 'scheduled/views/{name}'.format(name=name)
        content = self.connection.get_record(relative_url=relative_url)
        return content.feed.entry

    def edit(self, name: str, view_edit_model: ViewEdit=None)->dict:
        """
        Edit a scheduled view, e.g. change schedule, enable disable schedule etc.
        :return: None
        """
        relative_url = 'scheduled/views/{name}'.format(name=name)
        content = self.connection.post(relative_url=relative_url, data=view_edit_model.dict)
        return content.feed.entry

    def dispatch(self, name: str, trigger_actions: bool=True):
        """
        Dispatch the scheduled search (powering the scheduled view) just like the
        scheduler would.
        :param name: View name.
        :param trigger_actions:
        :return: Indicates whether to trigger alert actions
        """
        relative_url = 'scheduled/views/{name}/dispatch/'.format(name=name)
        data = {'dispatch.now': True, 'trigger_actions': trigger_actions}
        self.connection.post(relative_url=relative_url, data=data)

    def history(self, name: str) -> List[dict]:
        """
        Get a list of search jobs used to deliver this scheduled view.
        :param name: View name.
        :return: Collection of saved search jobs.
        """
        relative_url = 'scheduled/views/{name}/history/'.format(name=name)
        content = self.connection.get_record(relative_url=relative_url)
        return content.feed.entry or []

    def reschedule(self, name: str, schedule_time: str=None):
        """
        Tells the scheduler when to next schedule PDF delivery of the view. If
        schedule_time is not specified, then it is assumed that the delivery should occur
        as soon as possible.
        :param schedule_time: The time to next run the search. 2012-08-15T14:11:01Z
        :param name: View name.
        :return: None
        """
        relative_url = 'scheduled/views/{name}/reschedule/'.format(name=name)
        data = {'schedule_time': schedule_time} if schedule_time else {}
        self.connection.post(relative_url=relative_url, data=data)

    def scheduled_times(self, name: str, earliest_time: str, latest_time: str):
        """
        Returns the scheduled times for a scheduled view. Specify a time range for the
        data returned using earliest_time and latest_time parameters.
        :param latest_time: Absolute or relative latest time. -2h
        :param earliest_time: Absolute or relative earliest time. -6h
        :param name: View name.
        :return: None
        """
        relative_url = 'scheduled/views/{name}/scheduled_times/'.format(name=name)
        params = {'earliest_time': earliest_time, 'latest_time': latest_time}
        content = self.connection.get_record(relative_url=relative_url, params=params)
        return content.feed.entry
