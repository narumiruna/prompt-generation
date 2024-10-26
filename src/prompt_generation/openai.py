import functools
import os
from collections.abc import Iterable
from typing import Final

from loguru import logger
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel

DEFAULT_MODEL: Final[str] = "gpt-4o-mini"
DEFAULT_TEMPERATURE: Final[float] = 0.0


@functools.cache
def get_client() -> OpenAI:
    return OpenAI()


@functools.cache
def get_model() -> str:
    model = os.getenv("OPENAI_MODEL", DEFAULT_MODEL)
    logger.info(f"Using OpenAI model: {model}")
    return model


@functools.cache
def get_temperature() -> float:
    temperature = float(os.getenv("OPENAI_TEMPERATURE", DEFAULT_TEMPERATURE))
    logger.info(f"Using OpenAI temperature: {temperature}")
    return temperature


def create(messages: Iterable[ChatCompletionMessageParam]) -> str:
    client: OpenAI = get_client()
    model = get_model()
    temperature = get_temperature()

    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    if not completion.choices:
        raise ValueError("No completion choices returned")

    content = completion.choices[0].message.content
    if not content:
        raise ValueError("No completion message content")

    return content


def parse(messages: Iterable[ChatCompletionMessageParam], response_format: type[BaseModel]) -> BaseModel:
    client: OpenAI = get_client()
    model = get_model()
    temperature = get_temperature()

    completion = client.beta.chat.completions.parse(
        model=model,
        messages=messages,
        temperature=temperature,
        response_format=response_format,
    )

    if not completion.choices:
        raise ValueError("No completion choices returned")

    parsed = completion.choices[0].message.parsed
    if not parsed:
        raise ValueError("No parsed response")

    return parsed
