import random

class Customer:
    def __init__(self, first_name, last_name, patronymic, account_balance, product_query):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.account_balance = account_balance
        self.bonus_points = random.randint(0, 5000)  # бонусные баллы до 5000
        self.product_query = product_query

    def get_total_available_funds(self):
        return self.account_balance + self.bonus_points

    def __str__(self):
        return (f"Покупатель: {self.last_name} {self.first_name} {self.patronymic}\n"
                f"Баланс: {self.account_balance:.2f} руб.\n"
                f"Бонусные баллы: {self.bonus_points}\n"
                f"Желаемый товар: {self.product_query}")