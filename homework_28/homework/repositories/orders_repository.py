from homework_28.homework.repositories.base_repository import BaseRepository
from homework_28.homework.models.orders import Orders


class OrdersRepository(BaseRepository):

    def get_all_orders(self):
        orders = self.session.query(Orders).all()
        return orders

    def add_order(self, data: dict) -> None:
        order = Orders(**data)
        self.session.add(order)
        self.session.commit()

    def change_quantity_for_order(self, ID: int, quantity: int):
        self.session.query(Orders).filter(Orders.id == ID).update({"quantity": quantity})
        self.session.commit()

    def delete_by_id(self, ID: int):
        self.session.query(Orders).filter(Orders.id == ID).delete()
        self.session.commit()
