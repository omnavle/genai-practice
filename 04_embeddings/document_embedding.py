from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "LangChain is used to build AI applications.",
    "Python is a popular programming language.",
    "Machine learning allows computers to learn from data."
]

embeddings = embedding_model.embed_documents(documents)

for i, embedding in enumerate(embeddings):
    print(f"Document {i + 1}")
    print("Embedding length:", len(embedding))
    print("First 5 values:", embedding[:5])
    print()