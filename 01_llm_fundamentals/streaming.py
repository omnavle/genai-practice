from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    streaming=True
)

print("AI: ", end="", flush=True)

for chunk in llm.stream("Explain Generative AI in simple words."):
    print(chunk.content, end="", flush=True)
    
print()