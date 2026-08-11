from typing import TypedDict
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

from langgraph.graph import StateGraph, START, END

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

class RAGState(TypedDict):
    question: str
    context: str
    answer: str
    
def retrieve(state: RAGState):
    question = state["question"]
    
    documents = retriever.invoke(question)
    
    context = "\n\n".join(
        document.page_content
        for document in documents
    )
    
    return {
        "context": context
    }
    
def generate(state: RAGState):
    question = state["question"]
    context = state["context"]

    prompt = ChatPromptTemplate.from_template(
        """
            You are a helpful AI assistant.

            Answer the question using ONLY the provided context.

            If the answer is not available in the context,
            say: "I don't know based on the provided information."

            Context:
            {context}

            Question:
            {question}

            Answer:
        """
    )
    
    messages = prompt.invoke({
        "context": context,
        "question": question
    })
    
    response = llm.invoke(messages)

    return {
        "answer": response.content
    }
    
    
builder = StateGraph(RAGState)
builder.add_node("retrieve", retrieve)
builder.add_node("generate", generate)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = graph.invoke({
        "question": question,
        "context": "",
        "answer": ""
    })

    print("\nAI:", result["answer"])