import tempfile
from PIL import Image

# Import os to set API
import os

import streamlit as st
from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()
from langchain.vectorstores import Chroma

from langchain.agents.agent_toolkits import(
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

st.title('🦜🔗 PDF-Chat: Interact with Your PDFs in a Conversational Way')
st.subheader('Load your PDF, ask questions, and receive answers directly from the document.')

st.subheader('Upload Your PDF')
uploaded_file=st.file_uploader('',type=(['pdf',"tsv","csv","txt","tab","xlsx","xls"]))

temp_file_path=os.getcwd()
while uploaded_file is None:
    x=1

if uploaded_file is not None:
    temp_dir=tempfile.TemporaryDirectory()
    temp_file_path=os.path.join(temp_dir.name,uploaded_file.name)
    with open(temp_file_path,'wb')as temp_file:
        temp_file.write(uploaded_file.read())

    st.write('Full path of Uploaded file',temp_file_path)

GOOGLE_API_KEY = os.getenv("KEY")
llm=GoogleGenerativeAI(model='gemini-1.5-pro')
embeddings=GoogleGenerativeAIEmbeddings(google_api_key=GOOGLE_API_KEY)

loader =PyPDFLoader(temp_file_path)
pages=loader.load_and_split()

store=Chroma.from_documents(pages,embeddings,collection_name='Pdf')


vector_store=VectorStoreInfo(
    name='Pdf',
    description='A Pdf file to answer your question',
    vectorstore=store
)

toolkit=VectorStoreToolkit(vectorstore_info=vector_store)

agent_excuster=create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit
)

prompt=st.text_input('Input your prompt here ')

if prompt:
    response=agent_excuster.run(prompt)

    st.write(response)

 
    with st.expander('Document Similarity Search'):

        search = store.similarity_search_with_score(prompt) 
 
        st.write(search[0][0].page_content) 