from datetime import datetime, timezone

from bson import ObjectId
from app.mongo import mongo_manager


class ActivityLogger:
    def _insert(self, collection: str, payload: dict) -> dict | None:
        db = mongo_manager.get_db()
        if db is None:
            return None
        doc = {**payload, "timestamp": datetime.now(timezone.utc)}
        result = db[collection].insert_one(doc)
        return {"id": str(result.inserted_id), **payload}

    def log_event(self, actor: str, action: str, details: dict) -> dict | None:
        return self._insert("event_logs", {"actor": actor, "action": action, "details": details})

    def log_user_activity(self, actor: str, action: str, details: dict) -> dict | None:
        return self._insert("user_activity_logs", {"actor": actor, "action": action, "details": details})

    def add_feedback(self, participant_email: str, event_id: int, comment: str) -> dict | None:
        return self._insert(
            "feedback_comments",
            {"participant_email": participant_email, "event_id": event_id, "comment": comment},
        )

    def get_docs(self, collection: str, limit: int = 100) -> list[dict]:
        db = mongo_manager.get_db()
        if db is None:
            return []
        docs = []
        for item in db[collection].find().sort("timestamp", -1).limit(limit):
            item["id"] = str(item.pop("_id"))
            docs.append(item)
        return docs

    def update_doc(self, collection: str, doc_id: str, payload: dict) -> bool:
        db = mongo_manager.get_db()
        if db is None:
            return False
        result = db[collection].update_one({"_id": ObjectId(doc_id)}, {"$set": payload})
        return result.modified_count > 0

    def delete_doc(self, collection: str, doc_id: str) -> bool:
        db = mongo_manager.get_db()
        if db is None:
            return False
        result = db[collection].delete_one({"_id": ObjectId(doc_id)})
        return result.deleted_count > 0
