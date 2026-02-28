from motor.motor_asyncio import AsyncIOMotorClient

from src.config import settings


mongo_client: AsyncIOMotorClient | None = None


def connect_mongo() -> None:
    global mongo_client
    if mongo_client is None:
        mongo_client = AsyncIOMotorClient(settings.mongodb_url)


def close_mongo() -> None:
    global mongo_client
    if mongo_client is not None:
        mongo_client.close()
        mongo_client = None


def get_logs_collection():
    if mongo_client is None:
        connect_mongo()

    db = mongo_client[settings.mongodb_db_name]
    return db[settings.mongodb_collection_name]
