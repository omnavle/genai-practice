from typing import Annotated
from typing_extensions import TypedDict

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode


class State(TypedDict):
    messages: Annotated[list, add_messages]


@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


tools = [
    add,
    subtract,
    multiply
]


tool_node = ToolNode(tools)

graph = StateGraph(State)

graph.add_node("tools", tool_node)

graph.add_edge(START, "tools")
graph.add_edge("tools", END)


app = graph.compile()

result = app.invoke({
    "messages": [
        HumanMessage(
            content="Calculate 10 + 20"
        )
    ]
})

print(result)