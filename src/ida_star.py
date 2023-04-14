from typing import Sequence, Callable
import math

from game import Game
from move import Move
from custom_collections import Stack, Set


class IDAStar():

    init: Game
    is_goal: Callable[[Game], bool] # Fonction qui renvoie vraie si l'état donné est un but
    get_game_chidren: Callable[[Game], Sequence[Game]] # Fonction qui renvoie les états fils d'un état
    get_game_heuristic: Callable[[Game], int] # Fonction heuristique (score) d'un état

    threshold: int # Seuil actuel lors de l'itération
    solution: Game = None # Solution trouvée
    iteration_count = 0

    def __init__(
        self, 
        init: Game, 
        is_goal: Callable[[Game], bool],
        get_game_chidren: Callable[[Game], Sequence[Game]],
        get_game_heuristic: Callable[[Game], int]
    ) -> None:
        """Mettre en place le solveur IDA*"""
        self.init = init
        self.is_goal = is_goal
        self.get_game_chidren = get_game_chidren
        self.get_game_heuristic = get_game_heuristic

    def f_score(self, game: Game) -> int:
        return len(game.history) + self.get_game_heuristic(game)

    def bounded_depth_first_iterate(self) -> bool:
        """Iteration en profondeur jusqu'à un seuil.
        
        Renvoie True si a trouvé une solution ou prouve qu'il n'y en a pas, sinon False = pas encore terminé."""

        new_threshold = math.inf
        seen = Set()
        waiting = Stack()
        waiting.add(self.init)

        n_created = 0
        
        while not waiting.is_empty():
            game = waiting.pop()
            seen.add(game)

            # Solution trouvée ?
            if self.is_goal(game):
                print(f"Created {n_created} nodes")
                self.solution = game
                return True

            # Sinon, mise en attente des états fils atteignables non-vus
            children = self.get_game_chidren(game)
            n_created += len(children)
            for child in sorted(children, key=self.f_score):
                f_score = self.f_score(child)
                if (f_score <= self.threshold) and (child not in seen): 
                    waiting.add(child)
                else:
                    new_threshold = min(new_threshold, f_score)
        
        print(f"Created {n_created} nodes")

        # Fini sans solution
        if new_threshold == math.inf:
            return True

        # Pas fini
        else:
            self.threshold = new_threshold
            return False

    def find_solution(self) -> Sequence[Move]:
        """Trouver une liste de déplacements pour arriver à un état but. Si impossible, une liste vide de déplacements."""
        
        # Seuil initial = heuristique de l'état initial
        self.threshold = self.get_game_heuristic(self.init)
        
        # Recherche d'une solution
        while True:
            self.iteration_count += 1
            print(f"IDA* iteration {self.iteration_count} (seuil {self.threshold})") # ! Info de debug
            has_finished = self.bounded_depth_first_iterate()
            if has_finished: break

        # Pas de solution possible
        if self.solution is None:
            return list()

        # Solution trouvée
        return self.solution.history