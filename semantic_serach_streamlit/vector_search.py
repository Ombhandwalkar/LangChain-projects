import pinecone
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

pc = pinecone.Pinecone(api_key='PINECONE_API_KEY')
index_name = 'semantic-search'

# Access the list of index names from the IndexList object.
index_list = pc.list_indexes().names

if index_name not in index_list:
    print(f"Index '{index_name}' does not exist. Please create it in Pinecone first.")
    exit()

index = pc.Index(index_name)

def addData(corpusData, url):
    id = index.describe_index_stats()['total_vector_count']
    for i in range(len(corpusData)):
        chunk = corpusData[i]
        chunkInfo = (str(id + i),
                     model.encode(chunk).tolist(),
                     {'title': url, 'context': chunk})
        index.upsert(vectors=[chunkInfo])

def find_match(query, k):
    query_em = model.encode(query).tolist()
    result = index.query(query_em, top_k=k, includeMetadata=True)

    return [result['matches'][i]['metadata']['title'] for i in range(k)], [result['matches'][i]['metadata']['context'] for i in range(k)]