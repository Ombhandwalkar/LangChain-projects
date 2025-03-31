import google.generativeai as genai
from langchain.schema import AIMessage,HumanMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# Constructs a prompt by combining the provided context with the user's query.
def create_prompt(context,query):
    header="Answer the question truthfully using the provided context. If the context is not enough, say:'Sorry, Not sufficient context to answer query'.\n\n"
    return header + context +"\n\nQuery:"+query

# Using GenAI model to answer the question
def generate_answer(prompt):
    messages=[
        SystemMessage(content='You are an AI assistant that answer queries truthfully using the given context'),
        HumanMessage(content=prompt)
    ]
    response=model(messages)
    return response.content.strip()