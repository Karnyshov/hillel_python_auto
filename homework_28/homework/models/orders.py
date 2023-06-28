from sqlalchemy import Column, VARCHAR, Integer
from homework_28.homework.models.base import Base


class Orders(Base):
    __tablename__ = "orders"

    id = Column(VARCHAR(30))
    product_id = Column(Integer)
    quantity = Column(Integer)

    def __repr__(self):
        return f"{self.Id} | {self.product_id} | {self.quantity}"

