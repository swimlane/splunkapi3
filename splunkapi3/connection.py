from typing import Union, List, Tuple
from urllib.parse import urlunparse, urlparse, urljoin
from requests import get, post, delete
from splunkapi3.data import load, Record
from splunkapi3.model.options import Options
from splunkapi3.status_codes import code_description


class Connection(object):

    def __init__(self, url: str, verify: bool=True):
        """
        Constructor
        :param url: The Splunk api url. 'https://localhost:
        :param verify: To verify SSL certificate or not. More for a development, qa.
        """
        self.url = self.clean_url(url)
        self.verify = verify
        self._session_key = None

    @property
    def session_key(self):
        return self._session_key

    @session_key.setter
    def session_key(self, value):
        self._session_key = value

    @property
    def headers(self):
        headers = {'Authorization': 'Splunk {key}'.format(key=self.session_key)} \
            if self._session_key else {}
        return headers

    @staticmethod
    def clean_url(url: str)->str:
        url_obj = urlparse(url, 'https')
        return urlunparse([url_obj.scheme, url_obj.netloc,
                           '/services/', None, None, False])

    @staticmethod
    def get_parameters(params: Union[dict, List[Tuple]], options: Options)->List[Tuple]:
        """
        Translates options into parameters and merges with parameters.
        :param params: Parameters specific to method.
        :param options: Generic pagination and filtering parameters.
        :return: Merged dictionary.
        """
        parameters = list(options.dict.items()) if options else []
        if params:
            parameters.extend(params.items() if isinstance(params, dict) else params)
        return parameters

    def get(self, relative_url: str,
            params: Union[dict, List[Tuple]]=None, options: Options=None)->str:
        _full_url = urljoin(self.url, relative_url)
        parameters = self.get_parameters(params, options)
        response = get(url=_full_url, params=parameters, headers=self.headers, verify=self.verify)
        self.validate_response(response)
        return response.content

    def get_record(self,
                   relative_url: str,
                   params: Union[dict, List[Tuple]]=None,
                   options: Options=None)->Record:
        """
        Return results of get request parsed and wrapped in Record.
        :param relative_url: Relative url of REST call
        :param params: Parameters for the call
        :param options: Paging and filtering parameters.
        :return: Record object.
        """
        return load(self.get(relative_url=relative_url, params=params, options=options))

    @staticmethod
    def validate_response(response):
        code = response.status_code
        if code != 200 and code != 201:
            message = code_description.get(code)
            if code in [400, 409, 500]:
                message += response.text
            raise ConnectionError(message)

    def post(self, relative_url: str, params: dict=None, data: dict=None)->str:
        full_url = urljoin(self.url, relative_url)
        response = post(url=full_url, headers=self.headers,
                        params=params, data=data, verify=self.verify)
        self.validate_response(response)
        return response.content

    def delete(self, relative_url: str):
        full_url = urljoin(self.url, relative_url)
        response = delete(url=full_url, headers=self.headers, verify=self.verify)
        self.validate_response(response)
