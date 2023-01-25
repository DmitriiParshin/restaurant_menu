from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import settings

DATABASE_URL = (
    f"postgresql://{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:"
    f"{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"
)

engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    session = Session()
    Base.metadata.create_all(engine)
    try:
        yield session
    finally:
        session.close()
