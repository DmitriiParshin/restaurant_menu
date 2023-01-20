from envparse import Env


env = Env()

DATABASE_URL = env.str(
    'DATABASE_URL',
    default='postgresql://postgres:postgres@127.0.0.1:5432/postgres'
)

TEST_DATABASE_URL = env.str(
    'TEST_DATABASE_URL',
    default='postgresql://postgres_test:postgres_test@127.0.0.1:5433/postgres_test'
)
