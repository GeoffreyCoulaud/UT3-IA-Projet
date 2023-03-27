from typing import MutableSequence
from rod import Rod


class IllegalMove(Exception): pass


class Game():

    rods: MutableSequence[Rod] = list()
    max_rod_size: int = 3

    def print(self) -> None:
        """Afficher le jeu, les tiges empilent les cubes à la verticale"""
        # TODO
        pass

    def move(self, source: Rod, destination: Rod) -> None:
        """Déplacer le cube du dessus de la source vers la destination"""
        # ! Empêcher les coups illégaux (error)
        # TODO
        pass