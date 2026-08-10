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

results = vector_store.similarity_search(
    "AI applications",
    k=3,
    filter={"topic": "AI"}
)

for i, document in enumerate(results):
    print(f"\nResult {i + 1}:")
    print(document.page_content)
    print("Metadata:", document.metadata)