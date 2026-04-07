from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

def load_documents(doc_path: str):
    loader = DirectoryLoader(
        doc_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} pages from PDFs")
    return documents