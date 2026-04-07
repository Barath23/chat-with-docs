# 📄 Chat with Your Docs — RAG System

A Retrieval-Augmented Generation (RAG) application that lets you chat with your PDF documents using free HuggingFace models. No OpenAI API key required!

---

## 🎯 What It Does

- Upload any PDF documents
- Ask questions in natural language
- Get accurate answers with source references
- Runs completely free using HuggingFace models

---

## 🏗️ Architecture

PDF Files → Loader → Chunker → Embeddings → Vector Store (ChromaDB)
                                                        ↓
User Question → Embeddings → Similarity Search → Top K Chunks
                                                        ↓
                                          LLM → Answer with Sources

---

## 🛠️ Tech Stack

| Component        | Tool                                      |
|------------------|-------------------------------------------|
| Framework        | LangChain                                 |
| LLM              | Mistral-7B-Instruct (HuggingFace API)     |
| Embeddings       | all-MiniLM-L6-v2 (sentence-transformers) |
| Vector Store     | ChromaDB                                  |
| PDF Loader       | PyPDF                                     |
| UI               | Streamlit                                 |

---

## 📁 Project Structure

chat-with-docs/
├── app.py                  # Streamlit UI
├── rag/
│   ├── __init__.py
│   ├── loader.py           # PDF loading
│   ├── chunker.py          # Text splitting
│   ├── embedder.py         # Embeddings
│   ├── vectorstore.py      # ChromaDB setup
│   └── retriever.py        # Search + LLM chain
├── data/
│   └── docs/               # Drop your PDFs here
├── .env                    # API keys
├── requirements.txt
└── README.md

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Barath23/chat-with-docs.git
cd chat-with-docs
```

### 2. Create Virtual Environment
```bash
conda create -n genai python=3.10 -y

# Activate
conda activate genai
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get HuggingFace API Token
- Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- Create a free account and generate a token

### 5. Set Up Environment Variables
Create a `.env` file in the root folder:
HUGGINGFACEHUB_API_TOKEN=your_token_here

### 6. Add Your PDFs
Drop your PDF files into the data/docs/ folder

---
## 🚀 Run the App
```bash
streamlit run app.py
```

Then:
1. Open `http://localhost:8501` in your browser
2. Click **"Index PDFs"** in the sidebar
3. Start asking questions!

---

## 💬 Example Usage
User:  What is the main topic of the document?
Bot:   The document covers... (Source: myfile.pdf)
User:  Summarize chapter 2
Bot:   Chapter 2 discusses... (Source: myfile.pdf)
User:  What are the key findings?
Bot:   The key findings are... (Source: myfile.pdf)

---

## 🧪 Experiments to Try

| Experiment         | Parameter              | Values to Test     |
|--------------------|------------------------|--------------------|
| Chunk size         | `chunk_size`           | 200, 500, 1000     |
| Retrieved chunks   | `k`                    | 2, 4, 6            |
| Search type        | `search_type`          | similarity, mmr    |
| Temperature        | `temperature`          | 0, 0.2, 0.5        |

---

## 🔧 Configuration

You can tweak settings in each module:

**Chunking** (`rag/chunker.py`)
```python
chunk_size=500       # Characters per chunk
chunk_overlap=50     # Overlap between chunks
```

**Retrieval** (`rag/retriever.py`)
```python
search_kwargs={"k": 4}   # Number of chunks retrieved
temperature=0.2           # LLM creativity (0 = focused)
max_new_tokens=512        # Max response length
```

---

## 🆚 LLM Options

| Option              | Model                          | Setup      | Cost    |
|---------------------|--------------------------------|------------|---------|
| HuggingFace API     | Mistral-7B-Instruct            | Easy       | Free    |
| Ollama (Local)      | mistral / llama3               | Medium     | Free    |
| OpenAI (Optional)   | gpt-4o-mini                    | Easy       | Paid    |

**Switch to Ollama (Local):**
```bash
ollama pull mistral
```
```python
from langchain_community.llms import Ollama
llm = Ollama(model="mistral")
```

---

## 🚧 Known Limitations

- HuggingFace free tier has rate limits (may slow down with heavy use)
- Large PDFs (100+ pages) may take time to index
- Answer quality depends on chunk size and retrieval settings

---

## 🔮 Future Improvements

- [ ] Conversational memory (multi-turn chat)
- [ ] Support DOCX, TXT, and web URLs
- [ ] Add Cohere re-ranker for better retrieval
- [ ] Show source chunks highlighted in UI
- [ ] Swap ChromaDB for Pinecone (cloud)
- [ ] Evaluation pipeline using RAGAS

---

## 📚 What I Learned

- How RAG pipelines work end-to-end
- Text chunking strategies and their impact on quality
- Vector embeddings and semantic search
- Prompt engineering for grounded answers
- Integrating HuggingFace models with LangChain

---

## 👤 Author

**Barath Kumar Ramamoorthi**
- GitHub: [Barath23](https://github.com/Barath23)
- LinkedIn: [barath-kumar-r-2302](https://linkedin.com/in/barath-kumar-r-2302)
