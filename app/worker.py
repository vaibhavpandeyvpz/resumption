from dependency_injector.wiring import Provide, inject
from redis import Redis
from rq import Queue, Worker

from .container import Container


@inject
def work(
    queue: Queue = Provide[Container.queue], redis: Redis = Provide[Container.redis]
):
    worker = Worker([queue], connection=redis)
    worker.work()


def main():
    container = Container()
    container.wire(modules=[__name__])
    work()
