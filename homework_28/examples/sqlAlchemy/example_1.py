from sqlalchemy import create_engine, Column, select, VARCHAR, Integer
from sqlalchemy.orm import declarative_base, Session


driver_name = "postgresql+psycopg2"
host = "127.0.0.1"
port = "5432"
database = "store"
user = "postgres"
password = "12345"

engine = create_engine(f"{driver_name}://{user}:{password}@{host}:{port}/{database}")

Base = declarative_base()


class Orders(Base):
    __tablename__ = "orders"

    Id = Column(VARCHAR(30))
    product_id = Column(Integer)
    quantity = Column(Integer)

    def __repr__(self):
        return f"{self.Id} | {self.product_id} | {self.quantity}"


session = Session(engine)

session.query(Orders).all()
