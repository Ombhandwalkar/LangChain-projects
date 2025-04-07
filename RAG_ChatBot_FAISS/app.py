from langchain_community.document_loaders import HuggingFaceDatasetLoader
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv,find_dotenv
from collections.abc import MutableSet,MutableMapping
from transformers import AutoTokenizer,pipeline
import collections
import collections.abc
collections.MutableMapping = collections.abc.MutableMapping
collections.MutableSet = collections.abc.MutableSet

import gradio as gr
import os

# Define the HuggingFace API key
_ = load_dotenv(find_dotenv())
hf_api_key=os.environ['HF_TOKEN']

# Load the dataset from HuggingFace 
loader=HuggingFaceDatasetLoader(path='databricks/databricks-dolly-15k',page_content_column='context',use_auth_token=hf_api_key)
data=loader.load()

# Split the data using RecursiceCharacterTextsplitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=150)
docs=text_splitter.split_documents(data)

# Convert into Embeddings 
embeddings=HuggingFaceBgeEmbeddings(
    model_name='sentence-transformers/all-MiniLM-l6-v2',
    model_kwargs={'device':'cpu'},
    encode_kwargs={'normalize':False}
)

# Set up vector store
db=FAISS.from_documents(docs,embeddings)

# Set up retriver
reteriver=db.as_retriever(search_kwargs={'k':4})

# Load the Tokenizer associated with model
tokenizer=AutoTokenizer.from_pretrained("Intel/dynamic_tinybert",padding=True,truncation=True,max_length=512)


# Define question answering pipeline to the model
question_answer=pipeline(
    'question-answering',
    model='Intel/dynamic_tinybert',
    tokenizer=tokenizer,
    return_tensors='pt'
)

# Generate question
def generate(question):
    docs=reteriver.get_relevant_documents(question)
    #context=docs[0].page_content
    context = " ".join([doc.page_content for doc in docs])
    squared_ex=question_answer(question=question,context=context)
    return squared_ex['answer']


def respond(message,chat_history):
    bot_message=generate(message)
    chat_history.append((message,bot_message))

    return '',chat_history

# Set up Chat interface
with gr.Blocks()as demo:
    chatbot=gr.Chatbot(height=240)
    msg=gr.Textbox(label='Ask ')
    btn=gr.Button('Submit')
    clear=gr.ClearButton(components=[msg,chatbot],value='Clear console')

    btn.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot]) #Press enter to submit

demo.queue().launch()