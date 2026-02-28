from datetime import UTC, datetime

from src.db.mongo import get_logs_collection


async def log_activity(action: str, entity: str, details: str) -> None:
    # Keep logging simple and readable for student projects.
    collection = get_logs_collection()
    await collection.insert_one(
        {
            "action": action,
            "entity": entity,
            "details": details,
            "timestamp": datetime.now(UTC),
        }
    )
