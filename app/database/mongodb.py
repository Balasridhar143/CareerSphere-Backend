from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings


class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.db = self.client[settings.DATABASE_NAME]

        await self.client.admin.command("ping")

        print("✅ MongoDB Atlas Connected Successfully")

    async def disconnect(self):
        self.client.close()


mongodb = MongoDB()