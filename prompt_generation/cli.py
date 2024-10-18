import gradio as gr
from dotenv import find_dotenv
from dotenv import load_dotenv
from loguru import logger

from .openai import create_completion
from .prompt import META_PROMPT
from .utils import save_text


def generate_response(message, history):
    messages = [{"role": "system", "content": META_PROMPT}]
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
