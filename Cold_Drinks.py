from Product import*

class Cold_Drinks(Product):
    def __init__(self, name, price,volume):
        super().__init__(name, price)
        self._volume = volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume

    def __str__(self) -> str:
        return f"{self._name} {self._price} {self._volume} "