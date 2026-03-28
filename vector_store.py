import faiss
import numpy as np

def create_index(embeddings):
    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)  # INNER PRODUCT = cosine after normalization
    index.add(embeddings)

    return index