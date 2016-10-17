from splunkapi3.access_control import AccessControl
from splunkapi3.search import Search
from splunkapi3.connection import Connection


class Client(object):

    _access_control = None
    _search = None

    def __init__(self, url: str, verify: bool=True):
        """
        Constructor
        :param url: The Splunk api url. 'https://localhost:
        :param verify: To verify SSL certificate or not. More for a development, qa.
        """
        self._connection = Connection(url=url, verify=verify)

    def connect(self, user: str, password: str):
        """
        Perform connection and authentication, persist session key.
        :param user: User name.
        :param password: Password.
        :return: None
        """
        self._connection.session_key = self.access_control.login(user, password)

    @property
    def access_control(self):
        if not self._access_control:
            self._access_control = AccessControl(self._connection)
        return self._access_control

    @property
    def search(self):
        if not self._search:
            self._search = Search(self._connection)
        return self._search
