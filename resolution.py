import numpy as np
from math import *
from random import *

chiffresPossibles = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def resolution(grille):
    "Entrée: grille(ndarray), Renvoie la grille de sudoku remplie"
    ValeurDansCase(0, grille)#Remplit chaque case du sudoku
    return grille

S=np.array([[0,0,4,6,7,9,8,0,0], [2,6,0,0,0,8,0,0,0], [0,0,0,0,5,0,4,0,0], [9,2,0,0,0,5,1,8,4], [0,4,0,2,0,1,0,9,0], [1,8,6,9,0,0,0,2,5], [0,0,1,0,9,0,0,0,0], [0,0,0,5,0,0,0,4,8], [0,0,3,7,2,4,6,0,0]])

def AbsLigne(k, i, grille):
    "Entrées: k(int), i(int), grille(ndarray), renvoie un boleen qui indique si la valeur k est presente ou non dans la ligne i de la grille"
    for j in range(9):
        if grille[i, j]==k:
            return False
    return True
                    
def AbsCol(k, j, grille):
    "Entrées: k(int), j(int), grille(ndarray), renvoie un boleen qui indique si la valeur k est presente ou non dans la colone j de la grille"
    for i in range(9):
        if grille[i, j]==k:
            return False
    return True

def AbsCar(k, i, j, grille):
    "Entrées: k(int), i(int), j(int), grille(ndarray), renvoie un boleen qui indique si la valeur k est presente ou non dans le carre de la position (i,j) de la grille"
    for g in range(3*(i//3), 3*(i//3)+3):
        for h in range(3*(j//3), 3*(j//3)+3):
            if grille[g, h]==k:
                return False
    return True

def grilleValable(grille):
    "Entrées: grille(ndarray), renvoie un boleen qui indique sur la grille de sudoku est valable ou non"
    somme=45
    #Tous les chiffres de la grille sont entre 1 et 9
    for i in range(9):
        for j in range(9):
            if not(grille[i, j] in chiffresPossibles):
                return False
    #On check les doubles dans les lignes
    for ligne in grille:
        if not(set(ligne).issubset(chiffresPossibles)):
            return False
    #On check les doubles dans les colones
    for colone in range(9):
        if not(set(grille[:, colone]).issubset(chiffresPossibles)):
            return False
    #On check les doubles dans les carres
    for carre in range(9):
        listcarre=[]
        for i in range(carre//3, (carre//3)+3):
            for j in range(carre%3, (carre%3)+3):
                listcarre.append(grille[i, j])
        if not(set(listcarre).issubset(chiffresPossibles)):
            return False
    return True

def ValeurDansCase(i, grille):
    "Entree: i(int), grille(ndarray), remplit la grille par recurrence case par case. On se repere avec i entre 0 et 80 pour les 81 valeurs de la case"
    if i==81:#On est arrive au bout de la grille
        return True
    ligne=i//9
    colone=i%9
    if grille[ligne, colone]!=0:#Si la valeur est 0, cette case reste a remplir. Sinon on teste la case d'apres
        return ValeurDansCase(i+1, grille)
    for nombre in range(1, 10):#On teste les nombres possibles dans cette case
        if AbsCar(nombre, ligne, colone, grille) and AbsCol(nombre, colone, grille) and AbsLigne(nombre, ligne, grille):#On teste la validite du nombre dans cette case
            grille[ligne, colone]=nombre#Si nombre est valide on le teste
            if ValeurDansCase(i+1, grille):#On remplit la case avec nombre pour voir si c'est valide
                return True
    grille[ligne, colone]=0
    return False

def aide(grilleComplete, grilleVide):
    "Entrées: grilleComplete(ndarray), grilleVide(ndarray), renvoie une grille vide avec une valeur de plus que la grille en entrée"
    casesVides=[]
    for ligne in range(9):
        for colone in range(9):
            if grilleVide[ligne, colone]==0:
                casesVides.append((ligne, colone))
    solution=randint(0, len(casesVides)-1)
    print(solution)
    (ligne, colone)=casesVides[solution]
    grilleVide[ligne, colone]=grilleComplete[ligne, colone]
    return grilleVide


def nombreSolution(grille):
    "Entree: grille(ndarray), renvoie le nombre de solution d'une grille de sudoku"
    global nombreSol
    nombreSol=0
    grillesPossibles(0, grille)
    return nombreSol


def grillesPossibles(i, grille):
    "Entree: i(int), decalage(int),grille(ndarray), remplit la grille par recurrence case par case. Puis recommence avec un decalage pour trouver le nombre de solutions de la grille. On se repere avec i entre 0 et 80 pour les 81 valeurs de la case"
    if i==81:#On est arrive au bout de la grille mais on reitere pour retrouver toutes les grilles possibles
        nombreSol+=1
        return True
    ligne=i//9
    colone=i%9
    if grille[ligne, colone]!=0:#Si la valeur est 0, cette case reste a remplir, sinon on teste la case d'apres
        return ValeurDansCase(i+1, grille)
    for nombre in range(1, 10):#On teste les nombres possibles dans cette case
        if AbsCar(nombre, ligne, colone, grille) and AbsCol(nombre, colone, grille) and AbsLigne(nombre, ligne, grille):#On teste la validite du nombre dans cette case
            grille[ligne, colone]=nombre#Si nombre est valide on le teste
            if ValeurDansCase(i+1, grille):#On remplit la case avec nombre pour voir si c'est valide
                return True
    grille[ligne, colone]=0
    return False