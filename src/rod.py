from typing import MutableSequence

from cube import Cube


class RodOverflow(Exception):
    pass


class RodIsEmpty(Exception):
    pass


class Rod():

    cubes: MutableSequence[Cube] = list()
    max_size: int
    number: int

    def __init__(self, number: int, max_size: int = 3) -> None:
        self.number = number
        self.max_size = max_size

    def put(self, cube: Cube) -> None:
        """Ajouter un cube au dessus"""
        # ! Bloquer l'ajout qui dépasse la taille max (error)
        # TODO
        pass

    def pick(self) -> Cube:
        """Prendre et retourner le cube du dessus"""
        # ! Bloquer prendre quand vide (error)
        # TODO
        pass

    def get_top(self) -> Cube:
        """Obtenir une copie du cube du dessus, sans l'enlever"""
        # ! Bloquer lire quand vide (error)
        # TODO
        pass

    def get_nth(self, n: int) -> Cube:
        """Obtenir une copie du nième cube. 0 = en bas."""
        # ! Bloquer lire quand vide (error)
        # TODO
        pass

    def get_size(self) -> int:
        return len(self.cubes)

    def is_empty(self) -> bool:
        return self.get_size() == 0