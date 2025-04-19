from typing import List
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
#from langchain_core.pydantic_v1 import  Field
from pydantic.v1 import BaseModel,Field
from langchain.chains.openai_tools import create_extraction_chain_pydantic
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter
from langchain_core.tools import tool
from agent_graph.load_tools_config import LoadToolsConfig

TOOL_CFG=LoadToolsConfig()

class Table(BaseModel):
    name:str=Field(description='Name of the Table in SQL Database')

def get_tables(categories:List[Table])->List[str]:
    tables=[]
    for category in categories:
        if category.name=="Music":
            tables.extend(
                [
                    "Album",
                    "Artist",
                    "Genre",
                    "MediaType",
                    "Playlist",
                    "PlaylistTrack",
                    "Track",
                ]
            )
        elif category.name=='Business':
            tables.extend(
                ["Customer", "Employee", "Invoice", "InvoiceLine"]
            )
    return tables

class ChinookSQLAgent:
    def __init__(self,sqldb_directory:str,llm:str,llm_temperature:float)-> None:
        self.sql_agent_llm=ChatGoogleGenerativeAI(model=llm,temperature=llm_temperature)
        self.db=SQLDatabase.from_uri(f"sqlite:///{sqldb_directory}")
        category_chain_system="""Return names of the SQL tables that are relevent to the user question.\
            Tables are:
                Music
                Business"""
        category_chain=create_extraction_chain_pydantic(Table,self.sql_agent_llm,system_message=category_chain_system)
        table_chain= category_chain | get_tables
        query_chain=create_sql_query_chain(self.sql_agent_llm,self.db)
        table_chain={'input':itemgetter('question')} | table_chain
        self.full_chain=RunnablePassthrough.assign(table_names_to_use=table_chain)|query_chain

    
@tool
def query_chinook_sqldb(query:str)->str:
    """Query the Chinook SQL Database. Input should be a search query."""
    agent=ChinookSQLAgent(
        sqldb_directory=TOOL_CFG.chinbook_sql_directory,
        llm=TOOL_CFG.chinbook_sqlagent_llm,
        llm_temperature=TOOL_CFG.chinbook_sqlagent_llm_temperature
    )
    query=agent.full_chain.invoke({'question':query})
    return agent.db.run(query)