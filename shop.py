from abstract import BaseStorage
from exceptions import TooMuchNamesError


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, name: str, quantity: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooMuchNamesError

        super().add(name, quantity)
