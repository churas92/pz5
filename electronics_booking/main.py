from datetime import datetime
from models.customer import Customer
from models.store import Store
from models.order import Order

def create_sample_stores():
    stores = [
        Store(
            store_name="DNS",
            product_names=["iPhone 15", "Samsung Galaxy S24", "Xiaomi Mi 11"],
            product_types=["смартфон", "смартфон", "смартфон"],
            product_prices=[80000, 70000, 40000],
            product_ratings=[4.8, 4.7, 4.5]
        ),
        Store(
            store_name="M.Video",
            product_names=["Samsung QLED TV", "LG OLED TV", "Sony Bravia"],
            product_types=["телевизор", "телевизор", "телевизор"],
            product_prices=[120000, 110000, 130000],
            product_ratings=[4.9, 4.8, 4.7]
        ),
        Store(
            store_name="Eldorado",
            product_names=["Dyson V15", "Xiaomi Vacuum", "Polaris PV"],
            product_types=["пылесос", "пылесос", "пылесос"],
            product_prices=[50000, 25000, 15000],
            product_ratings=[4.9, 4.6, 4.3]
        ),
        Store(
            store_name="Citilink",
            product_names=["MacBook Pro 14", "Asus ROG", "Lenovo ThinkPad"],
            product_types=["ноутбук", "ноутбук", "ноутбук"],
            product_prices=[200000, 150000, 100000],
            product_ratings=[4.9, 4.8, 4.7]
        ),
        Store(
            store_name="Technopark",
            product_names=["PlayStation 5", "Xbox Series X", "Nintendo Switch"],
            product_types=["игровая приставка", "игровая приставка", "игровая приставка"],
            product_prices=[60000, 55000, 30000],
            product_ratings=[4.9, 4.8, 4.6]
        )
    ]
    return stores

def input_customer_data():
    print("=== ВВОД ДАННЫХ ПОКУПАТЕЛЯ ===")
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    patronymic = input("Отчество: ")
    account_balance = float(input("Баланс счёта (руб.): "))
    
    product_query = input("Желаемый товар (название или тип, например 'пылесос' или 'iPhone'): ")
    
    return Customer(
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
        account_balance=account_balance,
        product_query=product_query
    )

def main():
    stores = create_sample_stores()
    
    print("\n=== ДОСТУПНЫЕ МАГАЗИНЫ И ТОВАРЫ ===")
    for i, store in enumerate(stores, 1):
        print(f"\n{i}. {store}")
    
    customer = input_customer_data()
    
    order = Order()
    
    success = order.place_order(customer, stores)
    
    order.print_order_info()
    
    if not success:
        print("\n=== ПРЕДЛОЖЕНИЕ АЛЬТЕРНАТИВЫ ===")
        order.suggest_alternative(customer, stores)
    
    print(f"\n=== ИЗМЕНЁННЫЕ ДАННЫЕ ПОКУПАТЕЛЯ ===")
    print(customer)

if __name__ == "__main__":
    main()