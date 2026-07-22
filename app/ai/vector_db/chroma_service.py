import chromadb

# Create local Chroma database
client = chromadb.PersistentClient(path="vectordb")

collection = client.get_or_create_collection(
    name="career_data"
)


def add_document(doc_id, text, embedding, metadata):
    """
    Add a job document to ChromaDB.
    """
    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata]
    )


def search_jobs(embedding, top_k=5):
    """
    Search for similar jobs using embedding.
    """
    result = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return result