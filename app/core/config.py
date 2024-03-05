from dotenv import load_dotenv
from os import getenv


def get_db_url() -> str:
    load_dotenv()

    db_user: str = getenv("DB_USER")
    db_pass: str = getenv("DB_PASS")
    db_name: str = getenv("DB_NAME")

    return f"postgresql+asyncpg://{db_user}:{db_pass}@0.0.0.0:5432/{db_name}"


db_url: str = get_db_url()
