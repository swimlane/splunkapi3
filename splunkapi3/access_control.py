# noinspection PyPackageRequirements
from xmltodict import parse
from splunkapi3.connection import Connection


class AccessControl(object):

    def __init__(self, connection: Connection):
        self.connection = connection

    def login(self, user: str, password: str)->str:
        """
        Login. Authenticate user.
        :param user: Username.
        :param password: Password
        :return: Session key.
        :exception: ConnectError
        """
        relative_url = 'auth/login/'
        content = self.connection.post(relative_url,
                                       data={'username': user, 'password': password})
        parsed = parse(content)
        return parsed['response']['sessionKey']

    def current_context(self):
        """
        Lists one item named "context" which contains the name of the current user.
        :return: Context ordered dictionary
        """
        relative_url = 'authentication/current-context/'
        content = self.connection.get(relative_url)
        parsed = parse(content)
        return parsed['feed']

    # noinspection SpellCheckingInspection,PyMethodMayBeStatic
    def get_httpauth_tokens(self):
        """
        List all currently active session tokens.
        :return:
        """
        pass

    # noinspection SpellCheckingInspection,PyMethodMayBeStatic
    def delete_httpauth_token(self, name: str):
        """
        End the session associated with this token.
        :return: None
        """
        pass

    # noinspection PyMethodMayBeStatic
    def get_users(self):
        """
        Returns a list of all the users registered on the server.
        :return:
        """
        pass

    # noinspection SpellCheckingInspection,PyMethodMayBeStatic
    def create_user(self):
        """
        Creates a new user.
        When creating a user you must specify at least one role. You can specify one or
        more roles with the roles parameter, or you can use the createrole parameter
        to create a role for the user.
        :return:
        """

    # noinspection SpellCheckingInspection,PyMethodMayBeStatic
    def delete_user(self, name: str):
        """
        Removes the user from the system.
        :return: None
        """
        pass

    # noinspection SpellCheckingInspection,PyMethodMayBeStatic
    def get_user(self, name: str):
        """
        Returns information about the user.
        :return: None
        """
        pass

    # noinspection SpellCheckingInspection,PyMethodMayBeStatic
    def update_user(self, name: str):
        """
        Update information about the user specified by name.
        :return: None
        """
        pass
