import json
from langchain_core.messages import ToolMessage
from typing_extensions import TypedDict
from typing import Annotated,Literal
from langgraph.graph.message import add_messages
from IPython.display import Image,display
from pydantic import BaseModel
# Represents state structure containing list of messages.
class State(TypedDict):
    # Helps to track conversationi flow
    messages: Annotated[list,add_messages]

# A node that runs the tools requested in the last AIMessage.
class BasicToolNode:
    
# Initialize BasicToolNode with available node.
# Takes list of tools and store then in list of dictonary so they can be looked up by name.
    def __init__(self,tools:list)->None:
        self.tools_by_name={tool.name:tool for tool in tools}

# Execute the tool based on tool calls in the last message.
    def __call__(self, inputs:dict):
        # Get the last message from converastion history.
        if messages:=inputs.get('messages',[]):
            message=messages[-1]
        else:
            raise ValueError('No message found in the input')
        outputs=[]
        # Look for any tool_call that AI want to make.
        for tool_call in message.tool_calls:
            # Run the correct tool using the provided arguments.
            tool_result=self.tools_by_name[tool_call['name']].invoke(
                tool_call['args']
            )
            outputs.append(
                # Wrap the result into ToolMessage and return it as part of next step in the conversation.
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call['name'],
                    tool_call_id=tool_call['id']
                )
            )
        return {'message':outputs}
    
# Determine whether to route the ToolNode or end the flow
def route_tools(state:State)-> Literal['tools','__end__']:
    # If AI asked to use a tool, route the process to the BasicToolNode or If not then end the process.
    if isinstance(state,list):
        ai_message=state[-1]
    elif messages :=state.get('messages',[]):
        ai_message=messages[-1]
    else:
        raise ValueError(f"No message found in input state tool_edge : {state}")
    if hasattr(ai_message,'tool_calls') and len(ai_message.tool_calls)>0:
        return 'tools'
    return '__end__'

# Plot the agent schema using graph object, If possible.
def plot_agent_schema(graph):
    try:
        display(Image(graph.get_graph().draw_mermid_png()))
    except Exception:
        return print('Graph could not be displayed')