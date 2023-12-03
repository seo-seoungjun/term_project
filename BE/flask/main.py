from fastapi import FastAPI, File, UploadFile, Form
import os
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from model.summarizer import OpenAIManager
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
load_dotenv('env/.env')
origins = [
    "http://localhost",
    "http://localhost:3000"
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestModel(BaseModel):
    grammar: str
    max_tokens: int
    temperature: float
    number_messages: int
    presence_penalty: float
    frequency_penalty: float
    user_message: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send")
async def receive_data(file: UploadFile = File(...), grammar: str = Form(...), max_tokens: int = Form(...),
                       temperature: float = Form(...), number_messages: int = Form(...),
                       presence_penalty: float = Form(...), frequency_penalty: float = Form(...),
                       user_message: str = Form(...)):
    settings = RequestModel(
        grammar=grammar,
        max_tokens=max_tokens,
        temperature=temperature,
        number_messages=number_messages,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        user_message=user_message
    )

    manager = OpenAIManager()
    assistant_id = os.getenv('ASSISTANT_ID')
    assistant = manager.client.beta.assistants.retrieve(assistant_id)
    prompt = settings.user_message
    thread, run = manager.create_thread_and_run(assistant, prompt)
    run = manager.wait_on_run(run, thread)
    response = manager.get_response(thread)
    manager.pretty_print(manager.get_response(thread))

    return response


