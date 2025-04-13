from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


prompt1=PromptTemplate(
    template='Generate tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1 | model | parser),
    'linkedin':RunnableSequence(prompt2 | model | parser)
})

result=parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print(result['linkedin'])