from dependency_injector.wiring import Provide, inject
from drymail import SMTPMailer, Message

from app.container import Container


@inject
async def welcome(
    mailer: SMTPMailer = Provide[Container.mailer],
):
    message = Message(
        sender=("John Doe", "john.doe@example.com"),
        receivers=[("Johnny Depp", "johnny.depp@example.com")],
        subject="Welcome to Python",
        text="Not bad, huh?",
    )

    mailer.send(message)
