[**AgentGraph-RAG-SQL-Tavily**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/AgentGraph-RAG-SQL-Tavily)  
QueryBot is an intelligent, conversational SQL assistant powered by Gemini 1.5 Flash, capable of interacting with both structured (SQL) and unstructured (vector) databases. It seamlessly integrates with Gradio, LangChain, LangGraph, and LangSmith, making data exploration effortless and intuitive.

🌟 Highlights
🤖 Natural Language Interface – Ask questions naturally; get precise data from SQL and vector DBs.

🧠 Gemini 1.5 Flash – Central agent managing queries and tool routing.

🗃️ Multi-Database Support – SQL (e.g., Chinook) and Vector DBs for document-based context.

🔍 Tavily Web Search – Real-time info when data isn’t in local sources.

💬 Conversational Memory – Maintains session context.

📊 LangSmith Integration – Logging, debugging, and observability.

🛠️ Gradio Frontend – User-friendly UI for seamless interaction.

---
[**KnowledgeGraph-Q&A-and-RAG-with-TabularData**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/NeoQuery-Tabular_Data) 
An intelligent chatbot powered by LangChain, GEMINI 1.5, and Neo4j, enabling Q&A and Retrieval-Augmented Generation (RAG) over tabular data (CSV, Excel, etc.) through an automatically constructed knowledge graph.

🧠 What It Does
This chatbot allows users to:

🗂 Chat with tabular datasets transformed into a knowledge graph

🔎 Ask complex questions that leverage relationships within the data

🧬 Perform RAG over graph-structured data

🛠️ Generate a knowledge graph from CSV/XLSX files using LLMs + LangChain Graph Transformer

✨ Features
✅ Natural language interface for querying structured data

🧾 Tabular input support: .csv, .xlsx, etc.

🧠 Knowledge graph built from your data (auto-generated or expert-designed)

💬 Cypher query generation and execution via LangChain + GEMINI 1.5

🗃️ Graph database: Neo4j (read-only mode enforced)


---

[**ChatSQL-Bot**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/ChatSQL_Bot)  
SQL Whisperer is a smart assistant that translates plain English into executable SQL queries using Google's Gemini 1.5 Flash, LangChain, and a sleek Streamlit UI. It's built to interact with MySQL databases, enabling effortless querying without needing SQL skills.

🚀 Key Highlights
🧠 Natural Language to SQL using Gemini-1.5-Flash

💬 Interactive Streamlit Chat UI for querying databases

📚 Few-Shot Learning with semantic example matching

📊 Schema Awareness with smart table selection

🔄 Contextual Conversations with history tracking

✅ Readable Output for user-friendly responses

🧱 Architecture Overview
* Gemini AI for understanding natural language queries

* Semantic Few-Shot Examples to guide SQL generation

* Dynamic Table Selection from database schema

* SQL Conversion & Execution on a live MySQL DB

* Formatted Output delivered via Streamlit UI

---

[**Crew-AI**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/Crew-AI) 
1) **ai_latest_developement**
A dynamic agent system that continuously tracks the latest developments in AI.
Leverages web scraping and LLM summarization for real-time trend analysis.
Ideal for staying updated on cutting-edge tools, models, and research.

2) **ai_news**
Aggregates and curates daily AI-related news articles and blog posts.
Uses NLP pipelines to summarize, tag, and classify updates.
Streamlined for fast skimming of high-signal AI headlines.

3) **crewai-hiereachical-antropic**
Implements a hierarchical agent system using Anthropic Claude for structured task delegation.
Tasks are broken into subtasks and distributed across specialized agents.
Optimized for complex workflows requiring planning, reasoning, and execution.

4) **crewai_sequential-ollama2**
Sequential agent architecture powered by Ollama 2 LLMs.
Agents pass context and outputs down a structured pipeline for task resolution.
Efficient for step-wise processes like data analysis, report generation, or multi-stage RAG.

5) **meeting minutes**
Transcribes, summarizes, and organizes meeting recordings into structured minutes.
Supports speaker tagging, action item extraction, and agenda mapping.
Useful for organizations aiming to automate documentation.

6) **pdf rag**
Retrieval-Augmented Generation system built for querying PDFs using natural language.
Parses and embeds documents for semantic search via vector DBs.
Great for turning static PDF reports into interactive knowledge systems.

7) **poem flow**
Creative agent workflow for generating and refining poems or lyrical content.
Includes persona-driven agents (e.g., editor, critic, stylist) for collaborative writing.
Perfect for AI-assisted artistic expression and poetic exploration.

---

