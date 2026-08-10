from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("sample.txt")

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print("Number of chunks:",len(chunks))

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
Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

response = llm.invoke(prompt)

print("\nAnswer:")
print(response.content)