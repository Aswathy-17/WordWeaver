import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Initialize models
embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Example document corpus for retrieval
documents = [
    "AI is transforming various industries, including healthcare, manufacturing, and finance, by automating repetitive tasks.",
    "Machine learning algorithms have been applied in multiple sectors to improve efficiency and reduce human error.",
    "In healthcare, AI helps doctors diagnose diseases more accurately by analyzing medical images and patient history.",
    "AI-powered systems are transforming education by providing personalized learning experiences."
]

# Create FAISS index
document_embeddings = embedder.encode(documents, convert_to_tensor=True)
index = faiss.IndexFlatL2(document_embeddings.shape[1])
index.add(np.array(document_embeddings))

# Content generation function
def generate_content(query):
    query_embedding = embedder.encode([query], convert_to_tensor=True)
    _, indices = index.search(np.array(query_embedding), 2)
    relevant_docs = [documents[i] for i in indices[0]]
    context = " ".join(relevant_docs) + " Generate content based on this information."

    inputs = tokenizer.encode(context, return_tensors="pt", max_length=1024, truncation=True)
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
