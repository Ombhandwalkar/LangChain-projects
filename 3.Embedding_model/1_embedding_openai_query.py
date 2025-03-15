from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(modl='text-embedding-3-large',dimensions=32)

result=embedding.embd_query('Delhi is capital of India')
print(str(result))