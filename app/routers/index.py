from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
import json
from openai import OpenAI
import os
from pydantic import BaseModel
import pymupdf4llm
from tempfile import NamedTemporaryFile
from typing import Annotated, Any, Dict

from app.container import Container
from app.schema import Resume

index_router = APIRouter()


class IndexResponse(BaseModel):
    env: str


@index_router.get("/", status_code=status.HTTP_200_OK, response_model=IndexResponse)
@inject
async def index(
    config: Dict[str, Any] = Depends(Provide[Container.config]),
) -> IndexResponse:
    return IndexResponse(env=config["app"]["env"])


@index_router.post(
    "/process", status_code=status.HTTP_200_OK, response_model=Dict[str, Any]
)
@inject
async def process(
    resume: Annotated[UploadFile, File(description="Resume as a PDF file.")],
    openai: OpenAI = Depends(Provide[Container.openai]),
    config: Dict[str, Any] = Depends(Provide[Container.config]),
) -> Dict[str, Any]:
    if resume.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is not a PDF file.",
        )
    # save the PDF temporary
    out_file = NamedTemporaryFile(delete=False)
    with out_file:
        while content := resume.file.read(1024 * 1024):
            out_file.write(content)

    try:
        # get the PDF content
        text = pymupdf4llm.to_markdown(out_file.name)

        # parse as JSON format
        completion = openai.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a bot that parses information from resume's text content into structured JSON.",
                },
                {
                    "role": "user",
                    "content": "Following is the text content (in markdown) extracted from an uploaded PDF resume."
                    "Parse it into JSON format.",
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
            model=config["openai"]["model"],
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "format_resume",
                        "description": "Restructure data extracted from resume to the defined JSON schema.",
                        "parameters": Resume,
                    },
                },
            ],
            tool_choice={"type": "function", "function": {"name": "format_resume"}},
        )

        choice = completion.choices[0]
        tool_call = choice.message.tool_calls[0]
        output = json.loads(tool_call.function.arguments)

        return output
    except Exception as e:
        raise e
    finally:
        os.unlink(out_file.name)
