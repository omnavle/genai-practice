from typing import TypedDict


class State(TypedDict):
    message: str


state = {
    "message": "Hello LangGraph"
}

print(state)
print(state["message"])