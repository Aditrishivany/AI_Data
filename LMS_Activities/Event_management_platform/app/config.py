from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Event Management Platform"
    environment: str = "dev"
    sql_database_url: str = "sqlite:///./event_management.db"
    mongo_url: str = "mongodb://mongo:27017"
    mongo_db_name: str = "event_management"
    allow_sqlite_auto_create: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

