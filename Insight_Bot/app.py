import databutton as db
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain.chains import retrieval_qa
import os
from brain import get_index_for_pdf
from dotenv import  load_dotenv
import google.api
load_dotenv()
import google.generativeai as genai

st.title('RAG enchanced Chatbot')


GOOGLE_API_KEY = db.secrets.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

os.environ['GOOGLE_API_KEY']=db.secrets.get('GOOGLE_API_KEY ')
google.api=db.secrets.get('GOOGLE_API_KEY')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat = model.start_chat()



@st.cache_data
def create_vectordb(files,filename):
    with st.spinner('Vector Database'):
        vectordb=get_index_for_pdf(
            [file.getvalue() for file in files],filename,google.api
        )
    return vectordb

# Upload PDF using streamlit's file uploader
pdf_file=st.file_uploader('',type='pdf',accept_multiple_files=True)


# If pdf Files are uploaded, Create vectorDB and store it in session state
if pdf_file:
    pdf_file_name=[file.name for file in pdf_file]
    st.session_state['vectordb']=create_vectordb(pdf_file,pdf_file_name)


# Define the Template for ChatBot App
prompt_template = """
    You are a helpful Assistant who answers to users questions based on multiple contexts given to you.

    Keep your answer short and to the point.
    
    The evidence are the context of the pdf extract with metadata. 
    
    Carefully focus on the metadata specially 'filename' and 'page' whenever answering.
    
    Make sure to add filename and page number at the end of sentence you are citing to.
        
    Reply "Not applicable" if text is irrelevant.
     
    The PDF content is:
    {pdf_extract}
"""

# Get current prompt from session state.
prompt=st.session_state.get('prompt',[{'role':'system','content':'none'}])


# Display the previous chat messages
for message in prompt:
    if message['role'] !='system':
        with st.chat_message(message['role']):
            st.write(message['content'])

# Get users question .
question =st.chat_input('Ask Anything ')


# Handle user's question
if question:
    vectordb=st.session_state.get('vectordb',None)
    if not vectordb:
        with st.message('assistant'):
            st.write('You need to provide PDF first')
            st.stop()
    
    # Search the query in the database.
    search_results=vectordb.similarity_search(question,k=3)

    # Search result
    pdf_extract='\n'.join([result.page_content for result in search_results])

    # Update the prompt with pdf extract
    prompt[0]={
        'role':'system',
        'content':prompt_template.format(pdf_extract=pdf_extract)
    }

    # Add user question and disply answer below it.
    prompt.append({'role':'system','content':question})
    with st.chat_message('user'):
        st.write(question)


    with st.chat_message('assistant'):
        botmsg=st.empty()

    
    response=[]
    result=''
    formatted_prompt = '\n'.join([f"{msg['role']}: {msg['content']}" for msg in prompt])
    response_text = ""
    for chunk in chat.send_message(formatted_prompt, stream=True):
        if chunk.text:
            response_text += chunk.text
            botmsg.write(response_text)

    
    # Add the assistant's response to the prompt
    prompt.append({"role": "assistant", "content": response_text})

    # Store the updated prompt in the session state
    st.session_state["prompt"] = prompt
    prompt.append({"role": "user", "content": result})

    # Store the updated prompt in the session state
    st.session_state["prompt"] = prompt

