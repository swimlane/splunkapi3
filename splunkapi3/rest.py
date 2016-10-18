from splunkapi3.connection import Connection

class Rest(object):

    def __init__(self, connection: Connection):
        """
        Constructor
        :param connection: Connection
        """
        self.connection = connection