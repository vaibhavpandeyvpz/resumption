from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .container import Container
from .routers import index_router

app = FastAPI()

container = Container()

# noinspection PyTypeChecker
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index_router)
