# 📄 AI Chat with Document Retrieval (RAG)

A Streamlit-based chatbot that answers user queries by referencing information from custom uploaded documents using Retrieval-Augmented Generation (RAG).

---

## 🚀 Project Overview

### What Problem Does It Solve?

Traditional chatbots struggle with domain-specific queries, often lacking access to proprietary or localized documents. This project bridges that gap by integrating a Retrieval-Augmented Generation (RAG) pipeline, enabling the chatbot to:

- Understand and retrieve relevant content from local `.txt` files.
- Provide **context-aware** responses backed by the **original source**.
- Transparently show users where answers are derived from, increasing trust.

### Business Relevance

This application is especially useful for:

- **Internal knowledge bases** (e.g., HR policies, SOPs, legal docs).
- **Customer support** teams needing accurate, contextual responses.
- **Research-heavy industries** where data traceability is critical.

---

## 🧠 Tech Stack & Design Decisions

### 🛠 Tech Stack

- **Python** – Primary language for backend logic.
- **Streamlit** – Quick and interactive frontend UI for web-based chat.
- **LangChain** – Orchestrates LLMs and vector stores seamlessly.
- **ONNX Runtime** – Lightweight, high-performance runtime for the LLM model.
- **DocArrayInMemorySearch** – In-memory vector search to handle document retrieval.
- **OpenAI-compatible LLMs** – For intelligent, conversational output.

### 📐 Design Decisions

- **Recursive Text Splitting**: Documents are chunked into overlapping parts using `RecursiveCharacterTextSplitter` to preserve context during retrieval.
- **Conversational Memory**: Powered by `ConversationBufferMemory`, retaining multi-turn conversations for natural dialogue flow.
- **Document Transparency**: Every response includes a reference popover that shows exact chunks from which the answer was derived.
- **Plug-and-Play**: Easy to update the knowledge base — just drop `.txt` files into the `data/` folder.

---

## ✅ Code Quality & Best Practices

- **Modularization**: Code is organized using classes (`CustomChatBot`) and utility functions (in `lib/utils.py`) for clarity and reusability.
- **Session Management**: Syncs with Streamlit sessions to maintain consistent UI and chat memory.
- **Secure Model Loading**: Embedding and LLM models are loaded safely using custom config handlers.
- **Extensible**: Can easily be adapted for PDF/CSV ingestion or swapped to cloud-based vector stores.
- **Testing Ready**: Clear separation of concerns allows easy unit/integration testing (test framework not shown here but easily integratable).
- **CI/CD Compatible**: Works out-of-the-box with GitHub Actions or Streamlit Community Cloud.

---

## 🧩 Challenges & Learnings

### Challenges

- Maintaining **chat continuity** while dynamically updating vector stores.
- Managing **source traceability** across multiple document chunks.
- Keeping **real-time responsiveness** in a browser-based UI with streaming outputs.

### Learnings

- Mastered LangChain's modular components, especially the `ConversationalRetrievalChain`.
- Gained deeper understanding of prompt engineering for document-contextual QA.
- Learned the balance between **performance** (ONNX runtime) and **accuracy** (retrieval fidelity).

---

## 🧪 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run index.py
