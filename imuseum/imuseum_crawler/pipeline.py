# -*-encoding: utf-8 -*-
import logging
import os
import string
import random
import json
from urllib.parse import urlparse

LOG = logging.getLogger(__name__)

DATA_DIR = "/Users/wenter/private-repos/ilovemuseum/data"


class PipeLine(object):
    def write(self, req, item):
        LOG.debug("PipeLine write item `%s`", item)
        url = req.url
        path = urlparse(url).path + ".json"
        fpath = os.path.join(DATA_DIR, '-'.join(path.split('/')))
        if os.path.exists(fpath):
            fpath = fpath + "".join(random.sample(string.digits + string.ascii_letters, 10))
        with open(fpath, 'w') as f:
            f.write(json.dumps(item))
