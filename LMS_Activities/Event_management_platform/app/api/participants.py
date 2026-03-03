from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import models, schemas
from app.dependencies import get_db, get_logger
from app.services.activity_logger import ActivityLogger

router = APIRouter(prefix="/participants", tags=["Participants"])


@router.post("", response_model=schemas.ParticipantOut, status_code=status.HTTP_201_CREATED)
def create_participant(
    payload: schemas.ParticipantCreate,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    participant = models.Participant(**payload.model_dump())
    db.add(participant)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="Participant email already exists") from exc
    db.refresh(participant)
    logger.log_user_activity(actor=payload.email, action="participant_created", details={"id": participant.id})
    return participant


@router.get("", response_model=list[schemas.ParticipantOut])
def list_participants(db: Session = Depends(get_db)):
    return db.scalars(select(models.Participant).order_by(models.Participant.id)).all()


@router.put("/{participant_id}", response_model=schemas.ParticipantOut)
def update_participant(
    participant_id: int,
    payload: schemas.ParticipantUpdate,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    participant = db.get(models.Participant, participant_id)
    if not participant:
        raise HTTPException(status_code=404, detail="Participant not found")

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(participant, key, value)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=400, detail="Participant email already exists") from exc
    db.refresh(participant)
    logger.log_user_activity(actor=str(participant.email), action="participant_updated", details={"id": participant.id})
    return participant


@router.delete("/{participant_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_participant(
    participant_id: int,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    participant = db.get(models.Participant, participant_id)
    if not participant:
        raise HTTPException(status_code=404, detail="Participant not found")
    actor = participant.email
    db.delete(participant)
    db.commit()
    logger.log_user_activity(actor=str(actor), action="participant_deleted", details={"id": participant_id})


@router.post("/{participant_id}/register/{event_id}", response_model=schemas.RegistrationOut, status_code=201)
def register_participant_for_event(
    participant_id: int,
    event_id: int,
    db: Session = Depends(get_db),
    logger: ActivityLogger = Depends(get_logger),
):
    participant = db.get(models.Participant, participant_id)
    if not participant:
        raise HTTPException(status_code=404, detail="Participant not found")

    event = db.get(models.Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    current_count = db.scalar(select(func.count(models.Registration.id)).where(models.Registration.event_id == event_id))
    if current_count >= event.capacity:
        raise HTTPException(status_code=400, detail="Event capacity reached")

    existing = db.scalar(
        select(models.Registration).where(
            models.Registration.participant_id == participant_id, models.Registration.event_id == event_id
        )
    )
    if existing:
        raise HTTPException(status_code=400, detail="Participant already registered for this event")

    registration = models.Registration(participant_id=participant_id, event_id=event_id)
    db.add(registration)
    db.commit()
    db.refresh(registration)
    logger.log_event(
        actor=participant.email,
        action="participant_registered_for_event",
        details={"participant_id": participant_id, "event_id": event_id},
    )
    return registration
