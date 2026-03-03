from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import events, logs, participants, trainers
from app.config import settings
from app.database import Base, engine
from app.mongo import mongo_manager


@asynccontextmanager
async def lifespan(_: FastAPI):
    if settings.allow_sqlite_auto_create and settings.sql_database_url.startswith("sqlite"):
        Base.metadata.create_all(bind=engine)
    yield
    mongo_manager.close()


app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.include_router(participants.router)
app.include_router(trainers.router)
app.include_router(events.router)
app.include_router(logs.router)


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok", "service": settings.app_name}

