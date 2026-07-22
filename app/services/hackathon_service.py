from app.database.mongodb import mongodb


async def create_hackathon(hackathon):

    database = mongodb.db

    await database.hackathons.insert_one(
        hackathon.model_dump()
    )

    return {
        "success": True,
        "message": "Hackathon Added Successfully."
    }


async def get_all_hackathons():

    database = mongodb.db

    hackathons = await database.hackathons.find().to_list(100)

    for hackathon in hackathons:
        hackathon["_id"] = str(hackathon["_id"])

    return hackathons