from typing import List

from splunkapi3.model.options import Options
from splunkapi3.rest import Rest

class Command(Rest):

    def get_data_commands(self, options: Options)->List[dict]:
        """
        Provides access to Python search commands used in Splunk.
        :param options: Options
        :return: Splunk search commands.
        """
        relative_url = 'data/commands/'
        content = self.connection.get_record(relative_url=relative_url, options=options)
        return content.feed.entry

    def get_data_command(self, name: str)->dict:
        """

        :param name:
        :return:
        """
        relative_url = 'data/commands/{name}'.format(name=name)
        content = self.connection.get_record(relative_url=relative_url)
        return content.feed.entry
