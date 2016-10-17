from splunkapi3.connection import Connection
from splunkapi3.options import Options
from splunkapi3.data import load
from splunkapi3.rest import Rest


class Command(Rest):

    def get_data_commands(self, options: Options):
        relative_url = 'data/commans'
        self.connection.get(relative_url=relative_url, options=options)
