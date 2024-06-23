import asyncio

from .commands import welcome as welcome_command
from .container import Container

container = Container()


def welcome():
    asyncio.run(welcome_command())
