from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = PromptTemplate(
    template="""
    Give information about the following person.

    Return the answer in JSON format with these keys:
    name
    age
    profession

    Person: {person}
    """,
    input_variables=["person"]
)

parser = JsonOutputParser()

chain = prompt | llm | parser

response = chain.invoke({
    "person": "Elon Musk"
})

print(response)