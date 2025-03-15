from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human',' Explain in simple what is {topic}')

])
prompt=chat_template.invoke({'domain':'cricket','topic':'Leg-by'})
print(prompt)