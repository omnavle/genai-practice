from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


def chatbot(state: MessagesState):
    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }
    
builder = StateGraph(MessagesState)

builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")

memory = InMemorySaver()

graph = builder.compile(
    checkpointer= memory
)

thread_1 = {
    "configurable": {
        "thread_id": "user_1"
    }
}

thread_2 = {
    "configurable": {
        "thread_id": "user_2"
    }
}

result = graph.invoke(
    {
        "messages": [
            HumanMessage(content="My name is Om.")
        ]
    },
    config=thread_1
)

print("User 1:", result["messages"][-1].content)


result = graph.invoke(
    {
        "messages": [
            HumanMessage(content="My name is Rahul.")
        ]
    },
    config=thread_2
)

print("User 2:", result["messages"][-1].content)


result = graph.invoke(
    {
        "messages": [
            HumanMessage(content="What is my name?")
        ]
    },
    config=thread_1
)

print("User 1:", result["messages"][-1].content)


result = graph.invoke(
    {
        "messages": [
            HumanMessage(content="What is my name?")
        ]
    },
    config=thread_2
)

print("User 2:", result["messages"][-1].content)