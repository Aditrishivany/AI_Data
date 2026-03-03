from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import models, schemas
from app.dependencies import get_db, get_logger
from app.services.activity_logger import ActivityLogger

router = APIRouter(prefix="/trainers", tags=["Trainers"])


@router.post("", response_model=schemas.TrainerOut, status_code=status.HTTP_201_CREATED)
def create_trainer(
    payload: schemas.TrainerCreate,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    trainer = models.Trainer(**payload.model_dump())
    db.add(trainer)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="Trainer email already exists") from exc
    db.refresh(trainer)
    logger.log_user_activity(actor=trainer.email, action="trainer_created", details={"id": trainer.id})
    return trainer


@router.get("", response_model=list[schemas.TrainerOut])
def list_trainers(db: Session = Depends(get_db)):
    return db.scalars(select(models.Trainer).order_by(models.Trainer.id)).all()


@router.put("/{trainer_id}", response_model=schemas.TrainerOut)
def update_trainer(
    trainer_id: int,
    payload: schemas.TrainerUpdate,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    trainer = db.get(models.Trainer, trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(trainer, key, value)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="Trainer email already exists") from exc
    db.refresh(trainer)
    logger.log_user_activity(actor=trainer.email, action="trainer_updated", details={"id": trainer.id})
    return trainer


@router.post("/{trainer_id}/assign/{event_id}", response_model=schemas.EventOut)
def assign_trainer_to_event(
    trainer_id: int,
    event_id: int,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    trainer = db.get(models.Trainer, trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    event = db.get(models.Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    event.trainer_id = trainer_id
    db.commit()
    db.refresh(event)
    logger.log_event(
        actor=trainer.email,
        action="trainer_assigned_to_event",
        details={"trainer_id": trainer_id, "event_id": event_id},
    )
    return event


@router.get("/{trainer_id}/sessions", response_model=list[schemas.EventOut])
def view_trainer_sessions(trainer_id: int, db: Session = Depends(get_db)):
    trainer = db.get(models.Trainer, trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return db.scalars(select(models.Event).where(models.Event.trainer_id == trainer_id)).all()

