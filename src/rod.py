from custom_collections import BoundedStack


class Rod(BoundedStack):
    """
    Classe qui représente une pique du jeu.
    
    Les cubes sont stockés dans une Pile/LIFO où le "dessous" est l'index 0.   
    On ajoute donc des cubes à la fin de la liste des cubes.
    """

    number: int

    def __init__(self, number: int, max_size: int = 3) -> None:
        self.number = number
        super().__init__(max_size)

    def __eq__(self, other) -> bool:
        """Deux piques sont égales si elles ont les mêmes cubes au même endroit"""
        if len(self) != len(other):
            return False
        for (a, b) in zip(self, other):
            if a != b:
                return False
        return True