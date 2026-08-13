import os
from typing import TypedDict

from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq


# Load environment variables
load_dotenv()


# Create Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


# Define state
class CodeState(TypedDict):
    code: str
    review: str


# Review code node
def review_code(state: CodeState):

    code = state["code"]

    prompt = f"""
You are a beginner-friendly code reviewer.

Review the following code:

```python
{code}
"""