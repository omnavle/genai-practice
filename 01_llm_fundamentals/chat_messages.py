from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="What is Python?"),
    AIMessage(content="Python is a popular programming language."),
    HumanMessage(content="Why is Python useful for AI?")
]

response = llm.invoke(messages)

print(response.content)