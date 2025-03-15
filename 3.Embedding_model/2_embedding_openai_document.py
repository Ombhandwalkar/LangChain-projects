from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embidding-3-large',dimenstions=32)

document=[
    'Delhi is capital of India',
    'Mumbai is capital of Maharashatra',
    'Washington DC is capital of US'
]

result=embedding.embed_documents(document)
print(str(result))