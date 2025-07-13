# data/memory_store.py

import os
import numpy as np
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# Load .env if available
load_dotenv()

# Initialize Pinecone v3 client
api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=api_key)

# Ensure index exists (if not, create it)
index_name = "dt-memories"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="gcp", region="us-west1")
    )

# Function to store session memory
def store_context_memory(user_input):
    session_id = user_input['session_context']['user_id']
    
    # Generate a placeholder 1536-dim embedding vector (you can replace with actual embeddings)
    fake_embedding = np.random.rand(1536).tolist()
    
    # Get the index
    index = pc.Index(index_name)
    
    # Store in Pinecone
    index.upsert([
        {
            "id": session_id,
            "values": fake_embedding,
            "metadata": {
                "role": user_input["session_context"]["role"],
                "intent": user_input["session_context"]["intent"]
            }
        }
    ])
