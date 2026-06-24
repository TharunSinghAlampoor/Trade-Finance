from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from pathlib import Path


class Settings(BaseSettings):
    # ---------------- APP ----------------
    APP_NAME: str = "trade-finance-m2"
    DEBUG: bool = False

    # ---------------- DATABASE ----------------
    DATABASE_URL: str

    # ---------------- JWT ----------------
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # ---------------- BOOTSTRAP ADMIN ----------------
    BOOTSTRAP_ADMIN_EMAIL: str
    BOOTSTRAP_ADMIN_PASSWORD: str
    BOOTSTRAP_ADMIN_ORG: str

    # ---------------- CELERY ----------------
    CELERY_BROKER_URL: Optional[str] = None
    CELERY_RESULT_BACKEND: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="forbid",
    )


print("=" * 60)
print("CURRENT WORKING DIRECTORY:", Path.cwd())
print("ENV FILE PATH:", Path(".env").resolve())
print("=" * 60)

settings = Settings()

print("LOADED DATABASE_URL =", settings.DATABASE_URL)
print("=" * 60)