from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()

prompt=ChatPromptTemplate([
    ('system','You are helpful Assistent'),
    ('user','Question :{question}')
])

st.title('Langchain Demo with Mistral')
input_text=st.text_input('Search the topic you want')

llm=Ollama(model='mistral')
perser=StrOutputParser()

chain=prompt|llm|perser

if  input_text:
    st.write(chain.invoke({"question":input_text}))