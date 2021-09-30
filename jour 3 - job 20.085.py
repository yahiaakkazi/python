import numpy as np

def asser(tableau):
    for i in tableau:
        s=0
        t=0
        for j in i:
            if j=="R":
                s=s+1
            if s==4:
                return("Le rouge a gagné")
            if j=="J":
                t=t+1
            if t==4:
                return("Le jaune a gagné")
    for i in tableau.T:
        s=0
        t=0
        for j in i:
            if j=="R":
                s=s+1
            if s==4:
                return("Le rouge a gagné")
            if j=="J":
                t=t+1
            if t==4:
                return("Le jaune a gagné")
class Board:
    def __init__(self,entier_i,entier_j):
        self.i=entier_i
        self.j=entier_j
        self.tableau=np.array(self.i*[self.j*["O"]])

    def play(self,nombre,chaine):
        self.chaine=chaine
        assert chaine in ["R","J"]
        s=self.i-1
        while self.tableau[s][nombre-1] in ['R','J']:
            s=s-1
        self.tableau[s][nombre-1]=chaine
        print(self.tableau)
        return(asser(self.tableau))

    def print(self):
        print(self.tableau)
        return(self.tableau)
