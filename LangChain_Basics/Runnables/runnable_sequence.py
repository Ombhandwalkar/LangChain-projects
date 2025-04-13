from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

# Defining the prompt
prompt1=PromptTemplate(
    template='Write joke about {topic}',
    input_variables=['topic']
)
# Defining the template
model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# This will help us to provide output in string fromat.
parser=StrOutputParser()

prompt2=PromptTemplate(
    template='Explain the following joke -{text}',
    input_variables=['text']
)

chain=RunnableSequence(prompt1 | model | parser | prompt2 | model | parser)

print(chain.invoke({'topic':'AI'}))