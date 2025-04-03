from gensim.models import Word2Vec
import chromadb
 
# Step 1
 
# Step 1: Read Sentences from a File
def load_sentences_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        # Split sentences into lists of words
        return [line.strip().lower().split() for line in file if line.strip()]
 
# Define a sample corpus
#sentences = [["richard", "spends", "million", "dollars", "on", "a", "private", "jet"]]
sentences = load_sentences_from_file("ipl_cricket.txt")
 
# Train Word2Vec model
model = Word2Vec(sentences, vector_size=5, window=3, min_count=1, workers=4)
 
 
 
#words = ["richard", "spends", "million", "dollars", "private", "jet"]
words = set(word for sentence in sentences for word in sentence)
vectors = {word: model.wv[word].tolist() for word in words}
 
 
 
# Step 2
 
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="word_embeddings")
for word, vector in vectors.items():
    collection.add(ids=[word], embeddings=[vector], metadatas=[{"word": word}])
 
 
#query_word = "dollars"
query_word = "match"
 
query_vector = model.wv[query_word].tolist()
results = collection.query(query_embeddings=[query_vector], n_results=3)
 
for i, (word, score) in enumerate(zip(results["ids"][0], results["distances"][0])):
    print(f"Rank {i+1}: Word '{word}' (Similarity Score: {score:.4f})")