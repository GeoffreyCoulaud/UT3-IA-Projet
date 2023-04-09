from rod import Rod
from cube import Cube
from typing import MutableSequence

class Etat():
    #cubes: MutableSequence[Cube]
    piques : MutableSequence[Rod]
    listPique : MutableSequence[piques]

    def getPique(self, numeroP: int) -> Rod:
        return self.piques[numeroP]

    # def get_size(self) -> int:
    #     """Obtenir le nombre de cubes dans la pique"""
    #     return len(self.cubes)

    def ajouterCube(self,cube : Cube):
        self.cubes.append(cube)

    def lenEtat(self) ->int:
        return len(self.listPique)

