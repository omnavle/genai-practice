from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = "LangChain is a framework for building AI applications."

embedding = embedding_model.embed_query(text)

print("Embedding length:", len(embedding))
print("First 10 values:", embedding[:10])