# -*- encoding: utf-8 -*-



import logging

import queue
from datetime import datetime
import traceback

logging.basicConfig()

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
logging.getLogger("imuseum_crawler").setLevel(logging.DEBUG)

import asyncio


class Engine(object):
    '''
     参考了 scrapy 的 架构 https://docs.scrapy.org/en/latest/topics/architecture.html
     设计理念是 控制流(Scheduler)和数据流(Spider)的分离。
    '''

    def __init__(self, spider, scheduler, pipeline, loop=None, workers_num=3):
        self.spider = spider
        self.scheduler = scheduler
        self.pipeline = pipeline
        self.running = False
        self.workers_num = workers_num
        self.loop = loop or asyncio.get_event_loop()

    async def start(self):
        LOG.info("Engine started at %s", datetime.now())
        self.running = True
        init_requests = self.spider.start_requests()
        [self.scheduler.enqueue_request(rq) for rq in init_requests]
        await  asyncio.wait([self.work(_) for _ in range(self.workers_num)])

    async def work(self, worker_no):
        LOG.debug("Worker `%s` start working", worker_no)
        while self.running:
            req = self.scheduler.next_request()
            if not req:
                await asyncio.sleep(3)
                continue

            LOG.debug("Worker `%s` working on `%s`", worker_no, req)
            next_requests = await self.workflow(req)
            LOG.debug("Worker `%s` enqueue next requests `%s`", worker_no, len(next_requests))
            if not next_requests:
                continue
            for req in next_requests:
                self.scheduler.enqueue_request(req)

    async def workflow(self, req):
        try:

            response = await self.spider.download(req)
            # items = self.spider.parse(response)
            next_requests = self.spider.extract(response)
            # if items:
            #     for item in items:
            self.pipeline.write(req, response)
        except Exception as e:

            LOG.warning("Exception: `%s`, traceback `%s`", str(e), traceback.format_exc())
            next_requests = []

        return next_requests

    def stop(self):
        LOG.info("Engine stopped at `%s`", datetime.now())
        self.running = False


from imuseum_crawler.spider import Spider
from imuseum_crawler.scheduler import Scheduler
from imuseum_crawler.pipeline import PipeLine

if __name__ == '__main__':
    q = queue.Queue()
    p = PipeLine()
    s = Spider(["http://icity.2q10.com/api/v1/imsm/users/43q3tza"])
    sche = Scheduler(q)
    engine = Engine(s, sche, p)
    loop = asyncio.get_event_loop()
    task = loop.create_task(engine.start())
    loop.run_until_complete(task)
    loop.close()
