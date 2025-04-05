from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()


llm=HuggingFaceEndpoint(
    repo_id='google/gemma-2-2b-it',
    task='text-generation'
)

model=ChatHuggingFace(llm=llm)

template=PromptTemplate(
    template='Write detailed report on {topic}',
    input_variables=['topic']

)

template2=PromptTemplate(
    template='write 5 line summary on following text \n {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain=template | model | parser | template2 | model | parser


result=chain.invoke({'topin':'black hole'})
print(result)