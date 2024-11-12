# prompt-generation

A specialized Python application for generating system prompts from task descriptions. It follows structured guidelines to create effective prompts for language models, featuring reasoning-first approach, example generation, and format preservation. The tool provides a modern Gradio web interface for easy interaction.

## Features

- 🎯 Intelligent prompt generation:

  - Task analysis and objective understanding
  - Reasoning-first approach with proper ordering
  - High-quality examples with placeholders
  - Format preservation for complex prompts
  - Clear and concise language

- 🚀 Modern interface:

  - Gradio web UI with queue system
  - Persistent chat history
  - One-click response copying
  - Real-time prompt generation

- ⚙️ Flexible configuration:
  - Customizable system prompts
  - Multiple OpenAI model support
  - Adjustable temperature settings

## Installation

Requires Python 3.11 or higher.

1. Install uv (Universal Virtualenv):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create virtual environment and install dependencies:

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

## Configuration

Set up your environment variables in a `.env` file:

```bash
# Required
OPENAI_API_KEY=your_api_key_here

# Optional
META_PROMPT=prompts/meta_prompt.txt  # Path to system prompt file, defaults to prompts/meta_prompt.txt
OPENAI_MODEL=gpt-4                   # Model to use, defaults to gpt-4o-mini
OPENAI_TEMPERATURE=0                 # Model temperature (0-2), defaults to 0
```

## Usage

1. Run the application:

```bash
uv run uvicorn app:app --reload
```

2. The application will launch a web interface where you can:
   - Input your task description or existing prompt
   - View generated prompts in the chat history
   - Copy results from the dedicated text area

Example Input:

```
Search for products that match a user's preference based on the provided input.
```

The tool will analyze your input and generate a structured prompt following these guidelines:

- Understanding core objectives and constraints
- Organizing reasoning steps before conclusions
- Including relevant examples with placeholders
- Preserving existing content when improving prompts
- Using clear, specific language

3. The generated prompt will be:
   - Displayed in the chat history
   - Automatically copied to the "Latest AI Response" area
   - Ready for use in your applications

## Development

The project uses several development tools:

- `ruff` for linting and formatting
- `mypy` for type checking
- `pytest` for testing

To set up the development environment:

```bash
uv pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Run linting:

```bash
ruff check .
```

## Project Structure

- `src/prompt_generation/`: Main package directory
  - `cli.py`: Command-line interface and Gradio UI implementation
  - `openai.py`: OpenAI API integration
  - `types.py`: Type definitions
  - `utils.py`: Utility functions
- `prompts/`: Directory containing system prompts
  - `meta_prompt.txt`: Core prompt generation guidelines
- `tests/`: Test directory
