import faiss
import numpy as np
from langchain.embeddings import OllamaEmbeddings
import split_text


def create_embeddings():
    """Converts text chunks into vector embeddings and stores them in FAISS"""
    chunks = split_text.split_text()

    # Use Ollama's embedding model
    embedding_model = OllamaEmbeddings(model="llama2")

    # Generate embeddings for each chunk
    embeddings = [embedding_model.embed_query(
        chunk.page_content) for chunk in chunks]

    # Convert to FAISS index
    d = len(embeddings[0])
    index = faiss.IndexFlatL2(d)
    index.add(np.array(embeddings, dtype=np.float32))

    # Save index
    faiss.write_index(index, "faiss_index.index")

    return index, chunks
