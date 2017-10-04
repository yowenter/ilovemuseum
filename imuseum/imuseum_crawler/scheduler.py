# -*- encoding: utf-8 -*-
import logging

logging.basicConfig()

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
logging.getLogger('asyncio').setLevel(logging.DEBUG)


class Scheduler(object):
    def __init__(self, queue):
        self.queue = queue

    def next_request(self):
        if self.queue.qsize():
            return self.queue.get()

    def enqueue_request(self, request):
        LOG.debug("Enqueue request `%s`", request)
        if self.has_seen_since(request):
            return

        self.queue.put(request)
        LOG.debug("Queue size `%s`", self.queue.qsize())

    def has_seen_since(self, request, seconds=86400):
        return False
