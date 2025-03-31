import streamlit as st
from io import StringIO
from vector_search import*
import qa
from utils import*

st.header('Semantic Search Engine for Documents and Q&A')
url=False
query=False
options=st.radio(
    'Choose Task',
    ('Ask a Question','Update a Database')
)
if 'Update a Database' in options:
    url=st.text_input('Enter the URL of the document')
if 'Ask a Question' in options:
    query=st.text_input('Enter your Question')

button=st.button('Submit')



if button and (url or query):
    if 'Update the Database' in options:
        with st.spinner("Updating Database..."):
            corpusData = scrape_text_from_url(url)
            addData(corpusData,url)
            st.success("Database Updated")
    if 'Ask a Question' in options:
        with st.spinner("Searching for the answer..."):
            urls,res = find_match(query,2)
            context= "\n\n".join(res)
            st.expander("Context").write(context)
            prompt = qa.create_prompt(context,query)
            answer = qa.generate_answer(prompt)
            st.success("Answer: "+answer)
