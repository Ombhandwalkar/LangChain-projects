import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from google import generativeai
from langchain.utils import invoke_chain
from dotenv import load_dotenv
load_dotenv()

st.title('LangChain NL2SQL Chatbot')

if 'google_model' not in st.session_state:
    st.session_state['google_model']='gemini-1.5-flash'

# Initialize the Chat History in Session state
if "messages" not in st.session_state:
    st.session_state.messages=[]

# Display the Previous messages 
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Get user input from Chat Box
if prompt :=st.chat_input('What is up ?'):
    # Store and Display user messages
    st.session_state.messages.append({'role':'user','content':prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

# Generate and Display Assistant's Response
with st.spinner('Generating response...'):
    with st.chat_message('assistant'):
        response=invoke_chain(prompt,st.session_state.messages)
        st.markdown(response)
st.session_state.messages.append({'role':'assistant','content':response})