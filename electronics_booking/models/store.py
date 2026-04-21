class Store:
    def __init__(self, store_name, product_names, product_types, product_prices, product_ratings):
        self.store_name = store_name
        self.product_names = product_names
        self.product_types = product_types
        self.product_prices = product_prices
        self.product_ratings = product_ratings

    def find_product_by_query(self, query):
        query_lower = query.lower()
        matches = []
        for i in range(len(self.product_names)):
            if (query_lower in self.product_names[i].lower() or 
                query_lower in self.product_types[i].lower()):
                matches.append(i)
        return matches

    def get_best_rated_product(self, product_indices):
        if not product_indices:
            return -1
        best_index = product_indices[0]
        for idx in product_indices[1:]:
            if self.product_ratings[idx] > self.product_ratings[best_index]:
                best_index = idx
        return best_index

    def __str__(self):
        result = f"Магазин: {self.store_name}\n"
        for i in range(len(self.product_names)):
            result += (f"  - {self.product_names[i]} ({self.product_types[i]}) | "
                       f"Цена: {self.product_prices[i]} руб. | Рейтинг: {self.product_ratings[i]}\n")
        return result