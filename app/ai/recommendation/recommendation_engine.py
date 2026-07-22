from app.ai.embeddings.embedding_service import generate_embedding
from app.ai.vector_db.chroma_service import search_jobs


def recommend_jobs(resume_text):
    embedding = generate_embedding(resume_text)

    results = search_jobs(embedding)

    recommendations = []

    if results["ids"]:
        for i in range(len(results["ids"][0])):
            recommendations.append({
                "job_id": results["ids"][0][i],
                "score": round((1 - results["distances"][0][i]) * 100, 2),
                "details": results["metadatas"][0][i]
            })

    return recommendations