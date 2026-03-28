import ollama

def ask_llm(context, question):
    prompt = f"""
You are a strict research assistant.

Rules:
- Use ONLY the context below
- If answer is not in context, say "Not found in the paper"
- Do not guess

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="tinyllama:latest",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]