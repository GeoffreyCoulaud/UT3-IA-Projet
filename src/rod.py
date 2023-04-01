from typing import MutableSequence

from cube import Cube


class RodOverflow(Exception):
    pass


class RodIsEmpty(Exception):
    pass


class Rod():
    """
    Classe qui représente une pique du jeu.
    
    Les cubes sont stockés dans une Pile/LIFO où le "dessous" est l'index 0.   
    On ajoute donc des cubes à la fin de la liste des cubes.
    """

    cubes: MutableSequence[Cube] = list()
    max_size: int
    number: int

    def __init__(self, number: int, max_size: int = 3) -> None:
        self.number = number
        self.max_size = max_size

    def put(self, cube: Cube) -> None:
        """Ajouter un cube au dessus de la pique.
        Soulève une erreur dans le cas où la pique est déjà pleine."""
        if len(self.cubes) == self.max_size:
            raise RodOverflow()
        self.cubes.append(cube)
        pass

    def pop(self) -> Cube:
        """Prendre et retourner le cube du dessus"""
        if self.is_empty():
            raise RodIsEmpty()
        return self.cubes.pop()

    def get_top(self) -> Cube:
        """Obtenir une copie du cube du dessus, sans l'enlever"""
        return self.get_nth(-1)

    def get_nth(self, n: int) -> Cube:
        """Obtenir une copie du nième cube. Le bas de la pique est index 0.
        Fournir un index négatif donne à partir de la fin, -1 étant le dessus."""
        if self.is_empty():
            raise RodIsEmpty()
        return self.cubes[n]

    def get_size(self) -> int:
        """Obtenir le nombre de cubes dans la pique"""
        return len(self.cubes)

    def is_empty(self) -> bool:
        """Savoir si la pique est vide"""
        return self.get_size() == 0