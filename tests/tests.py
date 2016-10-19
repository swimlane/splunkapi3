import os
import sys
from os import environ
from os.path import join, dirname, normpath
import nose
from dotenv import load_dotenv
from splunkapi3.client import Client
from splunkapi3.model import Options, SearchCreate

dot_env_path = normpath(join(dirname(__file__), '../', '.env'))
load_dotenv(dot_env_path)
sys.path.insert(0, os.path.abspath('../../'))


def test_something():
    assert True


if __name__ == '__main__':
    from pprint import pprint
    client = Client(environ.get('SPLUNK_URL'), False)
    client.connect(environ.get('SPLUNK_USER'), environ.get('SPLUNK_PASSWORD'))
    # cc = client.access_control.current_context()

    # r = client.search.job.get_jobs(options=Options(count=50))
    # pprint(r)
    # r1 = client.search.job.results('scheduler__nobody_c3BsdW5rX2FyY2hpdmVy__RMD5473cbac83d6c9db7_at_1476796620_5736')
    # r1 = client.search.util.time_parser(['-5h', '-6'])
    # r1 = client.search.util.type_ahead(prefix='source', count=3)
    r1 = client.search.job.export_oneshot("search index=* sourcetype=apache_error Severity=error")
    pprint(r1)

    nose.main()
