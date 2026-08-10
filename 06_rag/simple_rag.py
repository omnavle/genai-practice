from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document(
        page_content="LangChain is a framework used to build applications with large language models."
    ),
    Document(
        page_content="ChromaDB is a vector database used to store and search embeddings."
    ),
    Document(
        page_content="RAG stands for Retrieval Augmented Generation. It allows an LLM to answer questions using external information."
    )
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

question = "What is RAG?"

results = retriever.invoke(question)

context = "\n\n".join(
    document.page_content
    for document in results
)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

response = llm.invoke(prompt)

print("Answer:")
print(response.content)