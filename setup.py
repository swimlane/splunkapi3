from setuptools import setup
import sys
from os.path import normpath, dirname

sys.path.insert(0, normpath(dirname(__file__)))
from splunkapi3 import __version__ as _version

setup(
    name='splunkapi3',
    version=_version,
    packages=['splunkapi3',
              'splunkapi3/search',
              'splunkapi3/model'
              ],
    url='https://github.com/swimlane/splunkapi3',
    license='MIT',
    author='Dmitriy Krasnikov',
    author_email='dmitriy.krasnikov@swimlane.com',
    description='Splunk API for python 3.5',
    long_description=open('README.rst').read(),
    install_requires=[
        'requests',
        'xmltodict'
    ],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: Implementation :: PyPy',
                 ]
)
