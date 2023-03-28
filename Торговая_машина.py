from Product import*

class Vending_Machine():
    def __init__(self):
        list = []
        self._list = list
        
    def add_product(self, product):
        self._list.append(product)

    def get_product_by_name_price(self, target_name, target_price):
        for product in self._list:
            if product._name == target_name and product._price <= target_price:
                print (product)

    def get_all_products_cheaper_that(self, target_price):
        for product in self._list:
            if product._price <= target_price:
                print(product)