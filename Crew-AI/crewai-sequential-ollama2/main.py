import os
from crewai import Agent,Task,Process,Crew
from textwrap import dedent
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
load_dotenv()
import ollama

# Can create custom model
modelfile = '''
FROM llama2
PARAMETER temperature 0.8
PARAMETER stop Result
SYSTEM ""
'''

#ollama.create(model='crewai-llama2',modelfile=modelfile)
#ollama2=ChatOllama(base_url="http://localhost:11434",model='crewai-llama2')
#ollama2 = ChatOllama(model="ollama/crewai-llama2", base_url="http://localhost:11434")
ollama2 = ChatOllama(
    base_url="http://localhost:11434",
    model="ollama/crewai-llama2"  
)


print('## Welcome to the AI-powered learning assistant for students')
print('-'*50)
var_1=input(dedent((
    f"""
    What is the <var_1> to pass to your crew?\n
    """
)))
var_2=input(dedent((
    f"""
    What is the <var_2> to pass to your crew?\n
    """
)))
var_3=input(dedent((
    f"""
    What is the <var_3> to pass to your crew?\n
    """
)))
print('-'*50)

# Agent Defination
agent_1=Agent(
    role=dedent((
        f"""
        Product Strategist
        """
    )),
    backstory=dedent((
        f"""
        A former ed-tech founder who transitioned from bootstrapping a study-assistant startup to leading product at a YC-backed company
        """
    )),
    goal=dedent((
        f"""
        Analyze the problem of inconsistent online learning, synthesize user needs (specifically for remote software developers), and outline a product strategy that includes key features, user personas, and a unique value proposition.
        """
    )),
    allow_delegation=False,
    verbose=True,
    max_iter=3,
    llm=ollama2
)

agent_2=Agent(
    role=dedent((
       f"""
       AI/Tech Architect
       """ 
    )),
    backstory=dedent((
        f"""
        An ex-researcher from OpenAI Labs who specializes in adaptive learning algorithms and fine-tuning LLMs for educational use cases. After seeing how generic AI tutors fail real learners, they’re committed to building systems that adapt to user behavior dynamically.
        """
        )),
    goal=dedent((
        f"""
        Design the AI stack—how the assistant understands context, delivers content, tracks progress, and uses feedback loops to personalize learning.
        """
        )),
    allow_delegation=False,
    verbose=True,
    max_iter=3,
    llm=ollama2    
)
agent_3=Agent(
    role=dedent((
        f"""
        Growth & Community Specialist
        """
    )),
    backstory=dedent((
        f"""
        A dev-influencer turned community growth strategist who built one of the largest remote dev communities on Discord. They believe in "build in public" and that the best learning tools grow virally through community trust.
        """
    )),
    goal=dedent((
        f"""
        Create a growth playbook focused on remote devs: partnerships with bootcamps, engaging content on Dev.to, Discord-based accountability groups, and referral programs. Prioritize sticky growth channels and user feedback cycles.
         """
    )),
    allow_delegation=False,
    verbose=True,
    max_iter=3,
    llm=ollama2
)



task_1 = Task(
    description=dedent((
        f"""
        A clear, concise statement of what the task entails.
        ---
        VARIABLE 1: "{var_1}"
        VARIABLE 2: "{var_2}"
        VARIABLE 3: "{var_3}"
        Add more variables if needed...
        """)),
    expected_output=dedent((
        f"""
        A detailed description of what the task's completion looks like.
        """)),
  agent=agent_1,
)

task_2 = Task(
    description=dedent((
        f"""
        A clear, concise statement of what the task entails.
        ---
        VARIABLE 1: "{var_1}"
        VARIABLE 2: "{var_2}"
        VARIABLE 3: "{var_3}"
        Add more variables if needed...
        """)),
    expected_output=dedent((
        f"""
        A detailed description of what the task's completion looks like.
        """)),
    agent=agent_2,
    context=[task_1],
)

task_3 = Task(
    description=dedent((
        f"""
        A clear, concise statement of what the task entails.
        ---
        VARIABLE 1: "{var_1}"
        VARIABLE 2: "{var_2}"
        VARIABLE 3: "{var_3}"
        Add more variables if needed...
        """)),
    expected_output=dedent((
        f"""
        A detailed description of what the task's completion looks like.
        """)),
    agent=agent_3,
    context=[task_2],
)


def main():
    crew=Crew(
        agents=[agent_1,agent_2,agent_3],
        tasks=[task_1,task_2,task_3],
        verbose=True,
        process=Process.sequential
    )
    result = crew.kickoff()
    print(dedent(f"""\n\n########################"""))
    print(dedent(f"""## Here is your custom crew run result:"""))
    print(dedent(f"""########################\n"""))
    print(result)

if __name__ == "__main__":
    main()
