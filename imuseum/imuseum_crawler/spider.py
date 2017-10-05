# -*- encoding:utf-8 -*-
import asyncio
import os
import json
import logging
import aiohttp
import re
from collections import namedtuple

LOG = logging.getLogger(__name__)

imuseum_headers = {
    "IC-Auth-Token": os.getenv("IC-Auth-Token"),
    "IC-Device": "iPhone6,2",
    "IC-App": "IMSM-0.5",
    "IC-App-V": "IMSM-39"
}

imuseum_base_url = "http://icity.2q10.com/api/v1"


class Request(namedtuple('request', field_names=[
    'url', 'headers'
])):
    pass


class Spider(object):
    def __init__(self, start_urls):
        self.start_urls = start_urls

    def start_requests(self):
        LOG.debug("Init requests.. ")
        requests = [Request(url=url, headers=imuseum_headers.copy()) for url in self.start_urls]
        return requests

    async def fetch(self, req):
        with aiohttp.ClientSession() as session:
            async with session.get(req.url, headers=req.headers)  as response:
                if not response.status == 200:
                    LOG.warning("Fetch request `%s` status not ok", req)
                    return None
                return await response.json()

    def parse(self, data):
        LOG.debug("Parse data `%s`", data)
        # todo
        # model driver
        return [1, 2, 3]

    def extract(self, data):
        urls = _find_all_urls(data)
        LOG.debug("Extract  urls from request  `%s` count  `%s`", str(data)[:20], len(urls))
        return [Request(url=url, headers=imuseum_headers.copy()) for url in urls]

    async def download(self, req):
        LOG.debug("Downloading request `%s`", req)
        data = await  self.fetch(req)
        return data


def _find_all_urls(data):
    data_string = str(data)
    urls = re.findall(r"ic://([^']*)", data_string)
    return ["%s/%s" % (imuseum_base_url, i) for i in urls]


class iMuseumDataParser(object):
    def __init__(self, resp_json):
        self.resp_json = resp_json

    def parse(self):
        data = self.resp_json.get("data")
        if not data:
            return

        return [item for item in self.visit(data)]

    def visit(self, data):
        for k, v in data.items():
            pass

