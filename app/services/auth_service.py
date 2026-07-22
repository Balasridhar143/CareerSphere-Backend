from app.database.mongodb import mongodb
from app.auth.password import hash_password
from app.models.user import User
from app.auth.password import verify_password
from app.auth.jwt_handler import create_access_token

async def register_student(user: User):
    try:
        database = mongodb.db
        print("✅ Step 1: Database Connected")

        existing = await database.users.find_one(
            {"email": user.email}
        )
        print("✅ Step 2: Checked Existing User")

        if existing:
            return {
                "success": False,
                "message": "Email already registered."
            }

        user.password = hash_password(user.password)
        print("✅ Step 3: Password Hashed")

        await database.users.insert_one(user.model_dump())
        print("✅ Step 4: User Inserted")

        return {
            "success": True,
            "message": "Student Registered Successfully."
        }

    except Exception as e:
        print("❌ ERROR:", e)
        raise
async def login_user(email: str, password: str):

    database = mongodb.db

    user = await database.users.find_one(
        {
            "email": email
        }
    )

    if not user:
        return {
            "success": False,
            "message": "User not found."
        }

    if not verify_password(
        password,
        user["password"]
    ):
        return {
            "success": False,
            "message": "Invalid Password."
        }

    token = create_access_token(
        {
            "email": user["email"],
            "role": user["role"]
        }
    )

    return {
        "success": True,
        "access_token": token,
        "token_type": "bearer"
    }