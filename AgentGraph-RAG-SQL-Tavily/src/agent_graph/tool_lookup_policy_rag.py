from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_core.tools import tool
from agent_graph.load_tools_config import LoadToolsConfig

TOOL_CFG=LoadToolsConfig()

class SwissAirlinePolicyRAGTool:
    def __init__(self,embedding_model:str,vectordb_dir:str,k:int,collection_name:str) ->None:
        self.embedding_model=embedding_model
        self.vector_dir=vectordb_dir
        self.k=k 
        self.vectordb=Chroma(
            collection_name=collection_name,
            persist_directory=self.vector_dir,
            embedding_function=GoogleGenerativeAIEmbeddings(model=self.embedding_model)
        )
        print(f"Number of vector in vectordb:",self.vectordb._collection.count(),'\n\n')

@tool
def lookup_swiss_airline_policy(query:str)->str:
    """Consult the company policies to check whether certain options are permitted."""
    rag_tool=SwissAirlinePolicyRAGTool(
        embedding_model=TOOL_CFG.policy_rag_embedding_model,
        vectordb_dir=TOOL_CFG.policy_rag_vectordb_directory,
        k=TOOL_CFG.policy_rag_k,
        collection_name=TOOL_CFG.policy_rag_collection_name)
    docs=rag_tool.vectordb.similarity_search(query,k=rag_tool.k)
    return '\n\n'.join([doc.page_content for doc in docs])
        