from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnablePassthrough,RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()



prompt1=PromptTemplate(
    template='Write joke about- {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='Explain the following joke {text}',
    input_variables=['text']
)

parser=StrOutputParser()
model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')


joke_chain=RunnableSequence(prompt1 | model | parser)


parallel_joke=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(prompt2 | model | parser)
})


final_chain= RunnableSequence(joke_chain | parallel_joke)

print(final_chain.invoke({'topic':'Politics'}))