from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
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


# Create graph
graph = StateGraph(State)

# Add node
graph.add_node("chatbot", chatbot)

# Add edges
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

# Memory
memory = MemorySaver()

# Compile with checkpointer
app = graph.compile(
    checkpointer=memory
)


# Thread ID
config = {
    "configurable": {
        "thread_id": "user-1"
    }
}


# First message
result = app.invoke(
    {
        "message": "My name is Om."
    },
    config
)

print("AI:", result["message"])


# Second message
result = app.invoke(
    {
        "message": "What is my name?"
    },
    config
)

print("AI:", result["message"])