from game import Game
from cube import Cube
from move import Move
from ida_star import IDAStar


def get_cubes_positions(game: Game) -> dict[Cube, tuple[int]]:
    """Obtenir les positions (coordonnées) de chaque cube"""
    positions = dict()
    for (col, rod) in enumerate(game):
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

    # --- Test d'implémentation avec but 1, page 5
    
    # Etat initial
    init: Game = Game(n_rods=4, max_rod_size=3)
    init.add_cube(Cube(3, "J"), rod_index=0)
    init.add_cube(Cube(2, "J"), rod_index=0)
    init.add_cube(Cube(1, "J"), rod_index=1)
    init.add_cube(Cube(3, "B"), rod_index=2)
    init.add_cube(Cube(2, "B"), rod_index=2)
    init.add_cube(Cube(1, "B"), rod_index=2)
    init.add_cube(Cube(3, "R"), rod_index=3)
    init.add_cube(Cube(2, "R"), rod_index=3)
    init.add_cube(Cube(1, "R"), rod_index=3)
    
    # Etat but
    goal: Game = Game(n_rods=4, max_rod_size=3)
    goal.add_cube(Cube(3, "J"), rod_index=0)
    goal.add_cube(Cube(2, "J"), rod_index=0)
    goal.add_cube(Cube(1, "J"), rod_index=0)
    goal.add_cube(Cube(3, "B"), rod_index=2)
    goal.add_cube(Cube(2, "B"), rod_index=2)
    goal.add_cube(Cube(1, "B"), rod_index=2)
    goal.add_cube(Cube(3, "R"), rod_index=3)
    goal.add_cube(Cube(2, "R"), rod_index=3)
    goal.add_cube(Cube(1, "R"), rod_index=3)
    
    # Affichage initial
    print("Etat initial")
    init.print()
    print("Etat but")
    goal.print()

    # IDA*
    is_goal = lambda game: game == goal
    heuristic = lambda game: wrong_place_count(game, goal)
    ida_star = IDAStar(init, is_goal, game_successors, heuristic)
    solution = ida_star.find_solution()

    # Affichage de la solution
    print(solution)


if __name__ == "__main__":
    main()