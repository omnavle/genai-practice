from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    collection_name="my_collection",
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)

documents = [
    Document(
        page_content="Python is a popular programming language.",
        metadata={"topic": "programming", "level": "beginner"}
    ),
    Document(
        page_content="LangChain is used to build applications with large language models.",
        metadata={"topic": "AI", "level": "beginner"}
    ),
    Document(
        page_content="ChromaDB is a vector database used to store embeddings.",
        metadata={"topic": "database", "level": "beginner"}
    ),
]

vector_store.add_documents(documents)

print("Documents added successfully!")