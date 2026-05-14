import os
from sqlmodel import create_engine, Session
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("¡Falta la variable DATABASE_URL en el .env!")

# Motor de conexión
engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session