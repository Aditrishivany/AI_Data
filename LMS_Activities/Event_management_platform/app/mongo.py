from pymongo import MongoClient
from pymongo.errors import PyMongoError

from app.config import settings


class MongoManager:
    def __init__(self) -> None:
        self._client: MongoClient | None = None
        self._db = None

    def get_db(self):
        if self._db is not None:
            return self._db
        try:
            self._client = MongoClient(settings.mongo_url, serverSelectionTimeoutMS=1200)
            self._client.admin.command("ping")
            self._db = self._client[settings.mongo_db_name]
            return self._db
        except PyMongoError:
            self.close()
            return None

    def close(self) -> None:
        if self._client is not None:
            self._client.close()
        self._client = None
        self._db = None


mongo_manager = MongoManager()

