import os

import gradio as gr
from dotenv import find_dotenv
from dotenv import load_dotenv
from loguru import logger

from .openai import create_completion
from .utils import load_text
from .utils import save_text

prompt_file = os.getenv("META_PROMPT", "prompts/meta_prompt.txt")

SYSTEM_PROMPT = load_text(prompt_file)


def generate_response(message, history) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages += history
    messages += [{"role": "user", "content": message}]

    logger.info("messages: {}", messages)

    try:
        response = create_completion(messages)
        logger.info("response: {}", response)
        save_text(response, "prompt.txt")
        return response
    except Exception as e:
        logger.error("unable to generate response: {}", e)
        return str(e)


def main() -> None:
    load_dotenv(find_dotenv())
    gr.ChatInterface(generate_response, type="messages").launch()
