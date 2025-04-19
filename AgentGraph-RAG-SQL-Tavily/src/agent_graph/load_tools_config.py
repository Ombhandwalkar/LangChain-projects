import os
import yaml
from pyprojroot import here
from dotenv import load_dotenv
load_dotenv()

class LoadToolsConfig:
    def __init__(self):
        with open(here('configs/tools_config.yaml'))as cfg:
            app_config=yaml.load(cfg,Loader=yaml.FullLoader)

            # Set environment variableS
            os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
            os.environ['TAVILY_API_KEY']=os.getenv('TAVILY_API_KEY')

            # Primary agent
            self.primary_agent_llm=app_config['primary_agent']['llm']
            self.primary_agent_temperature=app_config['primary_agent']['llm_temperature']

            # Internet search config
            self.tavily_search_max_result=int(app_config['tavily_search_api']['tavily_search_max_results'])

            # Swiss Airline Policy RAG config
            self.policy_rag_llm=app_config['swiss_airline_policy_rag']['llm']
            self.policy_rag_llm_temperature=float(app_config['swiss_airline_policy_rag']['llm_temperature'])
            self.policy_rag_embedding_model=app_config['swiss_airline_policy_rag']['embedding_model']
            self.policy_rag_vectordb_directory=str(here(app_config['swiss_airline_policy_rag']['vectordb']))
            self.policy_rag_unstructured_docs_directory=str(here(app_config['swiss_airline_policy_rag']['unstructured_docs']))
            self.policy_rag_k=app_config['swiss_airline_policy_rag']['k']
            self.policy_rag_chunk_size=app_config['swiss_airline_policy_rag']['chunk_size']
            self.policy_rag_chunk_overlap=app_config['swiss_airline_policy_rag']['chunk_overlap']
            self.policy_rag_collection_name=app_config['swiss_airline_policy_rag']['collection_name']

            # Stories RAG config
            self.stories_rag_llm=app_config['stories_rag']['llm']
            self.stories_rag_llm_temperature=float(app_config['stories_rag']['llm_temperature'])
            self.stories_rag_embedding_model=app_config['stories_rag']['embedding_model']
            self.stories_rag_vectordb_directory=str(here(app_config['stories_rag']['vectordb']))
            self.stories_rag_collection_name=app_config['stories_rag']['collection_name']
            self.stories_rag_chunk_size=app_config['stories_rag']['chunk_size']
            self.stories_rag_chunk_overlap=app_config['stories_rag']['chunk_overlap']
            self.stories_rag_k=app_config['stories_rag']['k']

            # Travel SQL agent Config
            self.travel_sqldb_directory=str(here(app_config['travel_sqlagent_config']['travel_sql_dir']))
            self.travel_sqlagent_llm=app_config['travel_sqlagent_config']['llm']
            self.travel_sqlagent_llm_temperature=float(app_config['travel_sqlagent_config']['llm_temperature'])

            # Chingbook SQL agent config
            self.chinbook_sql_directory=str(here(app_config['chinbook_sqlagent_config']['travel_sqldb_dir']))
            self.chinbook_sqlagent_llm=app_config['chinbook_sqlagent_config']['llm']
            self.chinbook_sqlagent_llm_temperature=float(app_config['chinbook_sqlagent_config']['llm_temperature'])

            # Graph Config
            self.thread_id=str(app_config['graph_configs']['thread_id'])