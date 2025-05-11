import os
import streamlit as st
from streamlit.logger import get_logger
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAI
from langchain_community.embeddings import FastEmbedEmbeddings
from dotenv import load_dotenv
load_dotenv()


logger=get_logger('Langchian-chatbot')

def enable_chat_history(func):
    if os.environ.get('GOOGLE_API_KEY'):
        current_page=func.__qualname__
        if 'current_page' not in st.session_state:
            st.session_state['current_page']=current_page
        if st.session_state['current_page'] !=current_page:
            try:
                st.cache_resource.clear()
                del st.session_state['current_page']
                del st.session_state['messages']
            except:
                pass
        
        # To show chat history on session state
        if 'messages' not in st.session_state:
            st.session_state['messages']=[{'role':'assistant','content':'Which information from source documents do you need ?'}]
        for msg in st.session_state['messages']:
            st.chat_message(msg['role']).write(msg['content'])
    
    def execute(*args,**kwargs):
        func(*args,**kwargs)
        return execute
    
def display_message(msg,author):
    st.session_state.append({'role':author,'content':msg})
    st.chat_message(author).write(msg)

def configure_llm():
    llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash')
    return llm

def print_qa(cls,question:str,answer:str):
    log_str="\nUsecase: {}\nQuestion: {}\nAnswer: {}\n" +"-----"*10
    logger.info(log_str.format(cls.__name__,question,answer))


@st.cache_resource
def configure_embedding_model():
    embedding_model=FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    return embedding_model

def sync_st_session():
    for k,v in st.session_state.items():
        st.session_state[k]=v