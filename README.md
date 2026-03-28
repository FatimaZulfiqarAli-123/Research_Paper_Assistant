# 🤖 Research Paper Assistant (RAG App)

A Streamlit-based AI application that allows users to upload research papers (PDFs) and ask questions using Retrieval-Augmented Generation (RAG). The system extracts text, chunks it, generates embeddings, stores them in a vector database (FAISS), and uses a local LLM (Ollama) to answer questions based only on the provided document.

---

## 🚀 Features

- 📄 Upload and process PDF research papers
- ✂️ Smart text chunking
- 🧠 Sentence-transformer embeddings (MiniLM)
- 🔍 Fast similarity search using FAISS
- 🤖 Local LLM responses using Ollama (TinyLlama)
- 💬 Ask questions based only on document content
- 🎨 Beautiful Streamlit UI with custom styling

---

## Create Virtual Enviornment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

---
## Install Dependences
pip install -r requirements.txt

---
## Run the app
streamlit run app_streamlit.py

---