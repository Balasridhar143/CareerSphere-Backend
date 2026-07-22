from app.database.mongodb import mongodb


async def create_internship(internship):

    database = mongodb.db

    await database.internships.insert_one(
        internship.model_dump()
    )

    return {
        "success": True,
        "message": "Internship Posted Successfully."
    }


async def get_all_internships():

    database = mongodb.db

    internships = await database.internships.find().to_list(100)

    for internship in internships:
        internship["_id"] = str(internship["_id"])

    return internships