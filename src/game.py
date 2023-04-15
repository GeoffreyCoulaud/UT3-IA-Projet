from typing import MutableSequence, Iterable
import copy

from rod import Rod
from cube import Cube
from move import Move


class Game():

    rods: MutableSequence[Rod]
    max_rod_size: int

    history: MutableSequence[Move] # Déplacements joués pour arriver à cet état
    total_cost: int # Coût pour arriver à cet état

    def __init__(self, n_rods: int, max_rod_size: int = 4):
        self.rods = list()
        self.history = list()
        self.total_cost = 0
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
        for row in range(self.max_rod_size-1, -1, -1):
            text_line = ""
            for rod in self.rods:
                # Espace horizontal précédent chaque cube
                if rod.number > 0: 
                    text_line += " "
                # Laisser du blanc si pique vide ou n'a rien à cette ligne
                if rod.is_empty() or len(rod) <= row:
                    text_line += "  "
                    continue
                # Afficher le cube
                cube = rod[row]
                text_line += str(cube)
            print(text_line)

    def add_cube(self, rod_index: int, cube: Cube):
        """Ajouter un cube sur la pique donnée dans le jeu"""
        self.rods[rod_index].add(cube)

    def copy(self):
        """Créer une copie du jeu"""
        return copy.deepcopy(self)
    
    def play_move(self, move: Move):
        """Appliquer un déplacement dans le jeu (en place, ne crée pas de copie)"""
        
        # Ajout du déplacement à l'historique
        self.history.append(move)
        self.total_cost += 1

        # Application du déplacement
        source_rod = self.rods[move.source]
        cube = source_rod.pop()
        destination_rod = self.rods[move.destination] 
        destination_rod.add(cube)