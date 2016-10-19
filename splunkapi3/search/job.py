from typing import List
from urllib.parse import urlencode, quote
from splunkapi3.model import SearchCreate, ControlAction, Options, OutputMode
from splunkapi3.model import SearchResultOptions
from splunkapi3.rest import Rest
from json import loads, load


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

    def results(self, search_id: str)->dict:
        """
        This is the table that exists after all processing from the search pipeline has completed.
        This is the primary method for a client to fetch a set of TRANSFORMED events.
        If the dispatched search does not include a transforming command, the effect is the
        same as get_events, however with fewer options.

        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: Results of a search.
        """
        relative_url = 'search/jobs/{search_id}/results/'.format(search_id=quote(search_id))
        content = self.connection.get_record(relative_url=relative_url)
        return content

    def results_formatted(self, search_id: str, output_mode: OutputMode=OutputMode.xml,
                          options: SearchResultOptions=None)->str:
        """
        This is the table that exists after all processing from the search pipeline has completed.
        This is the primary method for a client to fetch a set of TRANSFORMED events.
        If the dispatched search does not include a transforming command, the effect is the
        same as get_events, however with fewer options.

        :param options: Other search result options.
        :param output_mode: Specifies the format for the returned output.
        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: Results of a search.
        """
        relative_url = 'search/jobs/{search_id}/results/'.format(search_id=quote(search_id))
        params = [('output_mode', output_mode.name)]
        if options:
            params.extend(options.dict)
        return self.connection.get(relative_url=relative_url, params=params)

    def results_immediate(self, search_id: str)->dict:
        """
        Returns the intermediate preview results of the search specified by {search_id}.
        When the job is complete, this gives the same response as `results` method.
        Preview is enabled for real-time searches and for searches where status_buckets > 0.

        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: Results of a search.
        """
        relative_url = 'search/jobs/{search_id}/results_preview/'\
            .format(search_id=quote(search_id))
        content = self.connection.get_record(relative_url=relative_url)
        return content

    def results_immediate_formatted(self, search_id: str,
                                    output_mode: OutputMode=OutputMode.xml,
                                    options: SearchResultOptions=None)->str:
        """
        Returns the intermediate preview results of the search specified by {search_id}.
        When the job is complete, this gives the same response as `results` method.
        Preview is enabled for real-time searches and for searches where status_buckets > 0.

        :param options: Other search result options.
        :param output_mode: Specifies the format for the returned output.
        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: Results of a search.
        """
        relative_url = 'search/jobs/{search_id}/results_preview/'.format(search_id=quote(search_id))
        params = [('output_mode', output_mode.name)]
        if options:
            params.extend(options.dict)
        return self.connection.get(relative_url=relative_url, params=params)

    def log(self, search_id: str)->str:
        """
        Get the {search_id} search log.

        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: Log as text.
        """
        relative_url = 'search/jobs/{search_id}/search.log/'.format(search_id=quote(search_id))
        return self.connection.get(relative_url=relative_url)

    def summary(self, search_id: str)->dict:
        """
        Get the getFieldsAndStats output of the events to-date, for the search_id search.

        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: Summary.
        """
        relative_url = 'search/jobs/{search_id}/summary/'.format(search_id=quote(search_id))
        return self.connection.get_record(relative_url=relative_url)

    def time_line(self, search_id: str, time_format: str=None)->dict:
        """
        Get the getFieldsAndStats output of the events to-date, for the search_id search.

        :param time_format: Expression to convert a formatted time string from
        {start,end}_time into UTC seconds. Default %m/%d/%Y:%H:%M:%S
        :param search_id: Search Id. <sid> returned from get_jobs.
        :return: Time line.
        """
        relative_url = 'search/jobs/{search_id}/summary/'.format(search_id=quote(search_id))
        params = {'time_format': time_format} if time_format else {}
        return self.connection.get_record(relative_url=relative_url, params=params)

    def export(self,
               query: str,
               options: SearchCreate=None,
               output_mode: OutputMode=OutputMode.xml)-> bytes:
        """
        Stream search results as they become available.
        Performs a search identical to POST search/jobs, except the search does not create a
        search ID (<sid>) and the search streams results as they become available.
        Streaming of results is based on the search string.

        For non-streaming searches, previews of the final results are available if preview
        is enabled. If preview is not enabled, it is better to use
        search/jobs with exec_mode=oneshot.

        If it is too big, you might instead run with the search/jobs (not search/jobs/export)
        endpoint (it takes POST with the same parameters), maybe using the
        exec_mode=blocking. You'll then get back a search id, and then you can page
        through the results and request them from the server under your control, which is a
        better approach for extremely large result sets that need to be chunked.
        :param query: The search query to run
        :param options: Optional parameters.
        :param output_mode: Specifies the format for the returned output.
        :return: Results of search.
        """
        relative_url = 'search/jobs/export/'
        params = options.dict if options else {}
        params.update({'search': query, 'output_mode': output_mode.name})
        return self.connection.get(relative_url=relative_url, params=params)

    def export_oneshot(self, query: str, options: SearchCreate=SearchCreate())->List[dict]:
        """
        Stream search results as they become available.
        Performs a search identical to POST search/jobs, except the search does not create a
        search ID (<sid>) and the search streams results as they become available.
        Streaming of results is based on the search string.

        For non-streaming searches, previews of the final results are available if preview
        is enabled. If preview is not enabled, it is better to use
        search/jobs with exec_mode=oneshot.

        If it is too big, you might instead run with the search/jobs (not search/jobs/export)
        endpoint (it takes POST with the same parameters), maybe using the
        exec_mode=blocking. You'll then get back a search id, and then you can page
        through the results and request them from the server under your control, which is a
        better approach for extremely large result sets that need to be chunked.
        :return: Results of search.
        """
        # options = options or SearchCreate()
        options.exec_mode = 'oneshot'
        content = self.export(query, options=options, output_mode=OutputMode.json)
        content = str(content, 'utf-8')
        result = []
        for row in content.split('\n'):
            record = loads(row)
            if record.get('lastrow'):
                break
            result.append(record['result'])
        return result


