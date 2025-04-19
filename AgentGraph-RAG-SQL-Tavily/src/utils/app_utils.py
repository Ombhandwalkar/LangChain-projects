import os 
from pyprojroot import here

# Create directory if does not exist
def create_directory(directory_path:str)->None:
    if not os.path.exists(here(directory_path)):
        os.mkdir(here(directory_path))