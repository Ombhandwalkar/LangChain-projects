from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model=GoogleGenerativeAI()

messages=[
    SystemMessage(content='You are helpful Assistent'),
    HumanMessage(content='Tell me about langchain')
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)