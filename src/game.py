from typing import MutableSequence
import copy

from rod import Rod
from cube import Cube
from move import Move


class Game():

    rods: MutableSequence[Rod] = list()
    max_rod_size: int

    history: MutableSequence[Move] = list() # Déplacements joués pour arriver à cet état
    total_cost: int = 0 # Coût pour arriver à cet état

    def __init__(self, n_rods: int, max_rod_size: int = 4) -> None:
        self.max_rod_size = max_rod_size
        # Créer les tiges vides de la bonne taille
        for i in range(n_rods):
            rod = Rod(number=i, max_size=self.max_rod_size)
            self.rods.append(rod)

    def __eq__(self, other) -> bool:
        """Deux jeux sont égaux s'ils ont les mêmes cubes au même endroit"""
        if len(self.rods) != len(other.rods):
            return False
        for (a, b) in zip(self.rods, other.rods):
            if a != b:
                return False
        return True

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

    def copy(self):
        """Créer une copie du jeu"""
        return copy.deepcopy(self)
    
    def play_move(self, move: Move):
        """Appliquer un déplacement dans le jeu (en place, ne crée pas de copie)"""
        
        # Ajout du déplacement à l'historique
        self.history.append(move) 

        # Application du déplacement
        source_rod = self.rods[move.source]
        cube = source_rod.pop()
        destination_rod = self.rods[move.destination] 
        destination_rod.put(cube)