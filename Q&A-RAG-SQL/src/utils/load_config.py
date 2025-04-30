import os 
import yaml
from pyprojroot import here
from langchain_google_genai import ChatGoogleGenerativeAI
import shutil 
import chromadb
from dotenv import load_dotenv

print('Enviroment variable loaded:',load_dotenv())

class LoadConfig:
    def __init__(self)->None:
        with open(here('configs/app_config.yaml'))as cfg:
            app_config=yaml.load(cfg,Loader=yaml.FullLoader)


    
    def load_directories(self,app_config):
        self.stored_csv_xlsx_directory=here(app_config['directories']['stored_csv_xlsx_directory'])
        self.sqldb_directory=str(here(app_config['directories']['sqldb_directory']))
        self.uploaded_files_sqldb_directory=str(here(app_config['directories']['uploaded_files_sqldb_directory']))
        self.stored_csv_xlsx_sqldb_directory=str(here(app_config['directories']['stored_csv_xlsx_sqldb_directory']))
        self.persist_directory=here(app_config['directories']['persist_directory'])

    def load_llm_configs(self, app_config):
        self.model_name = os.getenv("gemini_deployment_name")
        self.agent_llm_system_role = app_config["llm_config"]["agent_llm_system_role"]
        self.rag_llm_system_role = app_config["llm_config"]["rag_llm_system_role"]
        self.temperature = app_config["llm_config"]["temperature"]
        self.embedding_model_name = os.getenv("embed_deployment_name")

    def load_chroma_client(self):
        self.chroma_client = chromadb.PersistentClient(
            path=str(here(self.persist_directory)))
        

    def load_rag_config(self, app_config):
        self.collection_name = app_config["rag_config"]["collection_name"]
        self.top_k = app_config["rag_config"]["top_k"]
        

    def remove_directory(self, directory_path: str):
       
        if os.path.exists(directory_path):
            try:
                shutil.rmtree(directory_path)
                print(
                    f"The directory '{directory_path}' has been successfully removed.")
            except OSError as e:
                print(f"Error: {e}")
        else:
            print(f"The directory '{directory_path}' does not exist.")
