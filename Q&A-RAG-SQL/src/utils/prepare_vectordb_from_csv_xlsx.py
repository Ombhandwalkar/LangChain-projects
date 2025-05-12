import os 
import pandas as pd
from utils.load_config import LoadConfig

class PrepareVectorDBFromTabularData:
    """ 

    This class is designed to prepare a vector database from a CSV and XLSX file.
    It then loads the data into a ChromaDB collection. The process involves
    reading the CSV file, generating embeddings for the content, and storing 
    the data in the specified collection.

    """
    def __init__(self,file_directory:str)->None:
        # Initialize the instance with file direcoty and load config file.
        self.APPCFG=LoadConfig()
        self.file_directory=file_directory

    def run_pipeline(self):
        
        