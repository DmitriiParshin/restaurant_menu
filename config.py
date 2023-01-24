from envparse import Env

env = Env()

DATABASE_URL = env.str(
    "DATABASE_URL",
    default="postgresql://postgres:postgres@0.0.0.0:5432/postgres",
)

TEST_DATABASE_URL = env.str(
    "TEST_DATABASE_URL",
    default="postgresql://postgres:postgres@0.0.0.0:5433/postgres",
)
