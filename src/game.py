from typing import MutableSequence
import pickle

from rod import Rod
from cube import Cube
from move import Move


class IllegalMove(Exception): pass


class Game():

    rods: MutableSequence[Rod] = list()
    move_history: MutableSequence[Move] = list()
    max_rod_size: int = 4

    def __init__(self, n_rods: int) -> None:
        # Créer les tiges vides de la bonne taille
        for i in n_rods:
            rod = Rod(number=i, max_size=self.max_rod_size)
            self.rods.append(rod)

    def print(self) -> None:
        """Afficher le jeu, les tiges empilent les cubes à la verticale"""
        # TODO
        pass

    def add_cube(self, cube: Cube, rod: int):
        """Ajouter un cube dans le jeu"""
        # TODO
        pass


    def play_move(self, move: Move) -> None:
        """Effectuer un déplacement dans le jeu et renvoyer une copie du jeu avec le déplacement appliqué"""
        # ! Empêcher les coups illégaux (error)
        # TODO
        pass

    def copy(self):
        """Créer une copie du jeu"""
        str_repr = pickle.dumps(self)
        copy = pickle.loads(str_repr)
        return copy