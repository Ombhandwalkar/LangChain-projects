from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')


prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()


loader=TextLoader(r'B:\Major_Git\LangChain models\LangChain_Basics\document_loader\cricket.txt',encoding='utf-8')

docs=loader.load()


chain=prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))