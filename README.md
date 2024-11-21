# prompt-generation

A specialized Python application for generating system prompts from task descriptions. It follows structured guidelines to create effective prompts for language models, featuring a reasoning-first approach, example generation, and format preservation. The tool provides a modern Gradio web interface for easy interaction.

## Features

- 🎯 **Intelligent Prompt Generation**:

  - Comprehensive task analysis and clear objective understanding
  - Reasoning-first methodology with proper step ordering
  - Inclusion of high-quality examples with placeholders
  - Preservation of complex prompt formats
  - Emphasis on clarity and conciseness

- 🚀 **Modern Interface**:

  - Gradio web UI with queue system
  - Persistent chat history
  - One-click response copying
  - Real-time prompt generation

- ⚙️ **Flexible Configuration**:
  - Customizable system prompts
  - Multiple OpenAI model support
  - Adjustable temperature settings

## Installation

Requires Python 3.11 or higher.

Install uv:

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
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

1. **Run the application**:

   ```bash
   uv run prompt-generation
   ```

2. **Access the web interface**:

   - Input your task description or existing prompt
   - View generated prompts in the chat history
   - Copy results from the dedicated text area

   **Example Input**:

   ```
   Search for products that match a user's preference based on the provided input.
   ```

   The tool analyzes your input and generates a structured prompt following key guidelines:

   - Understanding core objectives and constraints
   - Organizing reasoning steps before conclusions
   - Including relevant examples with placeholders
   - Preserving existing content when improving prompts
   - Using clear and specific language

3. **Utilize the generated prompt**:
   - Displayed in the chat history
   - Automatically copied to the "Latest AI Response" area
   - Ready for integration into your applications

## Development

The project utilizes several development tools:

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
