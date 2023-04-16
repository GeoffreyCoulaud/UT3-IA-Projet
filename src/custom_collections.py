from typing import Iterator
from abc import ABC
from math import inf


class Collection(ABC):
    """Classe de base qui représente une collection"""

    _items: list

    def __init__(self) -> None:
        super().__init__()
        self._items = list()

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def add(self, item) -> None:
        """Abstrait, à implémenter dans les descendants"""
        raise NotImplementedError()

    def remove(self, item) -> None:
        """Abstrait, à implémenter dans les descendants"""
        raise NotImplementedError()

    def __len__(self) -> int:
        return self._items.__len__()

    def __iter__(self) -> Iterator:
        return self._items.__iter__()


class OrderedCollection(Collection):

    def pop(self) -> None:
        return self._items.pop()

    def top(self):
        return self._items[len(self._items) - 1]

    def __getitem__(self, i):
        return self._items.__getitem__(i)


class Queue(OrderedCollection):
    """Classe représentant une file (premier arrivé, premier sorti)"""

    def add(self, item) -> None:
        self._items.insert(0, item)


class Stack(OrderedCollection):
    """Classe représentant une pile (dernier arrivé, premier sorti)"""

    def add(self, item) -> None:
        self._items.append(item)


class BoundedCollection(Collection):
    """Classe représentant une collection avec une taille maximale"""

    max_size = inf

    def __init__(self, max_size: int) -> None:
        super().__init__()
        self.max_size = max_size

    def is_full(self) -> bool:
        return len(self) == self.max_size

    def add(self, item) -> None:
        if self.is_full(): 
            raise ValueError("Collection is full")
        return super().add(item)


class BoundedStack(Stack, BoundedCollection):
    """Classe représentant une pile avec une taille maximum"""
    pass


class Set(Collection):
    """Classe représentant un ensemble d'éléments uniques"""

    def add(self, item):
        if item in self._items: return
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __contains__(self, item):
        return self._items.__contains__(item)