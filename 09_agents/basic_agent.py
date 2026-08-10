from typing import Annotated
from typing_extensions import TypedDict

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

class State(TypedDict):
    messages: Annotated[list, add_messages]


@tool
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    return f"The weather in {city} is sunny and 28°C."


tools = [get_weather]

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    response = llm_with_tools.invoke(state["messages"])

    return {
        "messages": [response]
    }
    
graph = StateGraph(State)

graph.add_node("chatbot", chatbot)
graph.add_node("tools", ToolNode(tools))

graph.add_edge(START, "chatbot")

graph.add_conditional_edges(
    "chatbot",
    tools_condition
)

graph.add_edge("tools", "chatbot")

app = graph.compile()

response = app.invoke({
    "messages": [
        HumanMessage(
            content="What is the weather in Mumbai?"
        )
    ]
})

print(response["messages"][-1].content)