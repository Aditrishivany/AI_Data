from bson.errors import InvalidId
from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.dependencies import get_logger
from app.schemas import FeedbackCreate, LogCreate
from app.services.activity_logger import ActivityLogger

router = APIRouter(prefix="/logs", tags=["Logs"])

COLLECTIONS = {
    "events": "event_logs",
    "activities": "user_activity_logs",
    "feedback": "feedback_comments",
}


def collection_for(name: str) -> str:
    if name not in COLLECTIONS:
        raise HTTPException(status_code=404, detail="Log collection not found")
    return COLLECTIONS[name]


@router.post("/events", status_code=status.HTTP_201_CREATED)
def create_event_log(payload: LogCreate, logger: ActivityLogger = Depends(get_logger)):
    return logger.log_event(payload.actor, payload.action, payload.details) or {"message": "MongoDB unavailable"}


@router.post("/activities", status_code=status.HTTP_201_CREATED)
def create_user_activity_log(payload: LogCreate, logger: ActivityLogger = Depends(get_logger)):
    return logger.log_user_activity(payload.actor, payload.action, payload.details) or {"message": "MongoDB unavailable"}


@router.post("/feedback", status_code=status.HTTP_201_CREATED)
def create_feedback(payload: FeedbackCreate, logger: ActivityLogger = Depends(get_logger)):
    return logger.add_feedback(payload.participant_email, payload.event_id, payload.comment) or {
        "message": "MongoDB unavailable"
    }


@router.get("/events")
def get_event_logs(limit: int = Query(default=100, ge=1, le=500), logger: ActivityLogger = Depends(get_logger)):
    return logger.get_docs("event_logs", limit=limit)


@router.get("/activities")
def get_user_activity_logs(limit: int = Query(default=100, ge=1, le=500), logger: ActivityLogger = Depends(get_logger)):
    return logger.get_docs("user_activity_logs", limit=limit)


@router.get("/feedback")
def get_feedback_logs(limit: int = Query(default=100, ge=1, le=500), logger: ActivityLogger = Depends(get_logger)):
    return logger.get_docs("feedback_comments", limit=limit)


@router.put("/{collection}/{doc_id}")
def update_log_doc(collection: str, doc_id: str, payload: dict, logger: ActivityLogger = Depends(get_logger)):
    try:
        updated = logger.update_doc(collection_for(collection), doc_id, payload)
    except InvalidId as exc:
        raise HTTPException(status_code=400, detail="Invalid document id") from exc
    if not updated:
        raise HTTPException(status_code=404, detail="Document not found or MongoDB unavailable")
    return {"message": "Updated"}


@router.delete("/{collection}/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_log_doc(collection: str, doc_id: str, logger: ActivityLogger = Depends(get_logger)):
    try:
        deleted = logger.delete_doc(collection_for(collection), doc_id)
    except InvalidId as exc:
        raise HTTPException(status_code=400, detail="Invalid document id") from exc
    if not deleted:
        raise HTTPException(status_code=404, detail="Document not found or MongoDB unavailable")
