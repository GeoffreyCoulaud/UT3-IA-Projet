from game import Game
from cube import Cube

def main():

    # Test d'implémentation 1, page 5
    init: Game = Game(n_rods=4, max_rod_size=3)
    init.add_cube(Cube(number=3, color="J"), 0)
    init.add_cube(Cube(number=2, color="J"), 0)
    init.add_cube(Cube(number=1, color="J"), 1)
    init.add_cube(Cube(number=3, color="B"), 2)
    init.add_cube(Cube(number=2, color="B"), 2)
    init.add_cube(Cube(number=1, color="B"), 2)

    # TODO : Ajouter les états buts et tout afficher.
    # TODO : Implémenter IDA* 

if __name__ == "__main__":
    main()