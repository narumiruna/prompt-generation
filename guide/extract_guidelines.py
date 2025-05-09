from pathlib import Path

from agents import Agent
from agents import ModelSettings
from agents import Runner
from dotenv import find_dotenv
from dotenv import load_dotenv
from pydantic import BaseModel
from rich import print


class Step(BaseModel):
    explanation: str
    output: str


class Reasoning(BaseModel):
    steps: list[Step]
    final_output: str


class Guideline(BaseModel):
    reasoning: Reasoning
    description: str


class Guidelines(BaseModel):
    guidelines: list[Guideline]

    def __str__(self) -> str:
        return "\n".join([f"- {guideline.description}" for guideline in self.guidelines])


def main(output_file: str = "guidelines.txt") -> None:
    load_dotenv(find_dotenv(), override=True)
    with Path("guide/gpt4-1_prompting_guide.md").open(encoding="utf-8") as fp:
        markdown = fp.read()

    instructions = (
        "Extract guidelines from the markdown file." "Do not fabricate any information." "Do not miss any details."
    )
    agent = Agent(
        name="guidelines-extractor",
        instructions=instructions,
        model="gpt-4.1",
        model_settings=ModelSettings(temperature=0.0),
        output_type=Guidelines,
    )

    result = Runner.run_sync(agent, input=markdown)

    text = str(result.final_output)
    print(text)
    Path(output_file).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
