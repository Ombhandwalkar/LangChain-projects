# 🦜🔗 PDF-Chat: Interact with Your PDFs in a Conversational Way

This is a Streamlit-based application that allows you to interact with your PDF documents in a conversational way using Google Generative AI (Gemini) for natural language processing. Simply upload your PDF file, ask questions, and receive answers directly based on the document content.

## 🚀 Features
- **Conversational PDF Interaction:** Upload any PDF document and ask questions. The app will respond with accurate information directly extracted from the document.
- **Document Similarity Search:** The app can also show the most relevant part of the document related to your query.
- **Supports Multiple File Types:** You can upload PDF, TSV, CSV, TXT, TAB, XLSX, and XLS files.
- **Powered by Google Generative AI:** Utilizes the `gemini-1.5-pro` model for natural language understanding.
- **Efficient Vector Storage with Chroma:** For fast and efficient document search.

## 📝 Prerequisites
- Python 3.8 or above
- Streamlit
- Google Generative AI (Gemini) API key
- Chroma for Vector Store
- LangChain library
- dotenv for API key management


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


pip install streamlit langchain langchain-google-genai chromadb python-dotenv PyPDF2

streamlit run app.py
