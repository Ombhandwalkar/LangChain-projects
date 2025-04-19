# File fetch all Parameter from the configs/project_config.yaml
import os
import yaml
from pyprojroot import here
from dotenv import load_dotenv
load_dotenv()


with open(here('configs/project_config.yaml'))as cfg:
    app_config=yaml.load(cfg,Loader=yaml.FullLoader)

# Define a class that loads and sets project configureation settings
class LoadProjectConfig:
    def __init__(self)->None:
        os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
        os.environ['LANGCHAIN_TRACING_V2']=app_config['langsmith']['tracing']
        os.environ['LANGCHAIN_PROJECT']=app_config['langsmith']['project_name']

        self.memory_dir=here(app_config['memory']['directory'])