# -*- encoding: utf-8 -*-



import logging

from datetime import datetime

logging.basicConfig()

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


class Engine(object):
    '''
     参考了 scrapy 的 架构 https://docs.scrapy.org/en/latest/topics/architecture.html
     设计理念是 控制流(Scheduler)和数据流(Spider)的分离。
    '''

    def __init__(self, spider, scheduler, pipeline):
        self.spider = spider
        self.scheduler = scheduler
        self.pipeline = pipeline
        self.running = False

    async def start(self):
        LOG.info("Engine started at %s", datetime.now())
        self.running = True
        init_requests = await self.spider.start_requests()
        [self.scheduler.enquest_request(rq) for rq in init_requests]

        while self.running:
            req = self.scheduler.next_request()
            next_requests = await  self.workflow(req)
            for req in next_requests:
                self.scheduler.enquest_request(req)

    async def workflow(self, req):
        response = await self.spider.download(req)
        items = self.spider.parse(response)
        next_requests = self.spider.screw(response)
        for item in items:
            await self.pipeline.write(item)
        return next_requests

    def stop(self):
        LOG.info("Engine stopped at `%s`", datetime.now())
        self.running = False


if __name__ == '__main__':
    engine = Engine(None, None, None)

    engine.start()
