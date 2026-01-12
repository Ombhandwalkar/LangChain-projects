# 🤖 QueryBot: AI-Powered Multi-Database Agent

An intelligent conversational agent built with **Gemini 1.5 Flash**, **LangChain**, **LangGraph**, and **LangSmith** that seamlessly interacts with SQL databases, vector stores, and web search to provide natural language access to your data.

![QueryBot Architecture](Images/flow.png)

## 🌟 Overview

QueryBot is an advanced AI agent that combines the power of retrieval-augmented generation (RAG), SQL query execution, and real-time web search to answer questions from multiple data sources. Built with a modular architecture, it intelligently routes queries to the appropriate tools while maintaining conversation context.

## ✨ Key Features

### 🧠 Intelligent Agent System
- **Primary Agent**: Powered by Gemini 1.5 Flash for natural language understanding
- **Smart Tool Routing**: Automatically selects the right tool based on query context
- **Conversational Memory**: Maintains context across multiple interactions

### 🔧 Multi-Tool Integration
1. **RAG Tools** (Vector Databases)
   - Swiss Airline Policy lookup
   - Story content retrieval
   - Semantic search with ChromaDB

2. **SQL Agent Tools**
   - Chinook Database (Music & Business data)
   - Travel Database (Airline operations)
   - Natural language to SQL query generation

3. **Web Search**
   - Real-time information via Tavily Search API
   - Fallback for questions beyond internal data

### 💬 User Experience
- **Gradio Interface**: Clean, intuitive web UI
- **Persistent Memory**: Chat history saved to CSV files
- **Feedback System**: Like/dislike functionality for responses

### 📊 Observability
- **LangSmith Integration**: Full tracking and debugging
- **Session Logging**: Conversation history with timestamps
- **Tool Usage Monitoring**: Track which tools are called and why

## 🏗️ Architecture

```
User Query (Gradio UI)
    ↓
Primary Agent (Gemini 1.5 Flash)
    ↓
Tool Router
    ├── RAG Tools (Swiss Policy, Stories)
    ├── SQL Agents (Chinook, Travel DB)
    └── Tavily Web Search
    ↓
Response Generation
    ↓
Memory Storage
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Google Gemini API Key
- Tavily API Key
- LangChain/LangSmith API Keys

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/AgentGraph-RAG-SQL-Tavily.git
cd AgentGraph-RAG-SQL-Tavily
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
```

4. **Prepare Vector Databases**
```bash
cd src
python prepare_vector_db.py
```

5. **Launch the application**
```bash
python app.py
```

The Gradio interface will open at `http://localhost:7860`

## 📁 Project Structure

```
AgentGraph-RAG-SQL-Tavily/
├── configs/
│   ├── project_config.yaml      # LangSmith & memory settings
│   └── tools_config.yaml        # Tool configurations
├── data/
│   ├── airline_policy_vectordb/ # Swiss Airline policy vectors
│   ├── stories_vector_db/       # Story content vectors
│   ├── travel.sqlite            # Travel database
│   └── Chinbook.db              # Music/Business database
├── memory/                      # Chat history CSV files
├── src/
│   ├── agent_graph/
│   │   ├── agent_backend.py     # Core agent logic
│   │   ├── build_full_graph.py  # Agent graph construction
│   │   ├── tool_*.py            # Individual tool implementations
│   │   └── load_tools_config.py # Configuration loader
│   ├── chatbot/
│   │   ├── chatbot_backend.py   # Chat processing
│   │   ├── memory.py            # Memory management
│   │   └── load_config.py       # Project config loader
│   ├── utils/
│   │   ├── app_utils.py         # Utility functions
│   │   └── ui_settings.py       # UI configurations
│   ├── app.py                   # Main Gradio application
│   └── prepare_vector_db.py     # Vector DB preparation script
└── requirements.txt
```

## 🛠️ Configuration

### Tools Configuration (`configs/tools_config.yaml`)

```yaml
primary_agent:
  llm: gemini-1.5-flash
  llm_temperature: 0.0

swiss_airline_policy_rag:
  vectordb: "data/airline_policy_vectordb"
  embedding_model: models/embedding-001
  k: 2  # Number of documents to retrieve

# ... other tool configurations
```

### Project Configuration (`configs/project_config.yaml`)

```yaml
langsmith:
  tracing: "true"
  project_name: "Rag & SQL Agent"

memory:
  directory: memory
```

## 💡 Usage Examples

### Query Swiss Airline Policy
```
User: "What is the cancellation rule for a flight ticket?"
Bot: [Retrieves from Swiss Airline Policy RAG]
```

### Query Music Database
```
User: "List the total sales per country. Which country spent the most?"
Bot: [Executes SQL query on Chinook DB]
```

### Story Retrieval
```
User: "In the stories, who is Fred?"
Bot: [Searches story vector database]
```

### Web Search
```
User: "Give me the link to Trump and Harris debate on YouTube"
Bot: [Uses Tavily Search for real-time results]
```

## 🔍 Key Components

### Agent Backend
- **State Management**: Tracks conversation flow with typed dictionaries
- **Tool Node**: Executes tool calls and returns formatted results
- **Routing Logic**: Conditionally routes to tools or ends conversation

### Memory System
- Stores conversations in daily CSV files
- Includes thread ID, timestamp, query, and response
- Enables context-aware responses

### RAG Tools
- Uses ChromaDB for vector storage
- Google Generative AI embeddings
- Configurable chunk size and overlap
- Similarity search with top-k retrieval

### SQL Agents
- Natural language to SQL translation
- Table categorization for efficient queries
- Query execution and result formatting
- Support for multiple databases

## 📊 Monitoring with LangSmith

All agent interactions are tracked in LangSmith, providing:
- Full conversation traces
- Tool call sequences
- Performance metrics
- Debugging capabilities

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Google Gemini** for the powerful LLM
- **LangChain** & **LangGraph** for agent orchestration
- **Tavily** for real-time web search
- **ChromaDB** for vector storage
- **Gradio** for the intuitive UI

## 📧 Contact

For questions or feedback, please open an issue or reach out via LinkedIn.

