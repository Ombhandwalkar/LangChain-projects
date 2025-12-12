#                                          """We are making iteration of LM for better refinment response. """
import dspy
from print_utils import print
from typing import Optional
from pydantic import BaseModel, Field
dspy.configure(lm= dspy.LM('groq/meta-llama/llama-4-maverick-17b-128e-instruct', api_key=''))


class JokeIdea(BaseModel):
    setup:str
    contradicion:str
    punchline: str 

class QueryToIdea(dspy.Signature):
    """
    You are a funny comedian and your goal is to generate structure of joke
    """
    query: str= dspy.InputField()
    joke_idea: JokeIdea= dspy.OutputField()

class IdeaToJoke(dspy.Signature):
    """  
    You are funny comdian who like to tell stories before delivering punchline.
    You are always funny and act on input joke.
    """
    joke_idea: str





    