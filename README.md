# prompt-generation

A Python application that provides a chat interface for interacting with OpenAI's API, featuring a Gradio-based UI with easy response copying functionality.

## Installation

Requires Python 3.11 or higher.

1. Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create virtual environment and install dependencies:

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Usage

1. Set up your environment variables in a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
META_PROMPT=prompts/meta_prompt.txt  # Optional, defaults to this path
```

2. Run the application:

```bash
prompt-generation
```
