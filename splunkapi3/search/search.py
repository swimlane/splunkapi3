from splunkapi3.connection import Connection
from splunkapi3.search.alert import Alert


class Search(object):

    _alert = None

    def __init__(self, connection: Connection):
        self._connection = connection

    @property
    def alert(self):
        if not self._alert:
            self._alert = Alert(self._connection)
        return self._alert
