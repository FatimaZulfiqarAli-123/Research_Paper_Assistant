from sentence_transformers import SentenceTransformer
import numpy as np

# load model ONCE
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    embeddings = model.encode(chunks)

    # normalize for cosine similarity
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    return np.array(embeddings, dtype="float32")