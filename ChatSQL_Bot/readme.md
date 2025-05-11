# SQL Whisperer

SQL Whisperer is a natural language to SQL query converter built with LangChain, Google's Gemini AI, and Streamlit. It allows users to query a MySQL database using plain English questions, which are then translated into SQL queries and executed to retrieve the results.

## Features

- Converts natural language queries to SQL using Google's Gemini-1.5-Flash model
- Interactive chat interface with Streamlit
- Context-aware conversations with chat history
- Few-shot learning with semantic example selection
- Database schema understanding and table selection
- Formatted, human-readable responses

## Architecture

The application consists of several components:

1. **Natural Language Processing**: Uses Google's Gemini AI to understand user queries
2. **Few-Shot Learning**: Utilizes semantic similarity to select relevant examples
3. **Table Selection**: Identifies relevant database tables for the query
4. **SQL Generation**: Converts natural language to SQL queries
5. **Query Execution**: Executes SQL against the database
6. **Response Formatting**: Generates human-readable responses from query results

## Project Structure

```
├── main.py                          # Main Streamlit application entry point
├── langchain_utils.py               # Core LangChain utilities and chain setup
├── examples.py                      # Few-shot learning examples
├── prompts.py                       # Prompt templates
├── table_details.py                 # Database table description handler
├── database_table_descriptions.csv  # Database schema descriptions
├── .env                             # Environment variables (not included in repo)
└── Langchain_NL2SQL.ipynb           # Development notebook
```

## Setup

### Prerequisites

- Python 3.11+
- MySQL database (ClassicModels sample database)
- Google AI API key

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/ombhandwalkar/sql-whisperer.git
   cd sql-whisperer
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your credentials:
   ```
   GOOGLE_API_KEY=your_google_api_key
   db_user=your_mysql_username
   db_password=your_mysql_password
   db_host=localhost:3306
   db_name=classicmodels
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   LANGCHAIN_API_KEY=your_langchain_api_key
   ```

## Usage

1. Start the Streamlit app:
   ```
   streamlit run main.py
   ```

2. Open your browser and navigate to the provided URL (usually http://localhost:8501)

3. Ask questions about your database in natural language:
   - "List all customers in France with a credit limit over 20,000"
   - "Get the highest payment amount made by any customer"
   - "Show product details for products in the 'Motorcycles' product line"
   - "What is the price of 1968 Ford Mustang?"

## Database Schema

The application is configured to work with the ClassicModels sample database, which contains tables for:

- customers
- employees
- offices
- orderdetails
- orders
- payments
- productlines
- products

## Customization

To adapt this application to your own database:

1. Update the database connection details in your `.env` file
2. Create a new CSV file with your database table descriptions
3. Modify the few-shot examples in `examples.py` to match your database schema

## Dependencies

- langchain
- streamlit
- google-generativeai
- langchain-google-genai
- python-dotenv
- pandas
- pymysql



