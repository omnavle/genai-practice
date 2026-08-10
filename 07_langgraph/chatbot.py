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

    return{
        "message": response.content
    }
    
graph = StateGraph(State)

graph.add_node("chatbot", chatbot)

graph.add_edge(START, "chatbot")
graph.add_edge("chatbot",END)

app = graph.compile()

result = app.invoke({
    "message": "Hello"
})

print(result["message"])