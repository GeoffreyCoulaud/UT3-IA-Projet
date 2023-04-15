from game import Game
from cube import Cube

# ----------------------------------------- Situations initiales pages 5-6 du sujet 

initial_situations = list()

def __generate_initial_situations():

    global initial_situations

    # Situation initiale 1
    init = Game(n_rods=4, max_rod_size=3)
    init.add_cube(0, Cube(3, "J"))
    init.add_cube(0, Cube(2, "J"))
    init.add_cube(1, Cube(1, "J"))
    init.add_cube(2, Cube(3, "B"))
    init.add_cube(2, Cube(2, "B"))
    init.add_cube(2, Cube(1, "B"))
    init.add_cube(3, Cube(3, "R"))
    init.add_cube(3, Cube(2, "R"))
    init.add_cube(3, Cube(1, "R"))
    initial_situations.append(init)

    # Situation initiale 2
    init = Game(n_rods=4, max_rod_size=3)
    init.add_cube(0, Cube(3, "J"))
    init.add_cube(0, Cube(2, "J"))
    init.add_cube(0, Cube(1, "J"))
    init.add_cube(1, Cube(3, "B"))
    init.add_cube(1, Cube(2, "B"))
    init.add_cube(1, Cube(1, "B"))
    init.add_cube(2, Cube(3, "R"))
    init.add_cube(2, Cube(2, "R"))
    init.add_cube(2, Cube(1, "R"))
    initial_situations.append(init)

# ----------------------------------------- Buts pages 5-6 du sujet

goals = list()

def __generate_goals():

    global goals

    # But 1
    goal = Game(n_rods=4, max_rod_size=3)
    goal.add_cube(0, Cube(3, "J"))
    goal.add_cube(0, Cube(2, "J"))
    goal.add_cube(0, Cube(1, "J"))
    goal.add_cube(2, Cube(3, "B"))
    goal.add_cube(2, Cube(2, "B"))
    goal.add_cube(2, Cube(1, "B"))
    goal.add_cube(3, Cube(3, "R"))
    goal.add_cube(3, Cube(2, "R"))
    goal.add_cube(3, Cube(1, "R"))
    goals.append(goal)

    # But 2
    goal = Game(n_rods=4, max_rod_size=3)
    goal.add_cube(0, Cube(3, "J"))
    goal.add_cube(0, Cube(2, "J"))
    goal.add_cube(0, Cube(1, "J"))
    goal.add_cube(1, Cube(1, "R"))
    goal.add_cube(1, Cube(2, "R"))
    goal.add_cube(1, Cube(3, "R"))
    goal.add_cube(2, Cube(3, "B"))
    goal.add_cube(2, Cube(2, "B"))
    goal.add_cube(2, Cube(1, "B"))
    goals.append(goal)

    # But 3
    goal = Game(n_rods=4, max_rod_size=3)
    goal.add_cube(0, Cube(3, "J"))
    goal.add_cube(0, Cube(2, "J"))
    goal.add_cube(0, Cube(1, "R"))
    goal.add_cube(1, Cube(3, "B"))
    goal.add_cube(1, Cube(1, "B"))
    goal.add_cube(1, Cube(2, "R"))
    goal.add_cube(2, Cube(3, "R"))
    goal.add_cube(2, Cube(2, "B"))
    goal.add_cube(2, Cube(1, "J"))
    goals.append(goal)

    # But 4
    goal = Game(n_rods=4, max_rod_size=3)
    goal.add_cube(0, Cube(3, "J"))
    goal.add_cube(0, Cube(1, "J"))
    goal.add_cube(0, Cube(2, "J"))
    goal.add_cube(1, Cube(3, "B"))
    goal.add_cube(1, Cube(1, "B"))
    goal.add_cube(1, Cube(2, "B"))
    goal.add_cube(2, Cube(3, "R"))
    goal.add_cube(2, Cube(1, "R"))
    goal.add_cube(2, Cube(2, "R"))
    goals.append(goal)

    # But 5
    goal = Game(n_rods=4, max_rod_size=3)
    goal.add_cube(0, Cube(3, "J"))
    goal.add_cube(0, Cube(2, "J"))
    goal.add_cube(0, Cube(2, "R"))
    goal.add_cube(1, Cube(3, "B"))
    goal.add_cube(1, Cube(1, "B"))
    goal.add_cube(2, Cube(3, "R"))
    goal.add_cube(2, Cube(1, "R"))
    goal.add_cube(2, Cube(2, "B"))
    goal.add_cube(3, Cube(1, "J"))
    goals.append(goal)

    # But 6
    goal = Game(n_rods=4, max_rod_size=3)
    goal.add_cube(0, Cube(1, "B"))
    goal.add_cube(0, Cube(1, "R"))
    goal.add_cube(0, Cube(1, "J"))
    goal.add_cube(1, Cube(2, "B"))
    goal.add_cube(1, Cube(2, "R"))
    goal.add_cube(1, Cube(2, "J"))
    goal.add_cube(2, Cube(3, "B"))
    goal.add_cube(2, Cube(3, "R"))
    goal.add_cube(2, Cube(3, "J"))
    goals.append(goal)

# ----------------------------------------- Génération des valeurs

__generate_initial_situations()
__generate_goals()