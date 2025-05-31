from embeddings import embed_text, search_faiss
from openai import OpenAI

def get_answer(query):
    docs = search_faiss(query)
    prompt = f"Use the document below to answer:\n\n{docs}\n\nQuestion: {query}"
    return OpenAI(prompt)