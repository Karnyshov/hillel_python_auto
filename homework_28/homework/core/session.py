from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class BaseSession:
    driver_name = "postgresql+psycopg2"
    host = "127.0.0.1"
    port = "5432"
    database = "store"
    user = "postgres"
    password = "12345"

    engine = create_engine(f"{driver_name}://{user}:{password}@{host}:{port}/{database}", echo=True)

    session = Session(engine)
