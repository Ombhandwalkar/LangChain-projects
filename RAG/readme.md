# 🦜🔗 RAG from Scratch & Advanced Agentic RAG

A comprehensive collection of Jupyter notebooks designed to take you from the fundamentals of Retrieval Augmented Generation (RAG) to building advanced, adaptive, and agentic RAG workflows using **LangChain** and **LangGraph**.

## 📚 Overview

This project serves as a progressive course. It begins with the building blocks of indexing and retrieval, moves into optimizing query understanding, and culminates in state-of-the-art agentic architectures like Self-RAG and Corrective RAG (CRAG) that can reason, reflect, and self-correct.

## 🚀 Notebooks

### **1. [Introduction to RAG](01_Introduction_To_RAG.ipynb)**
This notebook establishes the foundational components of a RAG pipeline: Indexing, Retrieval, and Generation. It walks through loading data, creating embeddings, storing them in a vector database, and setting up a basic retrieval chain to answer user questions using specific context.

### **2. [Query Transformation](02_Query_Transformation.ipynb)**
Focuses on "Query Translation" techniques to bridge the gap between human language and what a retriever needs. It implements strategies like **Multi-Query** (generating varied perspectives of a question), **Decomposition** (breaking complex problems into sub-steps), and **Step-Back Prompting** to improve retrieval accuracy.

### **3. [Routing to Datasource](03_Routing_to_Datasource.ipynb)**
Implements logic to dynamically direct user queries to the most appropriate data source. It explores **Logical and Semantic Routing** to decide whether a query should be answered by a Vector Store (for specific domain knowledge) or a Web Search (for general or up-to-date information).

### **4. [Indexing to VectorDB](04_Indexing_to_VectorDB.ipynb)**
Covers advanced indexing strategies designed to handle complex documents and improve context preservation. It introduces **Multi-representation Indexing** (storing summaries while retrieving full text), **Parent Document Retrieval**, and **RAPTOR** (recursive tree summarization) to answer high-level questions better.

### **5. [Retrieval Mechanisms](05_Retrieval_Mechanisms.ipynb)**
Demonstrates how to refine the retrieval process to ensure the Language Model receives only the best data. It implements **Re-ranking** (using Cohere) to re-order retrieved documents by relevance and **Contextual Compression** to remove irrelevant noise from the context before generation.

### **6. [Self-Reflection RAG](06_Self_Reflection_RAG.ipynb)**
Builds a robust system inspired by the **Self-RAG** paper, where the model critiques its own work. It includes a "grader" mechanism that evaluates retrieved documents for relevance and checks the final generated answer for hallucinations, triggering a re-try if quality standards aren't met.

### **7. [Agentic RAG](07_Agentic_Rag.ipynb)**
Moves beyond linear chains to creating an autonomous **Retrieval Agent** using LangGraph. This notebook builds an agent that can decide *when* to retrieve information and *which* tools to use, allowing for dynamic, multi-step reasoning loops rather than a fixed sequence of events.

### **8. [Adaptive RAG Agent](08_Adaptive_Rag_Agent.ipynb)**
Implements the **Adaptive RAG** strategy, which acts as a smart router for query complexity. The agent classifies queries (e.g., factual vs. analytical) and selects the most efficient execution path, chosing between direct answers, vector retrieval, or web search based on the specific need.

### **9. [Corrective RAG Agent](09_Corrective_RAG_Agent.ipynb)**
Constructs a **Corrective RAG (CRAG)** workflow designed to handle retrieval failures gracefully. If the system detects that retrieved documents are irrelevant or low-quality, it automatically falls back to a web search to supplement its knowledge and correct the generation.

### **10. [LLAMA 3 Local RAG](10_LLAMA_3_Rag_Agent_Local.ipynb)**
A practical guide to implementing these advanced agentic patterns fully locally. It utilizes **Llama 3** (via Ollama) and local embeddings (Nomic) to build a private, cost-effective RAG agent that runs entirely on your own hardware without relying on external APIs.

---

## 🛠️ Tech Stack

- **Orchestration:** [LangChain](https://www.langchain.com/), [LangGraph](https://langchain-ai.github.io/langgraph/)
- **LLMs:** Google Gemini (Gemini-1.5-Flash), Llama 3 (via Ollama)
- **Vector Store:** ChromaDB
- **Embeddings:** Google Generative AI Embeddings, Nomic Embeddings
- **Search:** Tavily Search API

## ⚡ Getting Started

1. **Install Dependencies:**
   ```bash
   pip install langchain langchain-google-genai langchain-community tiktoken chromadb langgraph tavily-python