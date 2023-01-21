from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL


engine = create_engine(DATABASE_URL)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = session()
    try:
        yield db
    finally:
        db.close()
