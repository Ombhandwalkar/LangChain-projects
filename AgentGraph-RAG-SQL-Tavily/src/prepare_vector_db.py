import os
import yaml
from pyprojroot import here
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

class PrepareVectorDB:
    def __init__(self,doc_dir:str,chunk_size:int,chunk_overlap:int,embedding_model:str,vectordb_dir:str,collection_name:str,force:bool=False)->None:
        self.doc_dir=doc_dir
        self.chunk_size=chunk_size
        self.chunk_overlap=chunk_overlap
        self.embedding_model=embedding_model
        self.vectordb_dir=vectordb_dir
        self.collection_name=collection_name

    def path_maker(self,file_name:str,doc_dir):
        return os.path.join(here(doc_dir),file_name)
    
    def run(self):
        if not os.path.exists(here(self.vectordb_dir)):
            os.makedirs(here(self.vectordb_dir))
            print(f"Directory {self.vectordb_dir} was created")

            file_list=os.listdir(here(self.doc_dir))
            docs=[PyPDFLoader(self.path_maker(fn,self.doc_dir)).load_and_split()for fn in file_list]
            docs_list=[item for sublist in docs for item in sublist]
            # docs_list = []
            # for fn in file_list:
            #     loader = PyPDFLoader(self.path_maker(fn, self.doc_dir))
            #     docs = loader.load_and_split()
            #     docs_list.extend(docs)
            text_splitter=RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=self.chunk_size,chunk_overlap=self.chunk_overlap)
            doc_splits=text_splitter.split_documents(docs_list)

            vectordb=Chroma.from_documents(
                documents= doc_splits,
                collection_name=self.collection_name,
                embedding= GoogleGenerativeAIEmbeddings(model=self.embedding_model),
                persist_directory=str(here(self.vectordb_dir))
            )
            print('Vectordb created and saved')
            print('Number of vectors in vectordb:',vectordb._collection.count(),'\n\n')
        else:
            print(f"Directory '{self.vectordb_dir}' already exists.")



if __name__ == "__main__":
    load_dotenv()
    os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

    with open(here("configs/tools_config.yaml")) as cfg:
        app_config = yaml.load(cfg, Loader=yaml.FullLoader)

    # Uncomment the following configs to run for swiss airline policy document
    chunk_size = app_config["swiss_airline_policy_rag"]["chunk_size"]
    chunk_overlap = app_config["swiss_airline_policy_rag"]["chunk_overlap"]
    embedding_model = app_config["swiss_airline_policy_rag"]["embedding_model"]
    vectordb_dir = app_config["swiss_airline_policy_rag"]["vectordb"]
    collection_name = app_config["swiss_airline_policy_rag"]["collection_name"]
    doc_dir = app_config["swiss_airline_policy_rag"]["unstructured_docs"]

    prepare_db_instance = PrepareVectorDB(
        doc_dir=doc_dir,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        embedding_model=embedding_model,
        vectordb_dir=vectordb_dir,
        collection_name=collection_name,
        force=True)

    prepare_db_instance.run()

    # Uncomment the following configs to run for stories document
    chunk_size = app_config["stories_rag"]["chunk_size"]
    chunk_overlap = app_config["stories_rag"]["chunk_overlap"]
    embedding_model = app_config["stories_rag"]["embedding_model"]
    vectordb_dir = app_config["stories_rag"]["vectordb"]
    collection_name = app_config["stories_rag"]["collection_name"]
    doc_dir = app_config["stories_rag"]["unstructured_docs"]

    prepare_db_instance = PrepareVectorDB(
        doc_dir=doc_dir,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        embedding_model=embedding_model,
        vectordb_dir=vectordb_dir,
        collection_name=collection_name)

    prepare_db_instance.run()


