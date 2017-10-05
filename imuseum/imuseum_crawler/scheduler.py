# -*- encoding: utf-8 -*-
import logging

logging.basicConfig()

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
logging.getLogger('asyncio').setLevel(logging.DEBUG)


class Scheduler(object):
    def __init__(self, queue):
        self.queue = queue
        self.visited_urls = set()

    def next_request(self):
        if self.queue.qsize():
            LOG.debug("Dequeue request, queue size `%s`", self.queue.qsize())
            return self.queue.get()

    def enqueue_request(self, request):
        if self.has_seen_since(request):
            return
        self.visited_urls.add(request.url)

        LOG.debug("Enqueue request `%s`, queue size `%s`", request, self.queue.qsize())
        self.queue.put(request)

    def has_seen_since(self, request, seconds=86400):
        if request.url in self.visited_urls:
            return True
        else:
            return False
