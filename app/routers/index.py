from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from typing import Any, Dict

from app.container import Container

index_router = APIRouter()


class IndexResponse(BaseModel):
    env: str


@index_router.get("/", status_code=status.HTTP_200_OK, response_model=IndexResponse)
@inject
async def index(
    config: Dict[str, Any] = Depends(Provide[Container.config]),
) -> IndexResponse:
    return IndexResponse(env=config["app"]["env"])
