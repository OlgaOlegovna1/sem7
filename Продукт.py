class Product():
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name (self):
        return self._name

    @name.setter
    def name (self, new_name):
        self._name = new_name