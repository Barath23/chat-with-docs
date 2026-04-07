from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,       # characters per chunk
        chunk_overlap=50,     # overlap to preserve context
        separators=["\n\n", "\n", ".", " "]
    )
    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")
    return chunks