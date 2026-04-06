from src.config import settings
from sqlmodel import create_engine, Session

def get_db_session():
    engine = create_engine(settings.DB_URL)
    return Session(engine)