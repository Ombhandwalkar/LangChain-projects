from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser=StrOutputParser()

url='https://en.wikipedia.org/wiki/C._Sankaran_Nair'
loader=WebBaseLoader(url)

docs=loader.load()



chain = prompt | model | parser

print(chain.invoke({'question':'What was the result of case Jallianwala Bagh ?', 'text':docs[0].page_content}))