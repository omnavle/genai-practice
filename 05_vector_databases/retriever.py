from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    collection_name="my_collection",
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

query = "Tell me about vector databases"

documents = retriever.invoke(query)

for i, document in enumerate(documents):
    print(f"\nDocument {i + 1}:")
    print(document.page_content)
    print("Metadata:", document.metadata)