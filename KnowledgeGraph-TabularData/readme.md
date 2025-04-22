# KnowledgeGraph-Q&A-and-RAG-with-TabularData

`KnowledgeGraph-Q&A-and-RAG-with-TabularData` is a chatbot project that utilizes <u>knowledge graph</u>, <u>GPT 3.5</u>, <u>Langchain graph agent</u>, and <u>Neo4j</u> graph database and allows users to interact (perform <u>Q&A and RAG</u>) with Tabular databases (CSV, XLSX, etc.) using natural language. This project also demonstrates an approach for cunstructing the knowledge graph from unstructured data by leveraging LLMs.

## Features:
- Chat with a graphDB created from tabular data.
- RAG with a graphDB created from tabular data.

**Key NOTE:** Remember to NOT use a Neo4j with WRITE privileges. Use only READ and limit the scope. Otherwise your user can manupulate the data (e.g ask your chain to delete data). So, make sure that your database connection permissions are always scoped as narrowly as possible for your chain/agent’s needs (This warning applies to both designing the chatbot and constructing the knowledge graph using LLMs).

**Key NOTE:** Knowledge graphs, which form the backbone of the chatbot's data structure, can be built with input from domain experts or through advanced language models like the Langchain 'LLM Graph Transformer'. 

**Key NOTE:** Familiarity with database query languages such as Pandas for Python, SQL, and Cypher can enhance the user's ability to ask more better questions and have a richer interaction with the graph agent.

**Key NOTE:** Keep that in mind tha LLMs are non-diterministic. Therefore, if you use LLMs for constructing the knowledge graph, you might get slightly different results on each execution.


## Main underlying techniques used in this chatbot:
- Knowledge graph construction
- LLM chains and agents
- Cypher query
