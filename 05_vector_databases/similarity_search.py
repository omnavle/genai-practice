from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load Chroma database
vector_store = Chroma(
    collection_name="my_collection",
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)

query = "What is used to build AI applications?"

results = vector_store.similarity_search(
    query,
    k=2
)

for i, document in enumerate(results):
    print(f"\nResult {i + 1}:")
    print(document.page_content)
    print("Metadata:", document.metadata)