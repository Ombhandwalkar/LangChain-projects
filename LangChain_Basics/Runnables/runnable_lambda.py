from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableLambda,RunnableParallel,RunnableSequence,RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


prompt1=PromptTemplate(
    template='Write a joke about{topic}',
    input_variables=['topic']
)

def word_count(text):
    return len(text.split())


parser=StrOutputParser()
model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')


joke_chain=RunnableSequence(prompt1 | model | parser)

joke_parallel=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

joke_sequence=RunnableSequence(joke_chain | joke_parallel)


result=joke_sequence.invoke({'topic':'Flower'})


result=" {}\n word count -{}".format(result['joke'],result['word_count'])
print(result)