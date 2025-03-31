'''Here We are converting the Scrapped data into plain text --> To store in the Pinecone Database'''
import requests
from bs4 import BeautifulSoup

# This will fetch HTML source code and print it
def get_html_content(url):
    try:
        response=requests.get(url,timeout=5)
        response.raise_for_status() # This will reaise error for bad request
        return response.content
    except requests.exceptions.RequestException as e:
        return f"Error:{e}"
    
# Helps to extract clean text from HTML page by removing scripts and style using BeautifulSoup Library.
def get_plain_text(html_content):
    soup=BeautifulSoup(html_content,'html.parser')
    for script in soup(['script','style']):
        script.extract()
    return soup.get_text()

# Splits a long text into smaller parts.
def split_text_into_chunks(plain_text,max_chars=2000):
    text_chunks=[]      # A list to store the chunks of text
    current_chunks=""   # A string that temporarily holds the current chunk of text.
    for line in plain_text.split('\n'):
        if len(current_chunks) + len(line) + 1 <= max_chars:
            current_chunks += line +' '
        else:
            text_chunks.append(current_chunks.strip())
            current_chunks = line +' '
    if current_chunks:
        text_chunks.append(current_chunks.strip())
    return text_chunks

# This will run above function.
def scrape_text_from_url(url,max_chars=2000):
    html_content=get_html_content(url)
    plain_text=get_plain_text(html_content)
    text_chunks=split_text_into_chunks(plain_text,max_chars)
    return text_chunks