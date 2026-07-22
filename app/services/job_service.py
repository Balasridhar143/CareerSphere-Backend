from app.database.mongodb import mongodb
from app.ai.embeddings.embedding_service import generate_embedding
from app.ai.vector_db.chroma_service import add_document


async def create_job(job):
    database = mongodb.db

    job_data = job.model_dump()

    result = await database.jobs.insert_one(job_data)

    job_text = f"""
Job Title: {job_data['title']}

Company: {job_data['company_name']}

Skills:
{', '.join(job_data['skills'])}

Description:
{job_data['description']}

Location:
{job_data['location']}
"""

    embedding = generate_embedding(job_text)

    metadata = {
        "title": job_data["title"],
        "company": job_data["company_name"],
        "location": job_data["location"],
        "job_type": job_data["job_type"]
    }

    add_document(
        str(result.inserted_id),
        job_text,
        embedding,
        metadata
    )

    return {
        "success": True,
        "message": "Job Posted Successfully."
    }


async def get_all_jobs():
    database = mongodb.db

    jobs = []

    async for job in database.jobs.find():
        job["_id"] = str(job["_id"])
        jobs.append(job)

    return jobs