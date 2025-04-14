import load_pdf
import split_text
import create_embeddings
import retrieve


def main():
    print("Loading PDF...")
    load_pdf.load_pdf()

    print("Splitting text into chunks...")
    split_text.split_text()

    print("Creating embeddings and storing in FAISS...")
    create_embeddings.create_embeddings()

    print("Ready! You can now ask a question via FastAPI.")


if __name__ == "__main__":
    main()
