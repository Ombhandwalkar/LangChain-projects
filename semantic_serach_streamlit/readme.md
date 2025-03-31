# 🚀 Semantic Search Engine for Documents and Q&A
A **Streamlit-based application** for intelligent question-answering from web documents using **vector search** and **generative AI**.

---

## 🎯 Key Message
> "This project enables users to extract meaningful insights from web content by converting documents into embeddings and performing efficient semantic search with a Generative AI model."

---

## ✅ Answer
By leveraging **sentence-transformers, Pinecone vector database, and generative AI models**, we enable users to **upload URLs, process their content, and ask questions** about the extracted information.

---

## 📌 Supporting Arguments

🔹 **Automated Web Scraping** – Uses **requests** to fetch HTML content and **BeautifulSoup** to extract meaningful text while removing unnecessary scripts and styles.

🔹 **Chunking and Embedding** – Splits extracted text into **chunks** and converts them into embeddings using **sentence-transformers**.

🔹 **Efficient Vector Search** – Stores embeddings in **Pinecone**, enabling **fast and accurate retrieval** of relevant content.

🔹 **Generative AI Integration** – A **large language model (LLM)** generates responses by retrieving relevant embeddings from Pinecone.

🔹 **User-Friendly Streamlit Interface** – Provides two core functionalities:
   - **Ask a Question**: Users can **query** the stored content.
   - **Update a Database**: Users can **upload a URL** for processing.

---

## 📊 Supporting Data or Facts

📌 **Embeddings**: Generated using **sentence-transformers**, stored in **Pinecone** for vector-based retrieval.

📌 **Model**: A **Generative AI LLM** processes relevant chunks to generate answers.

📌 **Application Flow**:
   1. **User Uploads a URL** → System scrapes and processes text.
   2. **Text is Converted into Embeddings** → Stored in **Pinecone**.
   3. **User Asks a Question** → Relevant vectors are retrieved and passed to the **LLM** for an answer.
   4. **Answer is Displayed** on Streamlit.

📌 **Deployment**: Built with **Streamlit**, optimized with **caching** for performance.

---

## ⚡ How to Use?
1️⃣ **Run the Streamlit App**
   ```bash
   streamlit run main.py
   ```
2️⃣ **Choose a Task:**
   - **Upload a URL** → The system will process and store the extracted information.
   - **Ask a Question** → Enter a query to retrieve insights from the stored content.

---

🚀 **Enhance document search with AI-powered insights!** 🔍