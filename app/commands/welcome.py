from dependency_injector.wiring import Provide, inject
from rq import Queue

from app.container import Container
from app.jobs import welcome as welcome_job


@inject
async def welcome(queue: Queue = Provide[Container.queue]):
    queue.enqueue(welcome_job)
