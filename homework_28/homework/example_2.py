from homework_28.homework.repositories.orders_repository import OrdersRepository

repository = OrdersRepository()
orders = repository.get_all_orders()
print(orders)

repository.add_order(
    {
        "id": 3,
        "product_id": 3,
        "quantity": 4
    }
)

new_orders = repository.get_all_orders()
print(new_orders)
