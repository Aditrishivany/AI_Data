import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session, sessionmaker

from app.database import Base
from app.dependencies import get_db, get_logger
from app.main import app


class FakeLogger:
    def __init__(self):
        self.docs = [{"id": "1", "actor": "system"}]

    def log_event(self, actor: str, action: str, details: dict):
        return {"actor": actor, "action": action, "details": details}

    def log_user_activity(self, actor: str, action: str, details: dict):
        return {"actor": actor, "action": action, "details": details}

    def add_feedback(self, participant_email: str, event_id: int, comment: str):
        return {"participant_email": participant_email, "event_id": event_id, "comment": comment}

    def get_docs(self, collection: str, limit: int = 100):
        return self.docs[:limit]

    def update_doc(self, collection: str, doc_id: str, payload: dict):
        return True

    def delete_doc(self, collection: str, doc_id: str):
        return True


@pytest.fixture()
def session() -> Session:
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        future=True,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session: Session):
    def override_db():
        yield session

    app.dependency_overrides[get_db] = override_db
    app.dependency_overrides[get_logger] = lambda: FakeLogger()
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
