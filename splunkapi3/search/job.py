from typing import List
from urllib.parse import urlencode, quote
from splunkapi3.model import SearchCreate, ControlAction, Options, OutputMode
from splunkapi3.rest import Rest


class Job(Rest):

    def get_jobs(self, options: Options=None)->List[dict]:
        """
        Provides listings for search jobs.
        :param options: Paging and filtering options.
        :return: Job listing.
        """
        relative_url = 'search/jobs/'
        content = self.connection.get_record(relative_url=relative_url, options=options)
        return content.feed.entry or []

    def start_job(self, query: str, search_create_model: SearchCreate=None):
        """
        Create and start the job.
        :param query: Search string for search job.
        :param search_create_model: Other parameters.
        :return: None
        """
        relative_url = 'search/jobs/'
        data = search_create_model.dict if search_create_model else {}
        data['search'] = urlencode(query)
        self.connection.post(relative_url=relative_url, data=data)

    def get_job(self, search_id: str)->dict:
        """
        Get information about the {search_id} search job.
        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: Job details.
        """
        relative_url = 'search/jobs/{search_id}'.format(search_id=quote(search_id))
        content = self.connection.get_record(relative_url=relative_url)
        return content.entry

    def delete_job(self, search_id: str):
        """
        Deletes the search job specified by {search_id}.
        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: None
        """
        relative_url = 'search/jobs/{search_id}'.format(search_id=quote(search_id))
        self.connection.delete(relative_url=relative_url)

    def update_job(self, search_id: str, custom: str):
        """
        Update the {search_id} search job.
        :param custom: Specify custom job properties for the specified search job.
        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: None
        """
        relative_url = 'search/jobs/{search_id}'.format(search_id=quote(search_id))
        data = {'custom.*': urlencode(custom)}
        self.connection.post(relative_url=relative_url, data=data)

    def control(self, search_id: str, action: ControlAction):
        """
        Update the {search_id} search job.

        :param action: The control action to execute.
        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: None
        """
        relative_url = 'search/jobs/{search_id}/control/'.format(search_id=quote(search_id))
        data = {'action': action.name}
        self.connection.post(relative_url=relative_url, data=data)

    def events(self, search_id: str):
        """
        Access {search_id} search events. These events are the data from the search
        pipeline before the first "transforming" search command.

        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: None
        """
        relative_url = 'search/jobs/{search_id}/events/'.format(search_id=quote(search_id))
        content = self.connection.get_record(relative_url=relative_url)
        return content

    def results(self, search_id: str):
        """
        Access {search_id} search events. These events are the data from the search
        pipeline before the first "transforming" search command.

        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: None
        """
        relative_url = 'search/jobs/{search_id}/results/'.format(search_id=quote(search_id))
        content = self.connection.get_record(relative_url=relative_url)
        return content

    def results_formatted(self, search_id: str, output_mode: OutputMode=OutputMode.xml):
        """
        Access {search_id} search events. These events are the data from the search
        pipeline before the first "transforming" search command.

        :param output_mode: Specifies the format for the returned output.
        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: None
        """
        relative_url = 'search/jobs/{search_id}/results/'.format(search_id=quote(search_id))
        params = {'output_mode': output_mode.name}
        return self.connection.get(relative_url=relative_url, params=params)
