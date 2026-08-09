from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words."
)

chain = prompt | llm

response = chain.invoke({
    "topic": "Artificial Intelligence"
})

print(response.content)