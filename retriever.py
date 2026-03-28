import numpy as np

def search(query, model, index, chunks, k=3):
    query_vec = model.encode([query])
    query_vec = np.array(query_vec, dtype="float32")

    distances, indices = index.search(query_vec, k)

    return [chunks[i] for i in indices[0]]