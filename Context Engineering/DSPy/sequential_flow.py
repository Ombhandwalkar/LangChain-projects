#                                       """We are working on sequential work flow of LM using DSPy"""
import dspy
from print_utils import print
from pydantic import BaseModel, Field
from typing import Optional
dspy.configure(lm=dspy.LM('groq/meta-llama/llama-4-maverick-17b-128e-instruct', api_key=''))


class JokeIdea(BaseModel):
    setup : str
    contradiction: str
    punchline: str 

class QuerytoIdea(dspy.Signature):
    """  
    You are funny comedian and your goal is to generate nice structure for a joke.
    """
    query: str= dspy.InputField()
    joke_idea: JokeIdea= dspy.OutputField()

class IdeatoJoke(dspy.Signature):
    """
    You are funny comedian who likes to tell stories before delivering punchline.
    you are always funny and act on joke input idea.
    """
    joke_idea: JokeIdea= dspy.InputField()
    joke: str= dspy.OutputField(description='Full joke delivery in comedian voice')


class JokeGenerator(dspy.Module):
    def __init__(self):
        self.query_to_idea= dspy.Predict(QuerytoIdea)
        self.idea_to_joke= dspy.Predict(IdeatoJoke)

    def forward(self, query:str):
        joke_idea= self.query_to_idea(query=query)
        print(f"Joke Idea: \n{joke_idea}")

        joke= self.idea_to_joke(joke_idea=joke_idea)
        print(f"Joke: \n{joke}")

        return joke 
    
joke_generator= JokeGenerator()
joke= joke_generator(query='Write a joke about AI in terms of growth')
print(joke.joke)
