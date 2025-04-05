from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
# We can use 'temperature' parameter. Which controls randomness of language model's output
# It affects how deterministc and creative response are.
# It varies from 0-2 
# We also have 'max_completion_token' which will limit the number of words(tokens) in the output.
model=ChatOpenAI(model='gpt-4',temperature=0.3,max_completion_token=10)

result=model.invoke('What is capital of India')
# This provide answer along with metadata. ex- input token size, output token size.
print(result)
# This will provide only output
print(result.content)