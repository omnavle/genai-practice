from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


class State(TypedDict):
    message: str


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def chatbot(state: State):
    response = llm.invoke(state["message"])

    return {
        "message": response.content
    }
    
def route_question(state: State):
    question = state["message"].lower()
    
    if "python" in question:
        return "python"
    
    return "general"

def python_node(state: State):
    return {
        "message": "Python is a high-level programming language."
    }


def general_node(state: State):
    response = llm.invoke(state["message"])

    return {
        "message": response.content
    }
    
graph = StateGraph(State)

graph.add_node("python", python_node)
graph.add_node("general", general_node)

graph.add_conditional_edges(
    START,
    route_question,
    {
        "python": "python",
        "general": "general"
    }
)

# End nodes
graph.add_edge("python", END)
graph.add_edge("general", END)

# Compile
app = graph.compile()

# Test
result = app.invoke({
    "message": "What is Python?"
})

print(result["message"])