from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Cloud-Native Inventory & Order Management System"
    app_version: str = "1.0.0"
    debug: bool = True

    mysql_url: str = "mysql+pymysql://root:root123@localhost:3306/inventory_db"
    mongodb_url: str = "mongodb://localhost:27017"
    mongodb_db_name: str = "inventory_activity_db"
    mongodb_collection_name: str = "activity_logs"

    auto_create_tables: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
