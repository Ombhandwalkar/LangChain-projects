from sentence_transformers import SentenceTransformer  # This library used to create embeddings (Numerical Representation)of Text
import pinecone # This Vector DataBase Client
from pinecone import Pinecone,ServerlessSpec
import os 
import re
import streamlit as st
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

# Initializing the Model and Pinecone
model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

pc= Pinecone(api_key=os.getenv('PINECONE_API_KEY'), environment='us-east-1')
# This is Database name, Which we cerated in Chat-Bot-With-Pinecone.ipynb
# This is index where your text embeddings are stored.
index = pc.Index('langchain-chatbot')

''' This will help to refine users query. It construct a prompt that asks to the language model to generate
More relavent question for knowledge base . This will to search in database more accurate.'''
def query_refiner(conversation,query):
    
    prompt=f"""
    Given the following user query and conversation log, formulate a question that would be the most relevant 
    to provide the user with an answer from a knowledge base.

    CONVERSATION LOG: 
    {conversation}

    Query: {query}

    Refined Query:
    """
    response=model.invoke(prompt)
   
    match = re.search(r"Refined Query:\s*(.*)", response.content, re.IGNORECASE)
    
    if match:
        return match.group(1).strip() 
    
    return response.content.strip()  
    
'''This function finds the most similar text in the Pinecode Index to the user's input'''
def find_match(input):
    input_em=embedding_model.encode(input).tolist()
    result=index.query(vector=input_em,top_k=2,includeMetadata=True)
    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']

'''This function creates a string representation of the conversation history.'''
def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
    return conversation_string




