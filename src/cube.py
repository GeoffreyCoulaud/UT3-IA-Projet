from dataclasses import dataclass

@dataclass
class Cube():

    color: str
    number: int

    def __str__(self) -> str:
        return str(self.number) + self.color