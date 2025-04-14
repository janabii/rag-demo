from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama
import os

# Initialize FastAPI app
app = FastAPI()

# Enable CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


class Query(BaseModel):
    question: str

# POST endpoint for chatbot requests


@app.post("/ask")
async def ask_question(query: Query):
    # Query the LLaMA 2 model from Ollama
    response = ollama.chat(model="llama2", messages=[
                           {"role": "user", "content": query.question}])

    # Extract response content
    answer = response.get("message", {}).get(
        "content", "Sorry, I couldn't generate a response.")
    return {"answer": answer}

# Serve the main HTML file


@app.get("/")
def get_html():
    return HTMLResponse(open("static/index.html").read())
