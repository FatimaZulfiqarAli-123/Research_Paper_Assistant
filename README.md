# 🤖 Research Paper Assistant — RAG-Based Question Answering System

A Streamlit-based AI application that allows users to upload research papers in PDF format and ask questions about their content.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the uploaded document and generate context-aware answers using a **local Large Language Model (LLM)** through Ollama.

---

## 📌 Overview

Research papers are often lengthy and contain large amounts of information, making it difficult to quickly locate specific details.

The **Research Paper Assistant** provides an interactive way to communicate with research papers using natural language.

Users can:

- Upload a research paper in PDF format
- Process and analyze the document
- Ask questions about the paper
- Retrieve relevant sections automatically
- Generate answers based on the retrieved content

The application combines **PDF processing, text chunking, embeddings, vector search, and local LLM generation** into a complete RAG pipeline.

---
## System Architecture

The system follows a **Retrieval-Augmented Generation (RAG)** architecture that processes PDF documents, retrieves relevant information based on the user's question, and generates an answer using a local LLM.

```text
┌──────────────────────────┐
│       Streamlit UI       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│       PDF Loader         │
│    Text Extraction       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│        Chunking          │
│     Text Processing      │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│       Embeddings         │
│    Sentence Transformer  │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│     FAISS Vector Store   │
└────────────┬─────────────┘
             │
             │
       User Question
             │
             ▼
┌──────────────────────────┐
│   Similarity Retrieval   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│    Retrieved Context     │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│       Ollama LLM         │
│       TinyLlama          │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│      Final Answer        │
└──────────────────────────┘
```

### Workflow

1. **Streamlit UI** – Provides the user interface for uploading PDF documents and submitting questions.
2. **PDF Loader & Text Extraction** – Extracts textual content from the uploaded PDF documents.
3. **Chunking & Text Processing** – Splits the extracted text into smaller chunks for efficient processing and retrieval.
4. **Embeddings** – Converts each text chunk into a numerical vector using a Sentence Transformer model.
5. **FAISS Vector Store** – Stores the generated embeddings and enables fast similarity-based searching.
6. **Similarity Retrieval** – Converts the user's question into an embedding and retrieves the most relevant document chunks from FAISS.
7. **Retrieved Context** – The relevant chunks are provided as context to the language model.
8. **Ollama + TinyLlama** – Uses the locally running TinyLlama model through Ollama to generate a response based on the retrieved context.
9. **Final Answer** – Displays the generated answer to the user through the Streamlit interface.

### Architecture Overview

The application uses a **RAG (Retrieval-Augmented Generation)** approach. Instead of sending the entire PDF directly to the LLM, relevant information is first retrieved from the FAISS vector database. This retrieved context is then passed to TinyLlama, allowing the model to generate answers based on the contents of the uploaded documents.

---

## 🚀 Features

- 📄 Upload research papers in PDF format
- ✂️ Smart text chunking
- 🧠 Sentence Transformer embeddings
- 🔍 Semantic similarity search
- ⚡ Fast vector search using FAISS
- 🤖 Local LLM inference using Ollama
- 💬 Natural-language question answering
- 📚 Answers based on the uploaded document
- 🛡️ Reduced hallucination through retrieved context
- 🎨 Interactive Streamlit interface
- 🔒 Local document and LLM processing

---

# 📚 What is RAG?

**RAG (Retrieval-Augmented Generation)** is an AI architecture that combines information retrieval with language generation.

Instead of asking a Large Language Model to answer a question using only its pretrained knowledge, RAG first retrieves relevant information from an external knowledge source and then provides that information to the LLM as context.

### In simple terms:

> **RAG = Retrieve relevant information → Generate an answer using that information**

In this project, the external knowledge source is the **uploaded research paper**.

---

# 🧠 Why Use RAG in This Project?

RAG is used in the Research Paper Assistant for several reasons.

## 1. 📄 Document-Specific Answers

The system retrieves information directly from the uploaded research paper.

Instead of relying entirely on the general knowledge of an LLM, the model receives relevant sections of the document as context.

This makes the application suitable for:

- Research papers
- Academic articles
- Technical documents
- Reports
- Documentation
- Long PDF files

---

## 2. 🛡️ Reduced Hallucination

Large Language Models can sometimes generate information that is not supported by the provided document.

RAG helps reduce this problem by retrieving relevant document content before generating an answer.

The application is designed to instruct the LLM to answer using the retrieved context and indicate when the requested information cannot be found in the document.

---

## 3. ⚡ Efficient Search

Research papers can contain many pages of text.

Reading the entire document for every question would be inefficient.

RAG divides the document into smaller chunks and converts them into vector representations. FAISS can then quickly search for the chunks that are most semantically similar to the user's question.

---

## 4. 🧠 Better Question Answering

The system combines:

- Document retrieval
- Semantic embeddings
- Vector similarity search
- Large Language Model generation

This creates a more useful question-answering system for research documents.

---

# 🔄 RAG Pipeline

The complete workflow of the application is:


                📄 PDF Research Paper
                         │
                         ▼
                 📑 Text Extraction
                         │
                         ▼
                    ✂️ Chunking
                         │
                         ▼
                🧠 Text Embeddings
                         │
                         ▼
                 🗂️ FAISS Vector Store
                         │
                         │
                    User Question
                         │
                         ▼
                 🧠 Question Embedding
                         │
                         ▼
                🔍 Similarity Search
                         │
                         ▼
              📚 Relevant Text Chunks
                         │
                         ▼
                   🤖 Local LLM
                      Ollama
                         │
                         ▼
                  💬 Final Answer
