from langchain.text_splitter import RecursiveCharacterTextSplitter
import load_pdf


def split_text():
    """Splits the loaded PDF text into smaller chunks"""
    documents = load_pdf.load_pdf()

    # Define chunking parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50)

    # Split into chunks
    chunks = text_splitter.split_documents(documents)

    return chunks
