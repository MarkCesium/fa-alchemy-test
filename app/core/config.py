from dotenv import load_dotenv
from os import getenv

load_dotenv("...")

db_url: str = getenv("DB_URL")
