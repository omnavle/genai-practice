from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

message = HumanMessage(
    content="Explain Generative AI in simple words."
)

response = llm.invoke([message])

print(response.content)