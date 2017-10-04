# -*- encoding:utf-8 -*-
import asyncio
import os
import logging
import aiohttp
from collections import namedtuple

LOG = logging.getLogger(__name__)

imuseum_headers = {
    "IC-Auth-Token": os.getenv("IC-Auth-Token"),
    "IC-Device": "iPhone6,2",
    "IC-App": "IMSM-0.5",
    "IC-App-V": "IMSM-39"
}


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
        async with aiohttp.ClientSession() as session:
            async with session.get(req.url, headers=req.headers)  as response:
                return response.json()

    def parse(self, resp):
        LOG.debug("Parse response `%s`", resp)
        # todo
        # model driver
        return ['item1', 'item2', 'item3']

    def extract(self, resp):
        LOG.debug("Extract request `%s`", resp)
        # todo
        return []

    async def download(self, req):
        LOG.debug("Downloading request `%s`", req)
        return self.fetch(req)
