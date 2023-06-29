from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from homework_28.homework.models.base import Base


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer)
    quantity: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Order(id={self.id!r}, product_id={self.product_id!r}, quantity={self.quantity!r})"
