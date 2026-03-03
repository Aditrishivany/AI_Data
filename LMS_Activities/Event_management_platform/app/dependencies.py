from collections.abc import Generator

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.services.activity_logger import ActivityLogger


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_logger() -> ActivityLogger:
    return ActivityLogger()

