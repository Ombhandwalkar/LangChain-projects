import streamlit  as st
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.retrievers import BM25Retriever
from nltk.tokenize import word_tokenize
from langchain.retrievers import EnsembleRetriever
from dotenv import load_dotenv
load_dotenv()

# Generating prompt to our Model
template="""
        You are an Assistant for Question-Answering task. Use the following pieces of retrived context to answer the question.
        If you don't have any answer,Just say that you don't valid information.
        Use maximum 3 sentence to answer  and keep answer concise.
        context:{context}
        question:{question}
         """
# Definig Directory
pdf_directory=r'B:\Major_Git\LangChain models\Hybrid_RAG\pdf'

# Dening model
model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# Upload file
def upload_pdf(file):
    with open(pdf_directory+file.name,'wb')as f:
        f.write(file.getbuffer())

# Load Pdf
def load_pdf(file_path):
    loader=PDFPlumberLoader(file_path)
    documents=loader.load()
    return documents

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    return text_splitter.split_documents(documents)

# Creating the Embeddings
def build_senamtic_retriever(documents):
    embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store=InMemoryVectorStore(embedding)
    vector_store.add_documents(documents)
    return vector_store.as_retriever()

# Create BM25 retriver.
def build_bm25_retriever(documents):
    return BM25Retriever.from_documents(documents,preprocess_func=word_tokenize)

def answer_question(question,documents):
    context="\n\n".join([doc.page_content for doc in documents])
    prompt=ChatPromptTemplate.from_template(template)
    chain=prompt |model

    response = chain.invoke({'question':question,'context':context})
    return response.content

uploaded_file=st.file_uploader(
    'Upload File',
    type='pdf',
    accept_multiple_files=False
)


if uploaded_file:
    upload_pdf(uploaded_file)
    documents=load_pdf(pdf_directory+uploaded_file.name)
    chunked_documents=split_text(documents)

    semantic_retriever= build_senamtic_retriever(chunked_documents)
    bm25_retriever=build_bm25_retriever(chunked_documents)
    hybrid_retriever=EnsembleRetriever(
        retrievers=[semantic_retriever,bm25_retriever],
        weights=[0.5,0.5]
    )

    question = st.chat_input()

    if question:
        st.chat_message("user").write(question)
        related_documents = hybrid_retriever.invoke(question)
        answer = answer_question(question, related_documents)
        st.chat_message("assistant").write(answer)















