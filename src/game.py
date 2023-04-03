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
        for i in range(n_rods):
            rod = Rod(number=i, max_size=self.max_rod_size)
            self.rods.append(rod)

    def print(self) -> None:
        """Afficher le jeu, les tiges empilent les cubes à la verticale"""
        for line_index in range(self.max_rod_size-1, -1, -1):
            text_line = ""
            for column_index in range(len(self.rods)):
                rod = self.rods[column_index]
                # Espace horizontal précédent chaque cube
                if column_index > 0: 
                    text_line += " "
                # Laisser du blanc si pique vide ou n'a rien à cette ligne
                if rod.is_empty() or rod.get_size() <= line_index:
                    text_line += "  "
                    continue
                # Afficher le cube
                cube = rod.get_nth(line_index)
                text_line += str(cube)
            print(text_line)

    def add_cube(self, cube: Cube, rod_index: int):
        """Ajouter un cube dans le jeu"""
        rod = self.rods[rod_index]
        rod.put(cube)
        # print("DEBUG ajout de cube", cube, "dans rod", rod_index, "remplie à", rod.get_size(), "/", rod.max_size)

    def play_move(self, move: Move) -> None:
        """Effectuer un déplacement dans le jeu et renvoyer une copie du jeu avec le déplacement appliqué"""
        # ! Empêcher les coups illégaux (error)
        # TODO
        pass

    def copy(self):
        """Créer une copie du jeu"""
        return copy.deepcopy(self)