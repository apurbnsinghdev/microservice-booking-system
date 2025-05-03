from sqlmodel import Session, SQLModel, create_engine
from typing import Generator

def get_engine(db_url: str):
    return create_engine(db_url, echo=True)

def init_db(engine):
    SQLModel.metadata.create_all(engine)

def get_session(engine) -> Generator:
    def _get_session():
        with Session(engine) as session:
            yield session
    return _get_session

