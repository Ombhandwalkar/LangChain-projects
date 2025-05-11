from typing import List,Tuple
from langchain.schema import HumanMessage,SystemMessage
from utils.load_config import LoadConfig
import langchain 
langchain.debug=True

APPCFG=LoadConfig()


class ChatBot:

    @staticmethod
    def respond(chatbot:List,message:str,chatbot_functionality:str)->Tuple:
        if chatbot_functionality=='Q&A with GraphDB (Simple Agent)':
            chain_response=APPCFG.simple_chain.invoke({'query':message})
            response=chain_response['result']

        elif chatbot_functionality=='Q&A with GraphDB (Improved Agent)':
            response=APPCFG.improved_chain.invoke({'question':message})

        elif chatbot_functionality=='RAG with GraphDB':
            embeddings=APPCFG.llm.embeddings.create(input=message,model=APPCFG.embedding_model_name)
            question_embedding = embeddings.data[0].embedding
            search_result = APPCFG.graph.query("""
                with $question_embedding as question_embedding
                CALL db.index.vector.queryNodes(
                    'movie_tagline_embeddings', 
                    $top_k, 
                    question_embedding
                    ) YIELD node AS movie, score
                RETURN movie.title, movie.tagline, score
                """,
                                               params={
                                                   "question_embedding": question_embedding,
                                                   "top_k": APPCFG.top_k
                                               })
            messages = [
                SystemMessage(
                    content=(
                        APPCFG.system_message
                    )
                ),
                HumanMessage(
                    content=f"User question:\n{message}\n\n"+f"Search result:\n{str(search_result)}")
            ]
            response = APPCFG.llm(messages)
            response = response.content

        chatbot.append((message, response))
        return "", chatbot
