import os
import sys
import nose
from splunkapi3.core import *
from os.path import join, dirname
from dotenv import load_dotenv
from os import environ

dot_env_path = join(dirname(__file__), '../', '.env')
load_dotenv(dot_env_path)
sys.path.insert(0, os.path.abspath('../../'))


def test_something():
    assert True


if __name__ == '__main__':
    from pprint import pprint
    client = Client(environ.get('url'), False)
    client.connect(environ.get('user'), environ.get('password'))
    cc = client.access_control.current_context()
    pprint(cc)
    fa = client.search.alert.get_fired_alerts()
    pprint(fa)

    nose.main()
