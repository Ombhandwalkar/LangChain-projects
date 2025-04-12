import os 
from crewai import Agent,Task,Crew,Process
# Agent- Represents individual AI persona
# Task - Represents a specific job
# Crew - Brings it all together
# Persona- Define how crew should operate
from decouple import config  # It loads the secret API key
from textwrap import dedent  # It cleans up the multiline string
from langchain_anthropic import ChatAnthropic,ChatAnthropicMessages
#from langchain_community.chat_models import ChatAnthropic
#from dotenv import load_dotenv
#load_dotenv()
#os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY')
#os.environ['ANTHROPIC_API_KEY'] = os.getenv('ANTHROPIC_API_KEY')
from decouple import config
import os

os.environ['ANTHROPIC_API_KEY'] = config('ANTHROPIC_API_KEY')


print('## Welcome to the Startup Ideation crew')
print('-'*50)

# Asking query to user !
var_1=input(dedent((
    f"""
    What is your <var_1> to pass to your crew? \n
    """
))),
var_2=input(dedent((
    f"""
    What is your <var_2> to pass to your crew? \n
    """
))),
var_3=input(dedent((
    f"""
    What is your <var_3> to pass to your crew? \n
    """
)))


# Agent Defination
agent_1=Agent(
    # Defines the Agent job or Title
    role=dedent((
        f"""
        Founder
        """
    )),
    # Gives background about the Agent
    backstory=dedent((
        f"""
        Visionary Entrepreneur
        """
    )),
    # Primary objective or mission of the Agent
    goal=dedent((
        f"""
        Craft and Refine the Business idea.
        """
    )),
    # This settings allows the agent to assign tasks to other agents if needed.
    allow_delegation=True,
    # More descreptive in response
    verbose=True,
    # Agent allowed to upto 3 iteration of task execution
    max_iter=3,
    # Requests per minute
    max_rpm=3,
    # Define LLM
    llm=ChatAnthropic(model='claude-3-opus-20240229', temperature=0.8)
)

agent_2=Agent(
    # Define Agent Job role or title
    role=dedent((
        f"""
        Analyst
        """
    )),
    # Gives the background about Agent
    backstory=dedent(((
        f"""
        Market Researcher
        """
    ))),
    # Primary objective or mission of the agent
    goal=dedent((
        f"""
        Understan market landscape
        """
    )),
    # This method allows the agent to assign tasks to other agents if needed.
    allow_delegation=True,
    # More descreptive in response
    verbose=True,
    # Agent allowed to upto 3 iteration of task execution
    max_iter=3,
    # Request per minute
    max_rpm=3,
    # Define LLM
    llm=ChatAnthropic(model='claude-3-opus-20240229', temperature=0.8)
)

agent_3=Agent(
    # Define the agent role or job title
    role=dedent((
        f"""
        Pitch Decker
        """
    )),
    # Gives background of the Agent
    backstory=dedent((
        f"""
        Investor Storyteller
        """
    )),
    # Primary mission of the agent
    goal=dedent((
        f"""
        Build compelling narratives
        """
    )),
    # This allows the agent to assign taska to other agent if needed.
    allow_delegation=True,
    # More descreptive in response
    verbose=True,
    # Max iteration for task execution
    max_iter=3,
    # Request per time
    max_rpm=3,
    # LLM
    llm=ChatAnthropic(model='claude-3-opus-20240229', temperature=0.8)
)


# Task Defination

# Define a task
task_1=Task(
    # Gives the full instruction or problem statement the agent should work on 
    description=dedent((
        f"""
        Draft a lean business model canves for the idea
        ---
        VARIABLE 1: "{var_1}"
        VARIABLE 2: "{var_2}"
        VARIABLE 3: "{var_3}"
        Add more variables if needed...
        """
    )),
    # This tells the agent what the final result should look like 
    expected_output=dedent((
        f"""
        A detailed description of what the task's completion looks like 
        """
    )),
    # Assigns the task to a specific agent
    agent=agent_1
)
# Define task
task_2=Task(
    # Gives the full instruction of problem statement the agent should work on 
    description=dedent((
        f""" 
        Analyze demand,competition and trends
         ---
        VARIABLE 1: "{var_1}"
        VARIABLE 2: "{var_2}"
        VARIABLE 3: "{var_3}"
        Add more variables if needed...
        """
    )),
    # This tells the agent what the final result should look like 
    expected_output=dedent((
        f""" 
        A detailed description of what the task's completion looks like
        """
    )),
    agent=agent_2,
    context=[task_1]
)

# Define task
task_3=Task(
    # Give the full instrucion of problem statement the agent should work on 
    description=dedent((
        f"""Create a one-pager pitch based on findings
         ---
        VARIABLE 1: "{var_1}"
        VARIABLE 2: "{var_2}"
        VARIABLE 3: "{var_3}"
        Add more variables if needed...
        """
    )),
    # This tells the agent what the final result shoudl look like 
    expected_output=dedent((
        f""" 
        A detailed description of what the task's completion looks like\
        """
    )),
    agent=agent_3,
    context=[task_1,task_2]
)


def main():
    crew=Crew(
        # These are the AI agents you have defined.
        agents=[agent_1,agent_2,agent_3],
        # The to-do-list for your agents
        tasks=[task_1,task_2,task_3],
        # Run will output detailed logs to your terminal while execting
        verbose=True,
        # sets task execution model
        process=Process.hierarchical,
        # Define LLM
        manager_llm=ChatAnthropic(model='claude-3-opus-20240229', temperature=0.8),
        # The output from the run will be saved into the file
        output_log_file='./output.log'
    )
    # This kicks off the entire crew process
    result=crew.kickoff()
    print(dedent(f"""\n\n########################"""))
    print(dedent(f"""## Here is your custom crew run result:"""))
    print(dedent(f"""########################\n"""))
    print(result)

if __name__=="__main__":
    main()