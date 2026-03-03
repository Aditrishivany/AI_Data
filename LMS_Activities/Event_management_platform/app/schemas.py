from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ParticipantBase(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    phone: str | None = Field(default=None, max_length=20)


class ParticipantCreate(ParticipantBase):
    pass


class ParticipantUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=2, max_length=100)
    email: EmailStr | None = None
    phone: str | None = Field(default=None, max_length=20)


class ParticipantOut(ParticipantBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TrainerBase(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    expertise: str | None = Field(default=None, max_length=150)
    bio: str | None = None


class TrainerCreate(TrainerBase):
    pass


class TrainerUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=2, max_length=100)
    email: EmailStr | None = None
    expertise: str | None = Field(default=None, max_length=150)
    bio: str | None = None


class TrainerOut(TrainerBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class EventBase(BaseModel):
    title: str = Field(min_length=2, max_length=150)
    description: str | None = None
    capacity: int = Field(ge=1, le=100000)


class EventCreate(EventBase):
    trainer_id: int | None = None


class EventUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=150)
    description: str | None = None
    capacity: int | None = Field(default=None, ge=1, le=100000)
    trainer_id: int | None = None


class EventOut(EventBase):
    id: int
    trainer_id: int | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CapacityUpdate(BaseModel):
    capacity: int = Field(ge=1, le=100000)


class RegistrationOut(BaseModel):
    id: int
    participant_id: int
    event_id: int
    registered_at: datetime

    model_config = ConfigDict(from_attributes=True)


class LogCreate(BaseModel):
    actor: str = Field(min_length=1, max_length=100)
    action: str = Field(min_length=1, max_length=200)
    details: dict = Field(default_factory=dict)


class FeedbackCreate(BaseModel):
    participant_email: EmailStr
    event_id: int
    comment: str = Field(min_length=1, max_length=2000)

