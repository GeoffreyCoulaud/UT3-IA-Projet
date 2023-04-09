from typing import Sequence, Callable
from xmlrpc.client import Boolean
from etat import Etat
import copy

from game import Game
from move import Move
from rod  import Rod
from etat import Etat


class IDAStar():

    init: Game
    is_goal: Callable[[Game], bool] # Fonction qui renvoie vraie si l'état donné est un but
    get_state_chidren: Callable[[Game], Sequence[Game]] # Fonction qui renvoie les états fils d'un état
    get_state_heuristic: Callable[[Game], int] # Fonction heuristique d'un état

    threshold: int # Seuil actuel
    etatBut : Etat

    def __init__(
        self, 
        init: Game, 
        is_goal: Callable[[Game], bool],
        get_state_chidren: Callable[[Game], Sequence[Game]],
        get_state_heuristic: Callable[[Game], int]
    ) -> None:
        """Mettre en place le solveur IDA*"""
        self.init = init
        self.is_goal = is_goal
        self.get_state_chidren = get_state_chidren
        self.get_state_heuristic = get_state_heuristic
        

    def find_solution(self) -> list[Move]:
        """Trouver une liste de déplacements pour arriver à un état but. Si impossible, une liste vide de déplacements."""
        
        # Seuil initial = heuristique de l'état initial
        self.threshold = self.get_state_heuristic(self.init)
        
        # TODO implémenter + fonctions intermédiaires
        pass
    
    #j'ai du mal avec des variables en anglais donc je vais devoir coder avec le français :)

    def trouverDestination(etat:Etat, piqueI:Rod) ->list[Rod]:
        PiquesDestinataires = []
        for i in range(len(Rod)):
            if i!= piqueI and len(etat.getPique(i)) < Rod.get_size():
                PiquesDestinataires.append(i)
        return PiquesDestinataires


    def deplacer(etat:Etat, numP1: int, numP2: int) ->Etat:
        etatCopie = copy.deepcopy(etat)
        if len(etat.piques[numP1])==0 :
            return None
        etatCopie.piques[numP2].put(etatCopie.piques[1].pop())

        return etatCopie


    def estBut(etat:Etat, etatBut: Etat) ->Boolean:
        return egal(etat)
    
    def egal(self,etat: Etat) -> Boolean:
        return etat == self.etatBut


    def nombreMalMis(self,etat: Etat) ->int:
        nbMalPlaces = 0
        for i in range(etat.lenEtat(etat)):
            if len(etat.listPique[i]) == len(self.etatBut.listPique[i]):
                for j in range(self.etatBut.lenEtat(self.etatBut)):
                    if j >= etat.lenEtat(etat) or etat.piques[i][j]!= self.etatBut.piques[i][j]:
                        nbMalPlaces +=1
            else:
                for j in range(-1, -self.etatBut.lenEtat(self.etatBut)-1, -1):
                    if -j-1 >= etat.lenEtat(etat) or etat.piques[i][j]!= self.etatBut.piques[i][j]:
                        nbMalPlaces +=1


