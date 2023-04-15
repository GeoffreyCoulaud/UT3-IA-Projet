from dataclasses import dataclass


@dataclass
class Move():
    """Classe représentant un déplacement d'une tige à une autre"""

    source: int
    destination: int

    def __str__(self):
        return f"{self.source} → {self.destination}"