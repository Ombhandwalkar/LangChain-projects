import os
import yaml
from pyprojroot import here  # Helps to find root directory of project
from dotenv import load_dotenv
load_dotenv()



with open(here('configs/project_config.yaml'))as cfg:
    app_config= yaml.load(cfg,Loader=yaml.FullLoader)


class LoadProjectConfig:
    def __init__(self) ->None:

        os.environ['LANGHAIN_TRACING_V2']=app_config['langsmith']['tracing']
        os.environ['LANGCHAIN_PROJECT']=app_config['langsmith']['project_name']

        self.memory_dir=here(app_config['memory']['directory'])

