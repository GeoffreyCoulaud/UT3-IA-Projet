import argparse

from game import Game
from cube import Cube
from move import Move
from ida_star import IDAStar
import tests


def get_cubes_positions(game: Game) -> dict[Cube, tuple[int]]:
    """Obtenir les positions (coordonnées) de chaque cube"""
    positions = dict()
    for (col, rod) in enumerate(game.rods):
        for (row, cube) in enumerate(rod):
            positions[cube] = (col, row)
    return positions

def wrong_place_count(state: Game, goal: Game) -> int:
    """Compter les cubes à des positions différentes"""
    
    total = 0
    
    state_positions = get_cubes_positions(state)
    goal_positions = get_cubes_positions(goal)

    # S'assurer que l'on a bien les mêmes cubes
    if state_positions.keys() != goal_positions.keys():
        raise KeyError()
    
    # Compter les positions différentes deux à deux
    cubes = state_positions.keys()
    for cube in cubes:
        if state_positions.get(cube) != goal_positions.get(cube):
            total += 1
    return total

def game_successors(game: Game) -> list[Game]:
        """Renvoyer les états de jeu suivants possibles depuis un état donné"""
        
        # Identification des piques sources & destinations
        sources = list() # = piques non-vides
        destinations = list() # = piques non-pleines
        for (i, rod) in enumerate(game.rods):
            if not rod.is_empty(): sources.append(i)
            if not rod.is_full(): destinations.append(i)
        
        # Etats de jeu après les coups possibles
        # Coups = couples (s,d) s ∈ sources, d ∈ destinations, s ≠ d
        states = list()
        for s in sources:
            for d in destinations:
                if s == d: continue
                move = Move(s, d)
                state = game.copy()
                state.play_move(move)
                states.append(state)
        return states

def main():

    # Récupération des situations voulues
    parser = argparse.ArgumentParser()
    parser.add_argument("init_number", type=int, choices=range(1, len(tests.initial_situations)+1), help="Numéro de situation initiale")
    parser.add_argument("goal_number", type=int, choices=range(1, len(tests.goals)+1), help="Numéro de but")
    args = parser.parse_args()

    # Etat initial
    init = tests.initial_situations[args.init_number-1]
    goal = tests.goals[args.goal_number-1]
    
    # Affichage des états
    print("Etat initial")
    init.print()
    print("")
    print("Etat but")
    goal.print()
    print("")

    # IDA*
    is_goal = lambda game: game == goal
    heuristic = lambda game: wrong_place_count(game, goal)
    ida_star = IDAStar(init, is_goal, game_successors, heuristic)
    solution = ida_star.find_solution()

    # Affichage de la solution
    print("")
    for (i, move) in enumerate(solution, start=1):
        print(f"[Etape {i}] {str(move)}")


if __name__ == "__main__":
    main()