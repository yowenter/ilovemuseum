# -*-encoding: utf-8 -*-
import logging

LOG = logging.getLogger(__name__)


class PipeLine(object):
    async def write(self, item):
        LOG.debug("PipeLine write item `%s`", item)
