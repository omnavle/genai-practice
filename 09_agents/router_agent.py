from typing import Literal
from typing_extensions import TypedDict

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from langgraph.graph import StateGraph, START, END

load_dotenv()

class State(TypedDict):
    question: str
    category: str
    answer: str


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def router(state: State):
    question = state["question"]
    response = llm.invoke(
         f"""
            Classify the following question into exactly one category:

            python
            math
            general

            Question:
            {question}

            Return ONLY the category name.
            """
    )
    
    category = response.content.strip().lower()
    
    if category not in ["python", "math", "general"]:
        category = "general"

    return {
        "category": category
    }
    
def python_node(state: State):

    response = llm.invoke(
        f"""
You are a Python expert.

Answer this question:
{state["question"]}
"""
    )

    return {
        "answer": response.content
    }
    

def math_node(state: State):

    response = llm.invoke(
        f"""
You are a mathematics expert.

Solve this question:
{state["question"]}
"""
    )

    return {
        "answer": response.content
    }


def general_node(state: State):

    response = llm.invoke(
        f"""
Answer this general question:

{state["question"]}
"""
    )

    return {
        "answer": response.content
    }


def route(
    state: State
) -> Literal["python", "math", "general"]:

    return state["category"]

graph = StateGraph(State)


graph.add_node("router", router)

graph.add_node(
    "python",
    python_node
)

graph.add_node(
    "math",
    math_node
)

graph.add_node(
    "general",
    general_node
)

graph.add_edge(
    START,
    "router"
)


graph.add_conditional_edges(
    "router",
    route,
    {
        "python": "python",
        "math": "math",
        "general": "general"
    }
)


graph.add_edge(
    "python",
    END
)

graph.add_edge(
    "math",
    END
)

graph.add_edge(
    "general",
    END
)

app = graph.compile()

result = app.invoke({
    "question": "What is a Python list?",
    "category": "",
    "answer": ""
})


print("\nCategory:")
print(result["category"])

print("\nAnswer:")
print(result["answer"])