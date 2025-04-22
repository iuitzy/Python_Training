import os
import chromadb
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_faq():
    with open("data/faqs.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    questions, answers = [], []
    i = 0
    while i < len(lines):
        if lines[i].startswith("Q:"):
            question = lines[i][3:].strip()
            if i + 1 < len(lines) and lines[i + 1].startswith("A:"):
                answer = lines[i + 1][3:].strip()
                questions.append(question)
                answers.append(answer)
                i += 2
            else:
                i += 1  # skip if no corresponding answer
        else:
            i += 1  # skip invalid lines
    return questions, answers

questions, answers = load_faq()

# Ensure that questions and answers are non-empty and aligned
if not questions or not answers or len(questions) != len(answers):
    raise ValueError("FAQ data is malformed or incomplete. Please check data/faqs.txt")

chroma_client = chromadb.PersistentClient(path="embeddings/chromadb")
collection = chroma_client.get_or_create_collection(name="faq")
collection.delete(ids=[str(i) for i in range(len(questions))])

embeddings = model.encode(questions).tolist()
for i, emb in enumerate(embeddings):
    collection.add(ids=[str(i)], embeddings=[emb], metadatas=[{"answer": answers[i]}])

def get_bot_response(query: str) -> str:
    query_embedding = model.encode([query])[0].tolist()
    result = collection.query(query_embeddings=[query_embedding], n_results=1)
    if result and result["metadatas"] and result["metadatas"][0]:
        return result['metadatas'][0][0]['answer']
    return "Sorry, I couldn't find an answer to that."

def get_unique_word_count():
    all_text = " ".join(questions + answers)
    words = all_text.lower().split()
    cleaned_words = [''.join(char for char in word if char.isalnum()) for word in words]
    unique_words = set(cleaned_words)
    unique_words.discard("")  # remove empty string if any
    return len(unique_words), unique_words

count, words = get_unique_word_count()
print(f"Total unique words: {count}")
print(f"Unique words: {sorted(words)}")
