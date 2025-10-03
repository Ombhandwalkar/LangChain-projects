# 🚀 LangChain Projects Portfolio

A comprehensive collection of production-ready LangChain applications showcasing advanced RAG architectures, multi-agent systems, knowledge graphs, and conversational AI. Built with cutting-edge LLMs and modern tooling for intelligent information retrieval and natural language interfaces.

---

## 📋 Table of Contents

- [Featured Projects](#-featured-projects)
- [Tech Stack Overview](#-tech-stack-overview)
- [Getting Started](#-getting-started)
- [Project Categories](#-project-categories)
- [Contributing](#-contributing)
- [Contact](#-contact)

---

## 🌟 Featured Projects

### 1. [AgentGraph-RAG-SQL-Tavily](./AgentGraph-RAG-SQL-Tavily) - QueryBot
**Most Advanced Multi-Agent System**

An intelligent, conversational SQL assistant powered by Gemini 1.5 Flash, capable of interacting with both structured (SQL) and unstructured (vector) databases with real-time web search integration.

**Key Technologies:**
- 🧠 **LLM:** Gemini 1.5 Flash
- 🔄 **Orchestration:** LangGraph, LangChain
- 🗃️ **Databases:** SQL (Chinook DB), Vector DB, Tavily Web Search
- 📊 **Observability:** LangSmith
- 💻 **Frontend:** Gradio

**Highlights:**
- Natural language interface for SQL and vector database queries
- Intelligent agent routing between multiple data sources
- Real-time web search fallback via Tavily
- Conversational memory with session context
- Production-grade logging and debugging

---

### 2. [NeoQuery - Knowledge Graph RAG](./NeoQuery-Tabular_Data)
**Advanced Knowledge Graph Construction & Querying**

An intelligent chatbot that transforms tabular data into knowledge graphs, enabling complex relational queries through natural language using Neo4j and LangChain.

**Key Technologies:**
- 🧠 **LLM:** Gemini 1.5
- 🕸️ **Graph DB:** Neo4j
- 🔧 **Framework:** LangChain Graph Transformer
- 📊 **Data:** CSV, Excel support

**Highlights:**
- Automatic knowledge graph generation from tabular data
- Cypher query generation from natural language
- Complex relationship-aware querying
- RAG over graph-structured data
- Read-only mode for safe production deployment

---

### 3. [ChatSQL-Bot - SQL Whisperer](./ChatSQL_Bot)
**Intelligent Natural Language to SQL Translator**

A smart assistant that translates plain English into executable SQL queries using semantic few-shot learning and dynamic schema awareness.

**Key Technologies:**
- 🧠 **LLM:** Gemini 1.5 Flash
- 🗄️ **Database:** MySQL
- 💬 **UI:** Streamlit
- 🎯 **Learning:** Few-Shot with semantic matching

**Highlights:**
- Zero SQL knowledge required for users
- Dynamic table selection from schema
- Contextual conversation tracking
- Semantic example matching for accuracy
- Formatted, human-readable output

---

### 4. [Hybrid_Insight_Bot - Hybrid RAG PDF QA](./Hybrid_Insight_Bot)
**Advanced Retrieval with Dense + Sparse Fusion**

An intelligent PDF QA tool that combines dense and sparse retrieval methods for superior context-aware answers.

**Key Technologies:**
- 🧠 **LLM:** Gemini 1.5 Flash
- 🔍 **Retrieval:** Hybrid (BM25 + Dense Embeddings)
- 📄 **Parsing:** PDFPlumber
- 💻 **UI:** Streamlit
- ⚙️ **Embeddings:** GoogleGenerativeAIEmbeddings

**Highlights:**
- 50/50 ensemble retrieval (BM25 + Dense)
- Fast, factual responses with context
- Modular LangChain pipeline
- Recursive text chunking for optimal retrieval

---

### 5. [MemoryBot - Entity-Aware Conversational AI](./MemoryBot)
**Smart Chatbot with Persistent Entity Memory**

A conversational agent that remembers people, places, and events across sessions using entity-based memory tracking.

**Key Technologies:**
- 🧠 **LLM:** Gemini 1.5 Flash & Pro
- 🧩 **Memory:** ConversationEntityMemory
- 💬 **UI:** Streamlit
- 📂 **Session Management:** Multi-conversation support

**Highlights:**
- Entity-based memory tracking
- Model switching (Flash/Pro)
- Chat session management
- Memory buffer visualization
- Downloadable chat history

---

### 6. [Insight_Bot - RAG Enhanced Chatbot](./Insight_Bot)
**Multi-PDF QA with Citations**

An AI-powered chatbot that reads multiple PDFs and provides citation-backed, context-aware answers.

**Key Technologies:**
- 🧠 **LLM:** Google Gemini
- 🔍 **RAG:** LangChain Vector Store
- 📄 **Processing:** Multi-PDF upload
- 💻 **UI:** Streamlit

**Highlights:**
- Multi-document processing
- Source citations with page numbers
- Vector search for semantic retrieval
- Clean, interactive interface

---

### 7. [CrewAI Hierarchical - Anthropic](./crewai-hiereachical-antropic)
**Structured Multi-Agent Task Delegation**

Implements hierarchical agent architecture using Anthropic Claude for complex workflow management.

**Key Technologies:**
- 🧠 **LLM:** Anthropic Claude
- 🤖 **Framework:** CrewAI
- 🎯 **Architecture:** Hierarchical task delegation

**Highlights:**
- Task breakdown into subtasks
- Specialized agent coordination
- Planning and reasoning optimization
- Ideal for complex workflows

---

### 8. [CrewAI Sequential - Ollama 2](./crewai_sequential-ollama2)
**Pipeline-Based Agent Architecture**

Sequential agent system with context passing for step-wise task resolution.

**Key Technologies:**
- 🧠 **LLM:** Ollama 2
- 🤖 **Framework:** CrewAI
- 🔄 **Architecture:** Sequential pipeline

**Highlights:**
- Structured pipeline processing
- Context propagation between agents
- Efficient for data analysis and report generation
- Multi-stage RAG support

---

### 9. [AI Latest Development Tracker](./ai_latest_developement)
**Real-Time AI Trend Analysis**

Dynamic agent system that continuously monitors the latest AI developments using web scraping and LLM summarization.

**Key Technologies:**
- 🔍 **Web Scraping:** Custom scrapers
- 🧠 **Summarization:** LLM-based
- 📊 **Analysis:** Trend identification

**Highlights:**
- Real-time AI development tracking
- Automated trend analysis
- Tool and model monitoring
- Research update aggregation

---

### 10. [Meeting Minutes Generator](./meeting minutes)
**Automated Meeting Documentation**

Transcribes and organizes meeting recordings into structured minutes with speaker tagging and action items.

**Key Technologies:**
- 🎤 **Transcription:** Audio processing
- 🧠 **NLP:** Speaker identification, action extraction
- 📋 **Output:** Structured documentation

**Highlights:**
- Speaker tagging
- Action item extraction
- Agenda mapping
- Automated documentation workflow

---

### 11. [PDF RAG](./pdf rag)
**Document Intelligence System**

Retrieval-Augmented Generation system for querying PDFs with natural language.

**Key Technologies:**
- 🔍 **RAG:** Vector-based retrieval
- 📄 **Processing:** PDF parsing and embedding
- 🗃️ **Storage:** Vector DB

**Highlights:**
- Semantic search over PDFs
- Natural language querying
- Interactive knowledge extraction

---

### 12. [DocuMind - Lightweight RAG QA](./RAG_ChatBot_FAISS)
**Fast, Compact RAG System**

Efficient question-answering system using lightweight models and FAISS for high-speed retrieval.

**Key Technologies:**
- 🧠 **Model:** Intel Dynamic TinyBERT
- 🔍 **Vector Store:** FAISS
- 💬 **UI:** Gradio
- 📚 **Dataset:** Dolly-15k

**Highlights:**
- Low-latency responses
- Compact model deployment
- High-speed similarity search
- Resource-efficient architecture

---

### 13. [Poem Flow - Creative AI Agents](./poem flow)
**Collaborative Writing System**

Creative agent workflow with persona-driven agents for generating and refining poetic content.

**Key Technologies:**
- 🤖 **Multi-Agent:** Editor, Critic, Stylist personas
- ✍️ **Domain:** Creative writing
- 🔄 **Workflow:** Collaborative refinement

**Highlights:**
- AI-assisted artistic expression
- Multi-persona collaboration
- Iterative content refinement

---

### 14. [AI News Aggregator](./ai_news)
**Daily AI News Curation**

Aggregates and curates AI-related news with NLP-based summarization and classification.

**Key Technologies:**
- 📰 **Aggregation:** Multi-source scraping
- 🧠 **NLP:** Summarization and tagging
- 🏷️ **Classification:** Topic categorization

**Highlights:**
- Daily news compilation
- Automatic summarization
- High-signal content filtering

---

### 15. [LangChain Basics](./LangChain_Basics)
**Comprehensive LangChain Fundamentals**

Educational repository covering core LangChain concepts and building blocks.

**Modules Covered:**
- 🤖 LLMs & ChatModels
- 🔗 Chains & Runnables
- 📄 Document Loaders
- 🎯 Prompts & Output Parsers
- 🧠 Embedding Models
- 💬 Chatbot Implementation
- 📊 Structured Output

**Perfect for:** Learning LangChain from scratch

---

### 16. [RLHF - Proximal Policy Optimization](./RLHF)
**Reinforcement Learning from Human Feedback**

Implementation of PPO for fine-tuning language models based on human feedback.

**Key Technologies:**
- 🎯 **Algorithm:** Proximal Policy Optimization (PPO)
- 🔄 **Training:** RLHF pipeline
- 📊 **Optimization:** Reward-based fine-tuning

**Highlights:**
- Human-in-the-loop learning
- LLM fine-tuning methodology
- Reward maximization framework

---

## 🛠️ Tech Stack Overview

### Large Language Models
- Google Gemini 1.5 (Flash & Pro)
- Anthropic Claude
- Ollama 2
- HuggingFace Models (TinyBERT)

### Frameworks & Tools
- **LangChain** - Core orchestration framework
- **LangGraph** - Complex agent workflows
- **LangSmith** - Observability and debugging
- **CrewAI** - Multi-agent systems

### Databases & Storage
- **Vector DBs:** FAISS, Chroma
- **Graph DB:** Neo4j
- **SQL:** MySQL, Chinook DB

### Retrieval & Embeddings
- GoogleGenerativeAIEmbeddings
- BM25Retriever
- Hybrid Search (Dense + Sparse)

### User Interfaces
- Streamlit
- Gradio

### Additional Tools
- Tavily (Web Search)
- PDFPlumber (Document Processing)
- PPO (Reinforcement Learning)

---

## 🚀 Getting Started

### Prerequisites
```bash
python >= 3.8
pip install -r requirements.txt
```

### Environment Setup
Create a `.env` file with necessary API keys:
```
GOOGLE_API_KEY=your_gemini_api_key
ANTHROPIC_API_KEY=your_anthropic_key
LANGSMITH_API_KEY=your_langsmith_key
NEO4J_URI=your_neo4j_uri
NEO4J_USERNAME=your_username
NEO4J_PASSWORD=your_password
```

### Running Projects
Each project directory contains its own README with specific setup instructions. Navigate to the project folder and follow the instructions:

```bash
cd [project-name]
python app.py  # or streamlit run app.py
```

---

## 📂 Project Categories

### 🎯 Advanced RAG Systems
- AgentGraph-RAG-SQL-Tavily
- Hybrid_Insight_Bot
- Insight_Bot
- DocuMind
- PDF RAG

### 🤖 Multi-Agent Systems
- CrewAI Hierarchical (Anthropic)
- CrewAI Sequential (Ollama 2)
- AI Latest Development Tracker

### 🗃️ Database Interfaces
- NeoQuery (Knowledge Graphs)
- ChatSQL-Bot
- AgentGraph-RAG-SQL-Tavily

### 💬 Conversational AI
- MemoryBot
- ChatSQL-Bot
- Insight_Bot

### 🎨 Creative & Specialized
- Poem Flow
- Meeting Minutes Generator
- AI News Aggregator

### 📚 Learning Resources
- LangChain Basics
- RLHF

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

---

## 📧 Contact

**Om Bhandwalkar**
- GitHub: [@Ombhandwalkar](https://github.com/Ombhandwalkar)
- Repository: [LangChain-projects](https://github.com/Ombhandwalkar/LangChain-projects)

---

## 📄 License

This repository is available for educational and reference purposes. Please check individual project directories for specific licensing information.

---

## ⭐ Star History

If you find these projects helpful, consider giving the repository a star! ⭐

---

**Built with ❤️ using LangChain, Google Gemini, and cutting-edge AI technologies**
