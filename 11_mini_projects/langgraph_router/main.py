from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    question: str
    category: str
    response: str
    
def router(state: State):
    question = state["question"].lower()
    
    if any(word in question for word in ["python", "java", "code", "programming"]):
        category = "coding"

    elif any(word in question for word in ["weather", "temperature", "rain"]):
        category = "weather"
    
    else:
        category = "general"
    
    return {"category": category}


def coding_node(state: State):
    return {
        "response": "This question is related to programming."
    }
    
def weather_node(state: State):
    return{
        "response": "This question is related to weather."
    }

def general_node(state: State):
    return{
        "response": "This is a general question."
    }
  
def route_question(state: State):
    return state["category"]

graph = StateGraph(State)

graph.add_node("router", router)
graph.add_node("coding", coding_node)
graph.add_node("weather", weather_node)
graph.add_node("general", general_node)

graph.add_edge(START, "router")

graph.add_conditional_edges(
    "router",
    route_question,
    {
        "coding": "coding",
        "weather": "weather",
        "general": "general",
    }
)

graph.add_edge("coding", END)
graph.add_edge("weather", END)
graph.add_edge("general", END)

app = graph.compile()

if __name__ == "__main__":

    question = input("Ask your question: ")

    result = app.invoke({
        "question": question
    })

    print("\nCategory:", result["category"])
    print("Response:", result["response"])