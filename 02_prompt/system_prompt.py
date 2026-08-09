from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

messages = [
    SystemMessage(
        content="You are an expert Python teacher. Explain concepts simply for beginners."
    ),
    HumanMessage(
        content="What is a Python function?"
    )
]

response = llm.invoke(messages)

print(response.content)