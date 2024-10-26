import os
from collections.abc import Iterable

import gradio as gr
from dotenv import find_dotenv
from dotenv import load_dotenv
from loguru import logger
from openai.types.chat import ChatCompletionMessageParam
from openai.types.chat import ChatCompletionSystemMessageParam
from openai.types.chat import ChatCompletionUserMessageParam

from .openai import create
from .utils import load_text

prompt_file = os.getenv("META_PROMPT", "prompts/meta_prompt.txt")

SYSTEM_PROMPT = load_text(prompt_file)


def generate_response(message: str, history: list[dict[str, str]]) -> tuple[str, list[dict[str, str]]]:
    messages: Iterable[ChatCompletionMessageParam] = [
        ChatCompletionSystemMessageParam(role="system", content=SYSTEM_PROMPT),
        *[ChatCompletionUserMessageParam(role="user", content=hist["content"]) for hist in history],
        ChatCompletionUserMessageParam(role="user", content=message),
    ]

    logger.info("messages: {}", messages)

    try:
        response = create(messages)
        logger.info("response: {}", response)
        return "", history + [{"role": "user", "content": message}, {"role": "assistant", "content": response}]
    except Exception as e:
        logger.error("unable to generate response: {}", e)
        error_msg = str(e)
        return "", history + [{"role": "user", "content": message}, {"role": "assistant", "content": error_msg}]


def get_last_response(history: list[dict[str, str]]) -> str:
    """Get the last assistant response from chat history."""
    for msg in reversed(history):
        if msg["role"] == "assistant":
            return msg["content"]
    return ""


def main() -> None:
    load_dotenv(find_dotenv())

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(height=750, type="messages")
        msg = gr.Textbox(placeholder="Enter your message here...", container=False, scale=7)
        with gr.Row():
            submit = gr.Button("Submit", scale=1)

        last_response = gr.Textbox(
            label="Latest AI Response (Click to select all and copy)", interactive=True, lines=10
        )

        submit.click(
            generate_response,
            inputs=[msg, chatbot],
            outputs=[msg, chatbot],
        ).then(get_last_response, inputs=[chatbot], outputs=[last_response])

    demo.queue().launch()
