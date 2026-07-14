# Retrieval-Augmented Generation (RAG) System using LangChain and FAISS

## Overview

This project demonstrates the implementation of a Retrieval-Augmented Generation (RAG) system using LangChain, FAISS, and Hugging Face Embeddings. The system retrieves relevant information from research papers before generating responses, improving factual accuracy compared to traditional Large Language Models.

The project was developed as part of the **Large Language Models, Prompting, and Agentic AI** course at **SRH University of Applied Sciences**.

---

## Features

- Load multiple PDF research papers
- Split documents into semantic text chunks
- Generate vector embeddings using Hugging Face
- Store embeddings in a FAISS Vector Database
- Retrieve relevant document chunks using semantic similarity search
- Interactive terminal-based chatbot
- Compare different chunking strategies
- Demonstrate Query Expansion techniques

---

## Technologies Used

- Python
- LangChain
- FAISS
- Hugging Face Sentence Transformers
- PyPDFLoader
- RecursiveCharacterTextSplitter

---

## Project Structure

```
Assignment3/
│
├── documents/
│   ├── paper1.pdf
│   ├── paper2.pdf
│   ├── paper3.pdf
│   ├── paper4.pdf
│   └── paper5.pdf
│
├── faiss_index/
│
├── rag_baseline.py
├── rag_vector_db.py
├── rag_chatbot.py
├── rag_experiment.py
├── query_expansion_demo.py
│
├── requirements.txt
└── README.md
```

---

## System Workflow

```
PDF Documents
      │
      ▼
PyPDFLoader
      │
      ▼
Text Chunking
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
User Question
      │
      ▼
Semantic Retrieval
      │
      ▼
Relevant Context
      │
      ▼
Answer Display
```

---

## Python Files

### rag_baseline.py

Loads PDF documents and splits them into text chunks.

### rag_vector_db.py

Creates embeddings using **all-MiniLM-L6-v2** and stores them inside a FAISS vector database.

### rag_chatbot.py

Loads the FAISS database and retrieves the most relevant document chunks for user questions.

### rag_experiment.py

Compares different chunk sizes and overlap configurations.

### query_expansion_demo.py

Demonstrates query expansion by rewriting user questions into more informative search queries.

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/RAG-System.git
```

Move into the project

```bash
cd RAG-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1 – Create the Vector Database

```bash
python rag_vector_db.py
```

### Step 2 – Run the Chatbot

```bash
python rag_chatbot.py
```

### Step 3 – Run the Experiment

```bash
python rag_experiment.py
```

### Step 4 – Query Expansion Demo

```bash
python query_expansion_demo.py
```

---

## Research Papers Used

The knowledge base consists of publicly available research papers related to Large Language Models, including:

- Retrieval-Augmented Generation (RAG)
- Chain-of-Thought Prompting
- Zero-Shot Reasoning
- ReAct
- AutoGen

---

## Learning Outcomes

This project demonstrates:

- Document preprocessing
- Text chunking
- Embedding generation
- Vector databases
- Semantic search
- Information retrieval
- Retrieval-Augmented Generation (RAG)
- Experimental evaluation of chunking strategies
- Query expansion techniques

---

## Future Improvements

- Integrate Large Language Models (Gemini/OpenAI) for answer generation
- Web-based Streamlit interface
- ChromaDB support
- Hybrid search (BM25 + Vector Search)
- Response citation and source highlighting

---

## Author

**Abhiram Tella**

M.Eng. Artificial Intelligence in Business

SRH University of Applied Sciences

Berlin, Germany

---

## License

This project was developed for academic and educational purposes.
