from langgraph.graph import START, END,StateGraph
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.store import sqlite
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core .tools import tool
from dotenv import load_dotenv
import sqlite3
import requests
load_dotenv()


# LLM
llm= ChatGoogleGenerativeAI(model='gemini-1.5-flash')


# Search Tool
search_tool= DuckDuckGoSearchRun(region='us-en')


@tool 
def calculator(first_num:float, second_num:float,operation:float) -> dict:
    """
    Perform simple Artimitic operation on two numbers.
    Valid Operations: add, sub, mul, div
    """
    try:
        if operation == "+":
            result= first_num + second_num
        elif operation=="-":
            ressult= first_num - second_num
        elif operation== "*":
            result= first_num * second_num
        elif operation== "/":
            if second_num== 0:
                return {'error':"Can not divide the value by 0"}
            result= first_num / second_num
        else:
            return {'erro':f"Unsupported operation: {operation}"}
        return {'first_num':first_num, 'second_num':second_num,'result':result,'operation':operation}
    except Exception as e:
        return {'error':str(e)}
    

@tool
def get_stock_price(symbol:str)->dict:
    """
    Fetch latest stock price for given symbol (Ex- AAPL, TSLA)
    Using Alpha vintage with API key in the URL
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=C9PE94QUEW9VWGFM"
    response= requests.get(url)
    return response.json()


tools=[search_tool, calculator, get_stock_price]
llm_with_tools= llm.bind_tools(tools)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages]

# Node

def chat_node(state:ChatState):
    message= state['message']
    response= llm_with_tools.invoke(message)
    return {'message':[response]}

tool_node= ToolNode(tools)


# Checkpointer
conn= sqlite3.connect(database='chatbot.db',check_same_thread=False)
checkpointer= SqliteSaver(conn=conn)


# Graph 
graph= StateGraph(ChatState)
graph.add_node('chat_node',chat_node)
graph.add_node('tools',tool_node)

graph.add_edge(START,'chat_node')

graph.add_conditional_edges('chat_node',tools_condition)
graph.add_edge('tools','chat_node')

chatbot= graph.compile(checkpointer=checkpointer)

#  Helper
def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config["configurable"]["thread_id"])
    return list(all_threads)
