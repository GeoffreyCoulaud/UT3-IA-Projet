from typing import MutableSequence
import pickle
import copy

from rod import Rod
from cube import Cube
from move import Move


class IllegalMove(Exception): pass


class Game():

    rods: MutableSequence[Rod] = list()
    history: MutableSequence[Move] = list()
    max_rod_size: int

    def __init__(self, n_rods: int, max_rod_size: int = 4) -> None:
        self.max_rod_size = max_rod_size
        # Créer les tiges vides de la bonne taille
        for i in n_rods:
            rod = Rod(number=i, max_size=self.max_rod_size)
            self.rods.append(rod)

    def print(self) -> None:
        """Afficher le jeu, les tiges empilent les cubes à la verticale"""
        for y in range(len(self.max_rod_size)):
            line = ""
            for (x, rod) in self.rods:
                if x > 0: line += " "
                if y < rod.get_size():
                    cube = rod.get_nth(-y) # On veut parcourir du haut de la pique vers le bas
                    line += str(cube)
            print(line)

    def add_cube(self, cube: Cube, rod: int):
        """Ajouter un cube dans le jeu"""
        self.rods[rod].put(cube)
        pass

    def play_move(self, move: Move) -> None:
        """Effectuer un déplacement dans le jeu et renvoyer une copie du jeu avec le déplacement appliqué"""
        # ! Empêcher les coups illégaux (error)
        # TODO
        pass

    def copy(self):
        """Créer une copie du jeu"""
        return copy.deepcopy(self)