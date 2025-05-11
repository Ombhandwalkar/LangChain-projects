# DocuMind

DocuMind is a powerful question-answering system built with Retrieval-Augmented Generation (RAG) technology. It leverages the Databricks Dolly-15k dataset, HuggingFace embeddings, and efficient vector search to provide accurate answers to user queries through an intuitive chat interface.

## Features

- **RAG-based Question Answering**: Combines retrieval of relevant documents with a specialized QA model
- **Interactive Chat Interface**: User-friendly Gradio UI for asking questions
- **Efficient Document Processing**: Intelligent text splitting and embedding generation
- **FAISS Vector Store**: Fast and efficient similarity search for relevant context
- **Lightweight Model**: Uses Intel's dynamic_tinybert for responsive performance

## Architecture

The application follows a modern RAG architecture:

1. **Data Loading**: Loads documents from the Databricks Dolly-15k dataset
2. **Text Processing**: Splits documents into manageable chunks
3. **Embedding Generation**: Creates vector embeddings using HuggingFace models
4. **Vector Storage**: Organizes embeddings in a FAISS vector store
5. **Retrieval**: Finds relevant documents based on user queries
6. **Question Answering**: Uses a specialized model to extract answers from retrieved context
7. **User Interface**: Presents information through a chat interface

## Project Structure

```
├── app.py                    # Main application file with Gradio interface
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables (not tracked in git)
└── README.md                 # Project documentation
```

## Setup

### Prerequisites

- Python 3.8+
- HuggingFace API token
- Internet connection for model downloads

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/ombhandwalkar/documind.git
   cd documind
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your HuggingFace API token:
   ```
   HF_TOKEN=your_huggingface_token
   ```

## Usage

1. Start the application:
   ```
   python app.py
   ```

2. Open the provided URL in your browser (typically http://127.0.0.1:7860)

3. Type your question in the text box and click "Submit" or press Enter

4. The system will retrieve relevant information and generate an answer

## Components


### Embedding Model

- **Model**: sentence-transformers/all-MiniLM-l6-v2
- **Dimensions**: 384
- **Language**: English

### Question Answering Model

- **Model**: Intel/dynamic_tinybert
- **Type**: Extractive QA
- **Features**: Optimized for efficiency and performance

## Customization

To adapt this system to your own dataset:

1. Replace the HuggingFaceDatasetLoader with a different document loader
2. Adjust chunk sizes based on your content
3. Consider fine-tuning the QA model for your specific domain

## Dependencies

- langchain_community
- huggingface_hub
- transformers
- faiss-cpu
- gradio
- python-dotenv

## Performance Considerations

- The Intel/dynamic_tinybert model is optimized for efficiency but may not handle complex reasoning as well as larger models
- FAISS vector similarity search is performed on CPU; for larger document collections, consider GPU acceleration

