from pathlib import Path

import chainlit as cl
from agents import Agent
from agents import ModelSettings
from agents import Runner
from agents import TResponseInputItem
from dotenv import find_dotenv
from dotenv import load_dotenv

load_dotenv(find_dotenv(), override=True)


def load_text(f: str) -> str:
    with Path(f).open(encoding="utf-8") as fp:
        return fp.read()


class Bot:
    def __init__(self, f: str = "guide/gpt4-1_prompting_guide.md") -> None:
        prompting_guide = load_text(f)
        self.agent = Agent(
            name="prompt-engineer",
            instructions=(
                "You are prompt engineer expert.\n"
                "You will follow the prompting guide to generate the best prompt.\n"
                f"Prompting guide:\n{prompting_guide}"
            ),
            model="gpt-4.1",
            model_settings=ModelSettings(temperature=0.0),
        )

        self.messages: list[TResponseInputItem] = []

    async def run(self, content: str) -> str:
        self.messages.append(
            {
                "role": "user",
                "content": content,
            }
        )
        result = await Runner.run(self.agent, input=self.messages)
        self.messages = result.to_input_list()

        return str(result.final_output)


bot = Bot()


@cl.on_message
async def main(message: cl.Message) -> None:
    result = await bot.run(message.content)
    await cl.Message(content=result).send()
