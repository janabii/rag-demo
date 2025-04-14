# rag-demo
# RAG System with LLaMA, FAISS & FastAPI

This project is a Retrieval-Augmented Generation (RAG) system developed during my internship. It combines local document retrieval with LLaMA-based language generation (via [Ollama](https://ollama.com)) and serves results through a FastAPI backend. You can upload a PDF and ask questions about its content.

---

## Features

- Local LLM generation using LLaMA via Ollama  
- PDF parsing and intelligent chunking  
- Vector-based document retrieval with FAISS  
- REST API built with FastAPI and a lightweight frontend  
- Modular components for embedding, search, and generation  

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/janabii/rag-demo.git
cd rag-demo

pip install -r requirements.txt

ollama run llama2

### Usage

Step 1: Run the FastAPI server
Simply run the following command in your terminal to start the FastAPI server:

fastapi run api.py

Open http://0.0.0.0:8000 in your browser to test the system. You can now query the system and get answers based on the content of the data/example.pdf.

the current pdf im using is monopoly game instructions, (I love monopoly).

### How it works

-PDF is loaded and split into smaller, overlapping text chunks.
-Embeddings are generated using LangChain and stored in a FAISS index.
-At query time, relevant chunks are retrieved from FAISS.
-These chunks are passed into LLaMA via Ollama for final answer generation.
-Results are served via FastAPI and rendered in the frontend.

### License
MIT License

Copyright (c) 2025, Ahmed Al Janabi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### Author

Built by Ahmed Al Janabi during my internship to explore RAG systems with open-source tools and local language models.
