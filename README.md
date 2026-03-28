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
# 📚 What is RAG (Retrieval-Augmented Generation)?

**RAG (Retrieval-Augmented Generation)** is an AI method that combines:
- 🔍 **Retrieval**: finding relevant information from a document/database  
- 🤖 **Generation**: using a language model to generate an answer based on that information  

In simple words:  
👉 *It first searches for relevant text, then uses that text to answer questions.*

---

# 🧠 Why I am using RAG in my project?

I are using RAG in my **Research Paper Assistant** because:

## 1. 📄 Answers are based on your PDF only
Instead of guessing, the system:
- extracts text from the research paper
- finds relevant chunks using FAISS
- sends only those chunks to the LLM

---

## 2. 🔍 Better accuracy (less hallucination)
Without RAG:
- LLM may guess answers

With RAG:
- LLM is forced to use document context only  
- If info is missing → it says *"Not found in the paper"*

---

## 3. ⚡ Efficient search over large documents
Research papers are long. RAG helps:
- split document into chunks
- store embeddings
- quickly retrieve top relevant sections

---

## 4. 🧠 Smarter Q&A system
Your pipeline becomes:

📄 PDF → ✂️ Chunking → 🔢 Embeddings → 🗂️ FAISS Search → 🤖 LLM Answer

---

# 🎯 Final Summary

👉 RAG = “Search first, then generate answer”  
👉 You use it to make your AI:
- more accurate  
- document-specific  
- less hallucinated  
- research-friendly
  

