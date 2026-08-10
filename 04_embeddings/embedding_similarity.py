from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# Create embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text1 = "I love programming in Python."
text2 = "Python is my favorite programming language."

# Create embeddings
embedding1 = embedding_model.embed_query(text1)
embedding2 = embedding_model.embed_query(text2)

# Calculate similarity
similarity = cosine_similarity(
    [embedding1],
    [embedding2]
)

print("Similarity:", similarity[0][0])