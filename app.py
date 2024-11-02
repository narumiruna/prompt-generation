import json
import os

from dotenv import find_dotenv
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi import Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from loguru import logger

from prompt_generation.openai import create
from prompt_generation.utils import load_text

# Load environment variables
load_dotenv(find_dotenv())

# Initialize FastAPI app
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load system prompt
prompt_file = os.getenv("META_PROMPT", "prompts/meta_prompt.txt")
SYSTEM_PROMPT = load_text(prompt_file)


@app.post("/generate_response", response_class=JSONResponse)
async def generate_response(message: str = Form(...), history: str = Form(...)) -> dict:
    logger.info("Received message: {}", message)
    logger.info("Received history: {}", history)

    try:
        history_list = json.loads(history) if history else []
    except json.JSONDecodeError as e:
        logger.error("Invalid history format: {}", e)
        history_list = []

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *[{"role": "user", "content": hist["content"]} for hist in history_list],
        {"role": "user", "content": message},
    ]

    logger.info("messages: {}", messages)

    try:
        response = create(messages)
        logger.info("response: {}", response)
        history_list.append({"role": "user", "content": message})
        history_list.append({"role": "assistant", "content": response})
        return {"message": "", "history": history_list}
    except Exception as e:
        logger.error("Unable to generate response: {}", e)
        error_msg = str(e)
        history_list.append({"role": "user", "content": message})
        history_list.append({"role": "assistant", "content": error_msg})
        return {"message": "", "history": history_list}


@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request, "history": []})
