from app.database.mongodb import db
from app.auth.password import hash_password


async def create_user(user):

    user.password = hash_password(user.password)

    await db.users.insert_one(user.dict())

    return {
        "message": "User Registered Successfully"
    }