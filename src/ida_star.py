from game import Game
from move import Move


class IDAStar():

    start_game: Game
    goal: Game
    depth: int

    def find_solution(self) -> list[Move]:
        pass
