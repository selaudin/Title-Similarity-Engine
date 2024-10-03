# app/utils.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def find_most_similar_title(reference_title: str, other_titles: list):
    # Get embeddings for reference and other titles
    reference_embedding = model.encode(reference_title)
    other_embeddings = model.encode(other_titles)

    # Measure cosine similarity between the reference and other titles
    distances = cosine_similarity([reference_embedding], other_embeddings)[0]

    # Return the index of the most similar title
    most_similar_idx = distances.argmax()
    return other_titles[most_similar_idx]