[**🔍 Hybrid RAG-Powered PDF Question Answering App**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/Hybrid_Insight_Bot) 
An intelligent PDF QA tool that blends dense + sparse retrieval with Gemini 1.5 Flash to deliver fast, context-aware answers to natural language questions over uploaded PDF documents.

🌟 Quick Highlights
📄 Upload PDF and query it in plain English

🤖 Gemini 1.5 Flash for fast, factual responses

🔍 Hybrid Retrieval (RAG) using:

🧠 Dense: GoogleGenerativeAIEmbeddings

📚 Sparse: BM25Retriever

⚖️ Ensemble: Balanced 50/50 fusion

💻 Streamlit UI for a seamless experience

📦 LangChain Orchestration with modular pipelines

🧱 Architecture at a Glance
PDF Ingestion → PDFPlumberLoader

Chunking → RecursiveCharacterTextSplitter

Retrievers → BM25 + Dense Embeddings

LLM Response → Gemini Flash via LangChain



---

[**RAG Enhanced Chatbot**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/Insight_Bot) 
An AI-powered chatbot that reads uploaded PDFs and answers user questions with context-aware, citation-backed responses. Built with Streamlit, LangChain, and Google Gemini (Generative AI) using Retrieval-Augmented Generation (RAG).

🚀 Key Features
📄 Multi-PDF Upload – Load and analyze multiple documents

📊 Vector Search – Builds a vector store from extracted PDF content

💬 Smart Q&A – Uses Gemini + RAG for precise, contextual answers

📌 Citations Included – Adds filename and page number for each source

🌐 Interactive UI – Clean and intuitive Streamlit interface

---

[**LangChain-Basics**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/LangChain_Basics) 
**LL**Ms: Interface with powerful large language models to generate raw text responses.

**ChatMode**ls: Tailored for multi-turn conversations using chat-style input/output formats.

**Embedding Mode**ls: Convert text into vector representations for similarity search and retrieval tasks.

**Chai**ns: Combine multiple steps (e.g., prompt → model → parser) into a cohesive processing pipeline.

**Chatb**ot: Interactive conversational agent that integrates LangChain modules for dynamic Q&A.

**Document Loaders**: Ingest content from PDFs, web pages, and more into LangChain workflows.
**
Output Parsers**: Transform raw LLM outputs into structured, usable formats (e.g., JSON, lists).

**Prompts**: Define the input format and task instructions to guide LLM behavior effectively.

**Runnables**: Modular, composable units that allow chaining and reuse of logic across pipelines.

**Structured Output**: Enforce schema-based responses from LLMs for reliable downstream use.

---
[**Memory-Bot**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/MemoryBot) 
A smart, Streamlit-based chatbot powered by LangChain, Gemini (1.5 Flash & Pro), and entity-based memory — designed for rich, multi-turn conversations that feel truly human.

🌟 Highlights
🧠 Contextual Memory via ConversationEntityMemory

💬 Multi-turn Chat that remembers people, places, events

📂 Chat Session Management – start fresh or revisit previous conversations

🛠 Model Switching – choose between Gemini 1.5 Flash & Pro

🔍 Memory Viewer – preview internal memory buffers & tracked entities

📥 Downloadable Chat History – export full conversations

⚙️ Streamlit UI – responsive, interactive, and secure

---

[**DocuMind – RAG-Powered QA from Documents**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/RAG_ChatBot_FAISS) 
DocuMind is a lightweight and efficient question-answering system that uses Retrieval-Augmented Generation (RAG) to deliver precise answers from a curated dataset. Built on top of HuggingFace, FAISS, and Gradio, it enables seamless interaction through a modern chat interface and leverages small, fast models like Intel’s dynamic_tinybert for real-time performance.

🚀 Key Features
🔍 RAG-based QA: Retrieves relevant context and answers user queries using compact LLMs.

💬 Interactive Gradio Interface: Clean, intuitive, and easy to use.

⚡ Fast Inference with TinyBERT: Low-latency responses powered by a lightweight QA model.

📂 Efficient Document Handling: Chunking and embedding of the Dolly-15k dataset for scalable performance.

🧠 FAISS Vector Store: Enables high-speed similarity search across embedded knowledge.

---

[**RLHF**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/RLHF)
**PPO**- Proximal Policy Optimization (PPO) is a reinforcement learning algorithm used to fine-tune language models (LLMs) by maximizing rewards based on human feedback

---
[**MCP**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/MCP) 

---

[**Source Reference Bot**](https://github.com/Ombhandwalkar/LangChain-projects/tree/master/SourceReference_Bot)

---

