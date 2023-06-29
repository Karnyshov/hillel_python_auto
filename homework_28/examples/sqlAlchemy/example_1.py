from sqlalchemy import create_engine, Integer
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

driver_name = "postgresql+psycopg2"
host = "127.0.0.1"
port = "5432"
database = "store"
user = "postgres"
password = "12345"


class Base(DeclarativeBase):
    pass


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer)
    quantity: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Order(id={self.id!r}, product_id={self.product_id!r}, quantity={self.quantity!r})"


engine = create_engine(f"{driver_name}://{user}:{password}@{host}:{port}/{database}", echo=True)

session = Session(engine)

print(session.query(Orders).all())
