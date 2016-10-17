import os
import sys
import nose
from splunkapi3.client import Client
from os.path import join, dirname, normpath
from dotenv import load_dotenv
from os import environ
from splunkapi3.options import Options

dot_env_path = normpath(join(dirname(__file__), '../', '.env'))
load_dotenv(dot_env_path)
sys.path.insert(0, os.path.abspath('../../'))


def test_something():
    assert True


if __name__ == '__main__':
    from pprint import pprint
    client = Client(environ.get('SPLUNK_URL'), False)
    client.connect(environ.get('SPLUNK_USER'), environ.get('SPLUNK_PASSWORD'))
    cc = client.access_control.current_context()
    pprint(cc)
    fa = client.search.alert.get_fired_alerts(options=Options(count=50))
    pprint(fa)

    nose.main()
