from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import inspect, text

from src.api import auth, inventory, logs, order_items, orders, products, users
from src.config import settings
from src.db.models import Base
from src.db.mongo import close_mongo, connect_mongo, get_logs_collection
from src.db.mysql import SessionLocal, engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    if settings.auto_create_tables:
        Base.metadata.create_all(bind=engine)
        inspector = inspect(engine)
        user_columns = [col["name"] for col in inspector.get_columns("users")]
        if "password_hash" not in user_columns:
            with engine.connect() as connection:
                connection.execute(text("ALTER TABLE users ADD COLUMN password_hash VARCHAR(255) NULL"))
                connection.commit()
    connect_mongo()
    yield
    close_mongo()


app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(inventory.router)
app.include_router(orders.router)
app.include_router(order_items.router)
app.include_router(logs.router)

ui_dir = Path("ui").resolve()
app.mount("/ui", StaticFiles(directory=str(ui_dir)), name="ui")


@app.get("/health")
async def health_check():
    mysql_ok = False
    mongo_ok = False

    db = SessionLocal()
    try:
        try:
            db.execute(text("SELECT 1"))
            mysql_ok = True
        except Exception:
            mysql_ok = False
    finally:
        db.close()

    try:
        await get_logs_collection().database.command("ping")
        mongo_ok = True
    except Exception:
        mongo_ok = False

    return {
        "app": settings.app_name,
        "mysql": "connected" if mysql_ok else "not connected",
        "mongodb": "connected" if mongo_ok else "not connected",
    }


@app.get("/api/meta/mysql-tables")
def mysql_tables():
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    tables: list[dict] = []

    with engine.connect() as connection:
        for table in table_names:
            row_count = connection.execute(text(f"SELECT COUNT(*) FROM `{table}`")).scalar() or 0
            columns = [column["name"] for column in inspector.get_columns(table)]
            rows_result = connection.execute(text(f"SELECT * FROM `{table}` LIMIT 200"))
            rows = [dict(row) for row in rows_result.mappings().all()]
            tables.append({"name": table, "rows": int(row_count), "columns": columns})
            tables[-1]["values"] = rows

    return {"database": "MySQL", "tables": tables}


@app.get("/api/meta/mongodb")
async def mongodb_meta():
    collection = get_logs_collection()
    db = collection.database
    collection_names = await db.list_collection_names()
    collections: list[dict] = []

    for collection_name in collection_names:
        coll = db[collection_name]
        document_count = await coll.count_documents({})
        sample_doc = await coll.find_one()
        fields = sorted(list(sample_doc.keys())) if sample_doc else []
        docs = await coll.find().sort("_id", -1).limit(200).to_list(length=200)
        cleaned_docs = []
        for doc in docs:
            cleaned = {}
            for key, value in doc.items():
                cleaned[key] = str(value) if key == "_id" else value
            cleaned_docs.append(cleaned)
        collections.append(
            {
                "name": collection_name,
                "documents": int(document_count),
                "fields": fields,
                "values": cleaned_docs,
            }
        )

    return {"database": "MongoDB", "collections": collections}


@app.get("/")
def home_page():
    return FileResponse(ui_dir / "index.html")


@app.get("/users-page")
def users_page():
    return FileResponse(ui_dir / "users.html")


@app.get("/register-page")
def register_page():
    return FileResponse(ui_dir / "register.html")


@app.get("/login-page")
def login_page():
    return FileResponse(ui_dir / "login.html")


@app.get("/products-page")
def products_page():
    return FileResponse(ui_dir / "products.html")


@app.get("/inventory-page")
def inventory_page():
    return FileResponse(ui_dir / "inventory.html")


@app.get("/orders-page")
def orders_page():
    return FileResponse(ui_dir / "orders.html")


@app.get("/logs-page")
def logs_page():
    return FileResponse(ui_dir / "logs.html")
