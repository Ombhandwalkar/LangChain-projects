from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings
from langchain_core.tools import tool
from agent_graph.load_tools_config import LoadToolsConfig

TOOLS_CFG=LoadToolsConfig()



class StoriesRAGTool:
    def __init__(self,embedding_model:str,vectordb_dir:str,k:int,collection_name:str):
        self.embedding_model=embedding_model
        self.k=k
        self.collection_name=collection_name
        self.vectordb=Chroma(
            collection_name=collection_name,
            persist_directory=self.vectordb_dir,
            embedding_function=GoogleGenerativeAIEmbeddings(model=self.embedding_model)
        )
        print('Number of vector in VectorDB',self.vectordb._collection.count(),'\n\n')

@tool
def lookup_stories(query:str)->str:
    """Search among the fictional stories and find the answer to the query. Input should be the query."""
    rag_tool=StoriesRAGTool(
        embedding_model=TOOLS_CFG.stories_rag_embedding_model,
        vectordb_dir=TOOLS_CFG.stories_rag_vectordb_directory,
        k=TOOLS_CFG.stories_rag_k,
        collection_name=TOOLS_CFG.stories_rag_collection_name
    )
    docs=rag_tool.vectordb.similarity_search(query,k=rag_tool.k)
    return '\n\n'.join([doc.page_content for  doc in docs])