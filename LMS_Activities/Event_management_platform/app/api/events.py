from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models, schemas
from app.dependencies import get_db, get_logger
from app.services.activity_logger import ActivityLogger

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("", response_model=schemas.EventOut, status_code=status.HTTP_201_CREATED)
def create_event(
    payload: schemas.EventCreate,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    if payload.trainer_id is not None and not db.get(models.Trainer, payload.trainer_id):
        raise HTTPException(status_code=404, detail="Trainer not found")
    event = models.Event(**payload.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    logger.log_event(actor="system", action="event_created", details={"event_id": event.id})
    return event


@router.get("", response_model=list[schemas.EventOut])
def list_events(db: Session = Depends(get_db)):
    return db.scalars(select(models.Event).order_by(models.Event.id)).all()


@router.put("/{event_id}", response_model=schemas.EventOut)
def update_event(
    event_id: int,
    payload: schemas.EventUpdate,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    event = db.get(models.Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    data = payload.model_dump(exclude_unset=True)
    if "trainer_id" in data and data["trainer_id"] is not None and not db.get(models.Trainer, data["trainer_id"]):
        raise HTTPException(status_code=404, detail="Trainer not found")
    for key, value in data.items():
        setattr(event, key, value)
    db.commit()
    db.refresh(event)
    logger.log_event(actor="system", action="event_updated", details={"event_id": event_id})
    return event


@router.patch("/{event_id}/capacity", response_model=schemas.EventOut)
def update_capacity(
    event_id: int,
    payload: schemas.CapacityUpdate,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    event = db.get(models.Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    event.capacity = payload.capacity
    db.commit()
    db.refresh(event)
    logger.log_event(actor="system", action="event_capacity_updated", details={"event_id": event_id})
    return event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    event = db.get(models.Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(event)
    db.commit()
    logger.log_event(actor="system", action="event_deleted", details={"event_id": event_id})

