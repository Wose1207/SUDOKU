import numpy as np
from math import *

def resolution(grille):
    for i in range(9):
        for j in range(9):
            if grille[i, j]==0:
                grille[i, j]=remplir(i, j, grille)[0]
    return grille


def remplir(i, j, grille):
    "Entrée: i,j(int) grille(ndarray) renvoie le chifre qui va dans la case grille[i,j] ou 0 si aucun ne va"
    sol=[]
    for k in range(1, 10):#On teste tous les nombres possibles dans cette case
        #On va regarder si le nombre k est deja présent dans une ligne/colone/carre
        if AbsLigne(k, i, grille) and AbsCol(k, j, grille) and AbsCar(k, i, j, grille):
            sol.append(k)
    #Toutes les solutions possibles pour cette cases sont donc dans sol
    print(sol)
    if len(sol)==1:
        return sol[0], sol
    else:
        return 0, sol

S=np.array([[0,0,4,6,7,9,8,0,0], [2,6,0,0,0,8,0,0,0], [0,0,0,0,5,0,4,0,0], [9,2,0,0,0,5,1,8,4], [0,4,0,2,0,1,0,9,0], [1,8,6,9,0,0,0,2,5], [0,0,1,0,9,0,0,0,0], [0,0,0,5,0,0,0,4,8], [0,0,3,7,2,4,6,0,0]])

def AbsLigne(k, i, grille):
    for j in range(9):
        if grille[i, j]==k:
            return False
    return True
                    
def AbsCol(k, j, grille):
    for i in range(9):
        if grille[i, j]==k:
            return False
    return True

def AbsCar(k, i, j, grille):
    for g in range(3*(i//3), 3*(i//3)+3):
        for h in range(3*(j//3), 3*(j//3)+3):
            if grille[g, h]==k:
                return False
    return True
