from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    template="Give a short explanation of {topic}.",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | llm | parser

response = chain.invoke({
    "topic": "LangChain"
})

print(response)