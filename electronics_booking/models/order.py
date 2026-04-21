class Order:
    def __init__(self):
        self.store_name = None
        self.customer_full_name = None
        self.product_name = None
        self.product_type = None
        self.order_cost = None

    def check_product_exists(self, customer, store):
        matches = store.find_product_by_query(customer.product_query)
        if matches:
            best_index = store.get_best_rated_product(matches)
            return True, best_index
        return False, -1

    def can_afford(self, customer, price):
        return customer.get_total_available_funds() >= price

    def place_order(self, customer, stores):
        best_store = None
        best_product_idx = -1
        best_rating = -1

        for store in stores:
            exists, product_idx = self.check_product_exists(customer, store)
            if exists:
                price = store.product_prices[product_idx]
                rating = store.product_ratings[product_idx]
                if (self.can_afford(customer, price) and rating > best_rating):
                    best_rating = rating
                    best_store = store
                    best_product_idx = product_idx

        if best_store is not None:
            self.store_name = best_store.store_name
            self.customer_full_name = f"{customer.last_name} {customer.first_name} {customer.patronymic}"
            self.product_name = best_store.product_names[best_product_idx]
            self.product_type = best_store.product_types[best_product_idx]
            self.order_cost = best_store.product_prices[best_product_idx]

            price = self.order_cost
            if customer.bonus_points >= price:
                customer.bonus_points -= int(price)
            else:
                remaining = price - customer.bonus_points
                customer.bonus_points = 0
                customer.account_balance -= remaining

            return True
        return False

    def suggest_alternative(self, customer, stores):
        for store in stores:
            matches = store.find_product_by_query(customer.product_query)
            for idx in matches:
                price = store.product_prices[idx]
                if self.can_afford(customer, price):
                    print(f"\nАльтернатива: магазин '{store.store_name}'")
                    print(f"  Товар: {store.product_names[idx]} ({store.product_types[idx]})")
                    print(f"  Цена: {price} руб.")
                    print(f"  Рейтинг: {store.product_ratings[idx]}")
                    return
        print("К сожалению, нет подходящих альтернатив в пределах вашего бюджета.")

    def print_order_info(self):
        if self.store_name:
            print("\n=== ИНФОРМАЦИЯ О ЗАКАЗЕ ===")
            print(f"Магазин: {self.store_name}")
            print(f"Покупатель: {self.customer_full_name}")
            print(f"Товар: {self.product_name}")
            print(f"Категория: {self.product_type}")
            print(f"Стоимость заказа: {self.order_cost:.2f} руб.")
        else:
            print("\nЗаказ не оформлен: подходящий товар не найден или недостаточно средств.")