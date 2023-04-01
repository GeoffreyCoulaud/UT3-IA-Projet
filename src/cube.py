from dataclasses import dataclass

@dataclass
class Cube():

    number: int
    color: str

    def __str__(self) -> str:
        return str(self.number) + self.color