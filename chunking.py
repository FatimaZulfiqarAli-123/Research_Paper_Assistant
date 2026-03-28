def chunk_text(text, chunk_size=800, overlap=150):
    import re

    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    chunk = ""

    for sentence in sentences:
        if len(chunk) + len(sentence) < chunk_size:
            chunk += " " + sentence
        else:
            chunks.append(chunk.strip())
            chunk = sentence

    if chunk:
        chunks.append(chunk.strip())

    return chunks