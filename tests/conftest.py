import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
from db.models import Base

test_engine = create_engine(DATABASE_URL)

test_session = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine
)


@pytest.fixture(scope='session', autouse=True)
def create_tables():
    Base.metadata.create_all(test_engine)


@pytest.fixture(scope='session', autouse=True)
def drop_tables():
    Base.metadata.drop_all(test_engine)





