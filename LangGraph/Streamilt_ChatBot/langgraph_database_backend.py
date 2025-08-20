from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Literal, Annotated
from pydantic import BaseModel, Field 
from dotenv import load_dotenv
import sqlite3
load_dotenv()

# Creating the LLM
llm= ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# Defining the TypeDict
class StateChat(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# Creating the chat function
def chat_node( state: StateChat):
    messages= state['messages']
    response= llm.invoke(messages)
    return {'messages':[response]}

conn= sqlite3.connect(database='chatbot.db', check_same_thread=False)
checkpointer= SqliteSaver(conn=conn)

# Creating the LangGraph Node
graph= StateGraph(StateChat)

graph.add_node('chat_node',chat_node)

# Creating the Edge
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot= graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads=set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
        return list(all_threads)