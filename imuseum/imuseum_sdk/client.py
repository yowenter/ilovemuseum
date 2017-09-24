# -*- encoding:utf-8 -*-

import requests
import json

DEFAULT_HEADERS = {'Content-Type': 'application/json'}
DEFAULT_TIMEOUT = 10


class Client(requests.Session):
    def __init__(self, base_url, timeout=DEFAULT_TIMEOUT, headers=None, token=None):

        super(Client, self).__init__()
        if base_url.endswith("/"):
            self.base_url = base_url[:-1]
        else:
            self.base_url = base_url

        self._timeout = timeout
        self.headers = headers or DEFAULT_HEADERS.copy()
        if token:
            self.headers.update({'Authorization': 'token %s' % token})

    def _url(self, path):
        return '{0}/{1}'.format(self.base_url, path)

    def _set_params(self, kwargs):
        kwargs.setdefault('timeout', self._timeout)
        headers = kwargs.get("headers")
        if headers:
            kwargs.setdefault('headers', headers)
        return kwargs

    def _post(self, url, **kwargs):
        return self.post(url, **self._set_params(kwargs))

    def _get(self, url, **kwargs):
        return self.get(url, **self._set_params(kwargs))

    def _post_json(self, url, data, **kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        kwargs['headers']['Content-Type'] = 'application/json'
        return self._post(url, data=json.dumps(data), **self._set_params(kwargs))

    def _raise_for_status(self, response):
        """
            :param response:
            :param explanation:
            :return: None
        """

        response.raise_for_status()

    def _result(self, response, is_json=True):
        self._raise_for_status(response)
        if is_json:
            return response.json()
        else:
            return response.content

    @property
    def museum(self):
        from service.museum import Museum
        return Museum(self)



