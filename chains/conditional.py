from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')

parser=StrOutputParser()

class feedback(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description='Give the sentiment of feedback')

parser2=PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2


prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)


branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt3|model|parser),
    (lambda x:x.sentiment=='negative',prompt3|model|parser),
    RunnableLambda(lambda x: 'could not find the sentiment')
)

chain=classifier_chain|branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

#chain.get_graph().print_ascii()