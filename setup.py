from setuptools import setup

setup(
    name='splunkapi3',
    version='0.0.1',
    packages=['splunkapi3', 'splunkapi3/search'],
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
                 'Topic :: Software Development :: Libraries :: Python Modules :: Splunk'
                 ]
)
