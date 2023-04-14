from dataclasses import dataclass

@dataclass
class Cube():
    """Classe représentant un cube de jeu avec un numéro et une couleur"""

    number: int
    color: str

    def __str__(self) -> str:
        return str(self.number) + self.color
    
    def __eq__(self, other) -> bool:
        return (self.number == other.number) and (self.color == other.color)