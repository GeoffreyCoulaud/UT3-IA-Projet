from game import Game
from cube import Cube

def main():

    # Test d'implémentation 1, page 5
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
    init.print()

    # TODO : Ajouter les états buts et tout afficher.
    # TODO : Implémenter IDA* 

if __name__ == "__main__":
    main()