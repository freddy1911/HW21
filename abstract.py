from abc import ABC, abstractmethod

from exceptions import NotEnoughSpaceError, UnknownProductError, NotEnoughProductError


class AbstractStorage(ABC):
    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, name: str, quantity: int) -> None:
        ...

    @abstractmethod
    def remove(self, name: str, quantity: int) -> None:
        ...

    @abstractmethod
    def get_free_space(self) -> int:
        ...

    @abstractmethod
    def get_items(self) -> dict:
        ...

    @abstractmethod
    def get_unique_items_count(self) -> int:
        ...


class BaseStorage(AbstractStorage):
    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    def add(self, name: str, quantity: int):
        if self.get_free_space() < quantity:
            raise NotEnoughSpaceError

        if name in self._items:
            self._items[name] += quantity
        else:
            self._items[name] = quantity

    def remove(self, name: str, quantity: int) -> None:
        if name not in self._items:
            raise UnknownProductError

        if self._items[name] < quantity:
            raise NotEnoughProductError

        self._items[name] -= quantity
        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self) -> int:
        return self._capacity - sum(self._items.values())

    def get_items(self) -> dict:
        return self._items

    def get_unique_items_count(self) -> int:
        return len(self._items)

