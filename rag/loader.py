from langchain_community.document_loaders import PyPDFLoader

def load_documents(file_path):

    print("loading document")

    loader = PyPDFLoader(file_path)
    docs = loader.load()

    print("document loaded")

    print(f"Total Pages: {len(docs)}")

    return docs