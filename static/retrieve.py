import faiss
import numpy as np
from langchain.embeddings import OllamaEmbeddings
import split_text
import create_embeddings

# Load embeddings and text chunks
index, chunks = create_embeddings.create_embeddings()


def retrieve_documents(query):
    """Retrieves the most relevant text chunks for a given query."""
    embedding_model = OllamaEmbeddings(model="llama2")

    # Embed the query
    query_embedding = np.array(
        [embedding_model.embed_query(query)], dtype=np.float32)

    # Search FAISS index
    _, indices = index.search(query_embedding, 5)  # Get top 5 results

    print(_, indices=index.search(query_embedding, 5))

    # Retrieve matching chunks
    relevant_content = ""
    for idx in indices[0]:
        if idx < len(chunks):
            relevant_content += chunks[idx].page_content + "\n"

    return relevant_content
