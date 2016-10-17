from splunkapi3.connection import Connection
from splunkapi3.options import Options
from splunkapi3.data import load


class Rest(object):

    def __init__(self, connection: Connection):
        """
        Constructor
        :param connection: Connection
        """
        self.connection = connection