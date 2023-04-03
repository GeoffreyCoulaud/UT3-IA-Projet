from typing import Sequence, Callable

from game import Game
from move import Move


class IDAStar():

    init: Game
    is_goal: Callable[[Game], bool] # Fonction qui renvoie vraie si l'état donné est un but
    get_state_chidren: Callable[[Game], Sequence[Game]] # Fonction qui renvoie les états fils d'un état
    get_state_heuristic: Callable[[Game], int] # Fonction heuristique d'un état

    threshold: int # Seuil actuel

    def __init__(
        self, 
        init: Game, 
        is_goal: Callable[[Game], bool],
        get_state_chidren: Callable[[Game], Sequence[Game]],
        get_state_heuristic: Callable[[Game], int]
    ) -> None:
        """Mettre en place le solveur IDA*"""
        self.init = init
        self.is_goal = is_goal
        self.get_state_chidren = get_state_chidren
        self.get_state_heuristic = get_state_heuristic

    def find_solution(self) -> list[Move]:
        """Trouver une liste de déplacements pour arriver à un état but. Si impossible, une liste vide de déplacements."""
        
        # Seuil initial = heuristique de l'état initial
        self.threshold = self.get_state_heuristic(self.init)
        
        # TODO implémenter + fonctions intermédiaires
        pass
