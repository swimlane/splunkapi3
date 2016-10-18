from splunkapi3.connection import Connection
from splunkapi3.data import load
from splunkapi3.model.options import Options

class Alert(object):

    def __init__(self, connection: Connection):
        """
        Constructor
        :param connection: Connection
        """
        self.connection = connection

    def get_fired_alerts(self, options: Options=None)->int:
        """
        Returns a summary view of the list of all alerts that have been fired on the server.
        :return:
        """
        relative_url = 'alerts/fired_alerts/'
        content = self.connection.get(relative_url=relative_url, options=options)
        record = load(content)
        return int(record.feed.entry.content.triggered_alert_count)

    def delete_fired_alert(self, name: str):
        """
        Deletes the record of this triggered alert.
        :param name: Name of the alert.
        :return:
        """
        relative_url = 'alerts/fired_alerts/{name}'.format(name=name)
        self.connection.delete(relative_url=relative_url)

    def get_fired_alert(self, name: str):
        """
        Returns a list of all unexpired triggered or fired instances of this alert
        :param name:
        :return:actions
        UNDONE Any additional alert actions triggered by this alert.
        alert_type Indicates if the alert was historical or real-time.
        digest_mode UNDONE_attr_desc
        expiration_time_rendered UNDONE_attr_desc
        savedsearch_name Name of the saved search that triggered the alert.
        severity
        Indicates the severity level of an alert.
        Severity level ranges from Info, Low, Medium, High,
        and Critical. Default is Medium.
        Severity levels are informational in purpose and
        have no additional functionality.
        sid The search ID of the search that triggered the alert.
        trigger_time The time the alert was triggered.
        trigger_time_rendered UNDONE_attr_desc
        triggered_alerts UNDONE_attr_desc
        Example
        Retrieve all instances of the "MyAlert" alert being fired
        """
        relative_url = 'alerts/fired_alerts/{name}'.format(name=name)
        content = self.connection.get(relative_url=relative_url)
        record = load(content)
        return record.feed.entry.content
