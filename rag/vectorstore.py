from langchain_community.vectorstores import Chroma
from rag.embedder import get_embeddings

CHROMA_PATH = "chroma_db"

def build_vectorstore(chunks):
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=CHROMA_PATH
    )
    print("Vector store built!")
    return vectorstore

def load_vectorstore():
    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embeddings()
    )