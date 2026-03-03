from fastapi import APIRouter, Query, status
from src.schemas import ActivityLogCreate, ActivityLogOut
from src.services.activity_logger import log_activity
from src.db.mongo import get_logs_collection

router = APIRouter(prefix="/api/logs", tags=["Activity Logs"])


@router.get("/", response_model=list[ActivityLogOut])
async def get_logs(limit: int = Query(default=50, ge=1, le=200)):
    collection = get_logs_collection()
    cursor = collection.find().sort("timestamp", -1).limit(limit)
    logs = await cursor.to_list(length=limit)

    result: list[ActivityLogOut] = []
    for log in logs:
        result.append(
            ActivityLogOut(
                id=str(log["_id"]),
                action=log["action"],
                entity=log["entity"],
                details=log["details"],
                timestamp=log["timestamp"],
            )
        )
    return result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ActivityLogOut)
async def create_log(payload: ActivityLogCreate):
    await log_activity(payload.action, payload.entity, payload.details)

    collection = get_logs_collection()
    last_log = await collection.find_one(sort=[("_id", -1)])
    return ActivityLogOut(
        id=str(last_log["_id"]),
        action=last_log["action"],
        entity=last_log["entity"],
        details=last_log["details"],
        timestamp=last_log["timestamp"],
    )
