import streamlit as st
from rag.loader import load_documents
from rag.chunker import chunk_documents
from rag.vectorstore import build_vectorstore, load_vectorstore
from rag.retriever import build_qa_chain, ask
import os

st.set_page_config(page_title="Chat with Your Docs", page_icon="📄")
st.title("📄 Chat with Your Docs")

# Sidebar: Upload & Index
with st.sidebar:
    st.header("📂 Add Documents")
    if st.button("Index PDFs in /data/docs"):
        with st.spinner("Loading and indexing..."):
            docs = load_documents("data/docs")
            chunks = chunk_documents(docs)
            build_vectorstore(chunks)
        st.success("Done! Ready to chat.")

# Load vector store and chain
if os.path.exists("chroma_db"):
    vectorstore = load_vectorstore()
    qa_chain = build_qa_chain(vectorstore)

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if question := st.chat_input("Ask anything about your documents..."):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer, sources = ask(qa_chain, question)
            st.write(answer)
            if sources:
                st.caption(f"📎 Sources: {', '.join(sources)}")
        
        st.session_state.messages.append({"role": "assistant", "content": answer})
else:
    st.info("👈 Add PDFs to /data/docs and click 'Index PDFs' to get started.")