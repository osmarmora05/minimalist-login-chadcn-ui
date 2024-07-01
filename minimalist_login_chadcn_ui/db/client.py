from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv()
TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

dbUrl = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

# https://docs.turso.tech/sdk/python/orm/sqlalchemy
def connect():
    engine = create_engine(dbUrl, connect_args={
                           'check_same_thread': False}, echo=True)
    return engine