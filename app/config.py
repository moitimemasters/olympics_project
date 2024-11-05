import os

DB_USER = os.environ.get("POSTGRES_USER", "user")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password")
DB_NAME = os.environ.get("POSTGRES_DB", "olympics")
DB_HOST = os.environ.get("POSTGRES_HOST", "db")
DB_PORT = os.environ.get("POSTGRES_PORT", "5432")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
