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

graph = builder.compile(checkpointer=memory)

config = {
    "configurable": {
        "thread_id": "user_1"
    }
}

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break
    
    result = graph.invoke({
        "messages": [
            HumanMessage(content=user_input)
        ]
    }, config=config)
    
    print("AI:", result["messages"][-1].content)
    
    