from Product import Product


class Snack(Product):
    def __init__(self, name, price,weight):
        super().__init__(name, price)
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    def __str__(self) -> str:
        return f"{self._name} {self._price} {self._weight}"