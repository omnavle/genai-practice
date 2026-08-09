from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def chatbot(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

builder = StateGraph(MessagesState)

builder.add_node("chatbot", chatbot)

builder.add_edge(START, "chatbot")

memory = InMemorySaver()

graph = builder.compile(checkpointer=memory)

config = {
    "configurable": {
        "thread_id": "conversation-1"
    }
}

while True:
    user_input = input("You: ")

    if user_input.lower in ["exit", "quit"]:
        print("Goodbye!")
        break
    
    response = graph.invoke({
        "messages": [
            HumanMessage(content=user_input)
        ]
    }, config )
    
    print("AI:", response["messages"][-1].content)