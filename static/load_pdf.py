from langchain_community.document_loaders import PyPDFLoader


def load_pdf():
    """Loads a PDF file and extracts text"""
    loader = PyPDFLoader("data/example.pdf")
    documents = loader.load()
    return documents
