from dataclasses import dataclass


@dataclass
class Move():
    """Classe représentant un déplacement d'une tige à une autre"""

    source: int
    destination: int