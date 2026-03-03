from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    registrations: Mapped[list["Registration"]] = relationship(
        "Registration", back_populates="participant", cascade="all, delete-orphan"
    )


class Trainer(Base):
    __tablename__ = "trainers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False, index=True)
    expertise: Mapped[str | None] = mapped_column(String(150), nullable=True)
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    events: Mapped[list["Event"]] = relationship("Event", back_populates="trainer")


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    trainer_id: Mapped[int | None] = mapped_column(ForeignKey("trainers.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    trainer: Mapped["Trainer | None"] = relationship("Trainer", back_populates="events")
    registrations: Mapped[list["Registration"]] = relationship(
        "Registration", back_populates="event", cascade="all, delete-orphan"
    )


class Registration(Base):
    __tablename__ = "registrations"
    __table_args__ = (UniqueConstraint("participant_id", "event_id", name="uq_participant_event"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    participant_id: Mapped[int] = mapped_column(ForeignKey("participants.id"), nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    participant: Mapped["Participant"] = relationship("Participant", back_populates="registrations")
    event: Mapped["Event"] = relationship("Event", back_populates="registrations")

