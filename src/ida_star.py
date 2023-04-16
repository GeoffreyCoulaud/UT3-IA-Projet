from typing import Sequence, Callable
import math
import logging

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

        future_threshold = math.inf
        seen = Set()
        waiting = Stack()
        waiting.add(self.init)

        n_created = 0

        while not waiting.is_empty():
            game = waiting.pop()
            seen.add(game)

            # Solution trouvée ?
            if self.is_goal(game):
                self.solution = game
                logging.info(f"A créé {n_created} nœuds")
                return True

            # Sinon, mise en attente des états fils atteignables non-vus
            # (Etats triés selon leur score ascendant)
            children = self.get_game_chidren(game)
            children = sorted(children, key=self.f_score) 
            n_created += len(children)
            for child in children:
                f_score = self.f_score(child)
                info_line = f"profondeur={len(child.history)} score={f_score}"
                if child in seen:
                    # Ignorer les situations déjà vues
                    info_line += " (déjà vu)"
                elif f_score <= self.threshold:
                    # Si sous seuil, à explorer
                    info_line += " (en attente)"
                    waiting.add(child)
                else:
                    # Sinon, si plus petit que futur seuil, devient futur seuil
                    info_line += " (hors d'atteinte)"
                    future_threshold = min(future_threshold, f_score)
                logging.debug(info_line)

        logging.info(f"A créé {n_created} nœuds")

        # Fini sans solution
        if future_threshold == math.inf:
            return True

        # Pas fini
        else:
            self.threshold = future_threshold
            return False

    def find_solution(self) -> Sequence[Move]:
        """Trouver une liste de déplacements pour arriver à un état but. Si impossible, une liste vide de déplacements."""

        # Seuil initial = heuristique de l'état initial
        self.threshold = self.get_game_heuristic(self.init)

        # Recherche d'une solution
        while True:
            self.iteration_count += 1
            logging.info(f"IDA* iteration {self.iteration_count} seuil={self.threshold}")
            has_finished = self.bounded_depth_first_iterate()
            if has_finished: break

        # Pas de solution possible
        if self.solution is None:
            return list()

        # Solution trouvée
        return self.solution.history