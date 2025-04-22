import os
import yaml 
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_community.graphs import Neo4jGraph 
from pyprojroot import here
from langchain.chains import GraphCypherQAChain
from utils.improved_chain import PrepareImprovedAgent
from dotenv import load_dotenv
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')


print('Ehviroment variables are loaded',load_dotenv())

class LoadConfig:
    def __init__(self)->None:
        with open(here('configs/app_config.yaml'),'r')as cfg:
            self.app_config=yaml.load(cfg,Loader=yaml.FullLoader)
            
        
        self.top_k= self.app_config['RAG_config']['top_k']
        
        self.load_llm_config()
        self.load_graph_db()
        self.load_gemini()

    def load_llm_config(self):
        self.model_name=self.app_config['llm_config']['model_name']
        self.embedding_model_name=self.app_config['llm_config']['embedding_model_name']
        self.temperature=self.app_config['llm_config']['temperature']
        self.system_message=self.app_config['llm_config']['system_message']

    def load_graph_db(self):
        NEO4J_URI='bolt://localhost:7687'
        NEO4J_USERNAME='neo4j'
        NEO4J_PASSWORD= 'Password'
        NEO4J_DATABASE='neo4j'
        self.graph=Neo4jGraph(url=NEO4J_URI,username=NEO4J_USERNAME,password=NEO4J_PASSWORD,database=NEO4J_DATABASE)

    def load_gemini(self):
        self.llm=ChatGoogleGenerativeAI(
            model=self.model_name,
            temperature=self.temperature
        )
        self.simple_chain=GraphCypherQAChain.from_llm(graph=self.graph,llm=self.llm,verbose=True,allow_dangerous_requests=True)
        imporved_chain_instance=PrepareImprovedAgent(graph=self.graph,llm=self.llm)
        self.improved_chain=imporved_chain_instance.run_pipeline()