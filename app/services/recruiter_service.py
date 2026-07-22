from app.database.mongodb import mongodb
from app.auth.password import hash_password, verify_password
from app.auth.jwt_handler import create_access_token


async def register_recruiter(recruiter):
    database = mongodb.db

    existing = await database.recruiters.find_one(
        {"email": recruiter.email}
    )

    if existing:
        return {
            "success": False,
            "message": "Recruiter already exists."
        }

    recruiter.password = hash_password(recruiter.password)

    await database.recruiters.insert_one(
        recruiter.model_dump()
    )

    return {
        "success": True,
        "message": "Recruiter Registered Successfully."
    }


async def login_recruiter(email, password):
    database = mongodb.db

    recruiter = await database.recruiters.find_one(
        {"email": email}
    )

    if not recruiter:
        return {
            "success": False,
            "message": "Recruiter not found."
        }

    if not verify_password(password, recruiter["password"]):
        return {
            "success": False,
            "message": "Incorrect password."
        }

    token = create_access_token(
        {
            "email": recruiter["email"],
            "role": "recruiter"
        }
    )

    return {
        "success": True,
        "access_token": token,
        "token_type": "bearer"
    }