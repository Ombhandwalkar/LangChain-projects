# RAG Enhanced Chatbot

This project is a Retrieval-Augmented Generation (RAG) chatbot application built using **Streamlit**, **Google Generative AI (Gemini)**, and **LangChain**. The chatbot can read and understand the content of uploaded PDFs, then answer user questions using the extracted knowledge from the documents.

---

## 🚀 Features

- **📄 PDF Upload:** Supports uploading multiple PDF files.
- **📊 Vector Database Creation:** Extracts text from PDFs and creates a vector database for efficient search.
- **💡 Intelligent Q&A:** Answers user questions using a Retrieval-Augmented Generation (RAG) model.
- **📌 Citations with Metadata:** Automatically adds filename and page number for each answer.
- **🌐 Streamlit UI:** Interactive, user-friendly interface for chat and PDF upload.

---

## ⚡ Technologies Used

- **Streamlit:** Frontend for the chatbot UI.
- **Google Generative AI (Gemini):** Natural language generation.
- **LangChain:** Manages the retrieval-augmented generation process.
- **Google Generative AI API:** For text generation.
- **Databutton:** Manages API keys and secret handling.

---

## 📝 Prerequisites

- **Python 3.8+**
- **Google API Key** with access to Google Generative AI (Gemini).
- A `.env` file containing your API key:
  ```bash
  GOOGLE_API_KEY=your_google_api_key_here
