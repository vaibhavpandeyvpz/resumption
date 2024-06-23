from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration
from os import path


class Container(DeclarativeContainer):
    config = Configuration(
        ini_files=[
            path.join(path.dirname(__file__), "..", "config.ini"),
        ]
    )

    wiring_config = WiringConfiguration(
        modules=[".routers.index"],
    )
