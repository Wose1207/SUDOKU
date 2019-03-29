from random import *
import numpy as np
from tkinter import *
import time


# TP SUDOKU

# Petits Outils :

def CoordSouris(event):    # Me donne les coordonées de la souris
    X= event.x
    Y= event.y
    return (X,Y)
    
def nametouche():          # Pour voir les touches tkinter  ( a mettre dans la colonne outil )
    main2=Tk()    
    def clavier(event):
        touche=event.keysym
        Label21=Label(main2,text=touche,fg='black')
        Label21.pack()        
    canvas2=Canvas(main2,width=500,height=100)
    canvas2.focus_set()
    canvas2.bind("<Key>",clavier)
    canvas2.pack()
    canvas2.create_text(250,50,text='Pressez une touche pour voir son nom Tkinter')
    main2.mainloop()
    


## Création d'une grille de Sudoku


def grille():
    " Cette fonction renvoie une grille pleine qui verifie nos contraintes en un temps vraiment petit . J'utilise beaucoup de variable et de copy car j'ai besoin de limiter le nombre d'essaies et de garder en memoire un tableau et une liste fixé."
        
    List=[(x,y) for x in range(9) for y in range(9)]             # Liste qui ma me servir d'appuie pour la suite
    conteur=0                                          
    
    while True: 
        M=np.array([[0 for k in range(9)] for k in range(9)])    # Voici ma matrice
        ListGlobal=List.copy()
                                                                 # La list globale est la liste qui va marquer les positions libres de la matrice
        for k in range(9):
                                                                 # Je cale les 1, puis les 2, puis les 3 ...
            conteuressaie =0                 
            while conteur <9:                                    # Je ne passe cette condition qui si mes neufs 1 sont placés dans mon tableau ( idem pour 2,3,...)
                Mbis=M.copy()                                    # J'ai besoin de cette manip car je dois garder en memoire ma matrice si jamais cela ne marche pas
                conteur=0
                L=ListGlobal.copy()                              # L est la listes des positions autorisés de mes chiffres, != de LG
                LG=ListGlobal.copy()                             # LG est la liste globale appliqué a cette boucle, qui garde les emplacements libres du tableaux
                
                for i in range(9):                               # Je cale 9 fois le chiffre, et je m'arrete s'il n'y a pas d'emplacement autorisé
                    if len(L)!=0:
                        (x,y)=L[randint(0,len(L)-1)]
                        for l in range(9):
                            if (l,y) in L:
                                L.remove((l,y))
                            if (x,l) in L:
                                L.remove((x,l))
                        for a in range(3):
                            for b in range(3):
                                if (a+3*(x//3),b+3*(y//3)) in L:
                                    L.remove((a+3*(x//3),b+3*(y//3)))
                        
                        LG.remove((x,y))
                        conteur+=1
                        Mbis[x,y]=k+1
                conteuressaie+=1
                if conteuressaie>=20:                           # je ne laisse que 20 essaie, sinon cela laisse des zéros et ca recommence
                    conteur=9
                    
            conteur=0
            conteuressaie
            M=Mbis.copy()                                       # A chaque étape, je actualise mon tableaux et ma liste globale pour continuer
            ListGlobal=LG.copy()
            
        if 0 not in M:                                          # Je verifie que le tableau soit entierment remplie pour l'utiliser !
            return M
        

def grilleTores(niveau):
    "grille to resolve, entrez en arguments le niveau de jeu : (child : 1 ) (easy : 2) (middle : 3) (hard : 4) (diabbolic : 5)"
    
    assert niveau in [1,2,3,4,5]
    l=[70,40,32,26,20]
    List=[(x,y) for x in range(9) for y in range(9)]
    
    M=grille()
    Mj=M.copy()
    for i in range(81-l[niveau-1]):
        (x,y)=List[randint(0,len(List)-1)]
        List.remove((x,y))
        Mj[x,y]=0
    return Mj,M
     
     
## Affichage et Platforme de jeu
    
     
def AffgrilleComplete(M=grille()):
    " Affiche une grille complète , ce trouve dans les outils "
    mainG=Tk()
    mainG.geometry('740x740+200+200')
    can=Canvas(mainG,height=740,width=740)
    can.pack()
    
    # Création de la grille
    cx=10
    for i in range(10):
        if i%3==0:
            couleur='red'
        else:
            couleur='black'
        can.create_line(10,cx,730,cx,fill=couleur)
        can.create_line(cx,10,cx,730,fill=couleur)
        cx+=80
    # Impression du tableau
    for i in range(9):
        for j in range(9):
            can.create_text(50+i*80,50+j*80,text=str(M[i,j]),font='Arial 20')
    mainG.mainloop()



    
def AffgrilleJeu(tuple,motif):
    " Affiche la grille de jeu , pour jouer, clicker sur les cases et appuyer sur un chiffre. En entree (la matrice de jeu, la matrcie entière) et le motif de curseur"
    
    # Configuration de la fenètre et quelques variables
    
    mainG=Tk()
    mainG.geometry('740x820+200+200')
    can=Canvas(mainG,height=740,width=740,cursor=motif)
    can.pack()
    can.focus_set()
    Button(mainG,text='Effacer',command=mainG.destroy,height=5,width=15).pack(side=LEFT,padx=5,pady=5)
    
    Mjeu=tuple[0]                   # Mjeu est la matrice de jeu support  ( Utiliser pour pouvoir effacer Mj)
    Mj=Mjeu.copy()                  # Mj est la matrice de jeu variable
    M=tuple[1]                      # M est la matrice complete garder en memoire pour la verification
    PositionVide=[]
    
    """
    def chrono():
        global t
        t+=1
        T.set(t)
        mainG.after(1000,chrono)
    t=0
    T=StringVar()
    Label(mainG,textvariable=T).pack(padx=10,pady=10)
    chrono()
    """
    
    # Création de la grille
    cx=10
    for i in range(10):
        if i%3==0:
            couleur='red'
        else:
            couleur='black'
        can.create_line(10,cx,730,cx,fill=couleur)
        can.create_line(cx,10,cx,730,fill=couleur)
        cx+=80
        
    # Impression du tableau Et insertion des chiffres
            
    for i in range(9):
        for j in range(9):
            if Mj[i,j]!=0:
                can.create_text(50+i*80,50+j*80,text=str(Mj[i,j]),font='Arial 20')
            else:
                PositionVide.append((i,j))
                
    def InsertionChiffre(event):
        #print(PositionVide)
        (i,j)=(CoordSouris(event)[0]//80,CoordSouris(event)[1]//80)
            
        def Chiffre(event2):
            if (i,j) in PositionVide:
                touche=event2.keysym
                if touche in ('1','2','3','4','5','6','7','8','9'):
                    PositionVide.remove((i,j))
                    Mj[i,j]=int(touche)
                    can.create_text(50+i*80,50+j*80,text=touche,font='Arial 20')
        can.bind("<Key>",Chiffre)
        
    # Vérification et solution
    
    def Verif():
        if Mj.all()==M.all():
            can.create_text(370,370,text='BRAVO !!',font='Arial 70 bold',fill='yellow')
            can.create_text(370,470,text='appuyer sur la croix pour sortir',font='Arial 20',fill='yellow')
        
    Button(mainG,text='Verifier',command=Verif,height=5,width=15).pack(side=RIGHT,padx=5,pady=5)

        
    can.bind("<Button-1>",InsertionChiffre)
    mainG.mainloop()
    
def AffgrilleJeuNiv1():
    return AffgrilleJeu(grilleTores(1),'heart')
def AffgrilleJeuNiv2():
    return AffgrilleJeu(grilleTores(2),'spraycan')
def AffgrilleJeuNiv3():
    return AffgrilleJeu(grilleTores(3),'pirate')
def AffgrilleJeuNiv4():
    return AffgrilleJeu(grilleTores(4),'spider')
def AffgrilleJeuNiv5():
    return AffgrilleJeu(grilleTores(5),'star')
    
     
def jeu():
    " Affiche la plateforme de jeu, ainsi que de nombreux outils "
    main=Tk()
    main['cursor']='trek'
    main.title('Les jolis Sodokus de Waxel ')
    main.geometry('600x600+200+200')
    main['bg']='white'
    canvas=Canvas(main,height=500,width=600,bg='white')
    
    photo=PhotoImage(file='C:/Users/Axel/Desktop/homer2.png')
    canvas.create_image(300,140,image=photo)
    
    canvas.pack()
    
    # Configuration de la bar menu superieur
    menubar=Menu(main)
    menu1=Menu(menubar)
    menu1.add_command(label="Grille Complète",command=AffgrilleComplete)
    menu1.add_separator()
    menu1.add_command(label="Touches Tkinter",command=nametouche)
    menu2=Menu(menubar)
    menu2.add_command(label="Quitter le jeu",command=main.destroy)
    menu2.add_command(label="A propos",command=main.destroy)
    menubar.add_cascade(label="Outils",menu=menu1)
    menubar.add_cascade(label="Aide",menu=menu2)
    main.config(menu=menubar)
    
    # Configuration des boutons pour jouer et presentation
    
    canvas.create_text(300,300,text='Bienvenue ! Hakuna Matata a vous !',font='Arial 10')
    canvas.create_text(300,340,text='Pour jouer , Clickez sur votre niveau de Jeu : ',font='Arial 10')
    canvas.create_text(300,380,text='Durant le jeu , Clickez sur une case pour mettre un chiffre .',font='Arial 8')
    canvas.create_text(300,400,text='A la fin , Verifiez votre grille ou effacez la pour revenir au début .',font='Arial 8')
    canvas.create_text(300,450,text='( Regardez les curseurs, une magnificiance ! )',font='Arial 8')
    
    Button1=Button(main,text='Quadripède',font='Arial 9 bold',command=AffgrilleJeuNiv1,bg='pink',cursor='heart',height=3,width=10,relief='groove')
    Button1.pack(side=LEFT,padx=10,pady=10)
    Button2=Button(main,text='Débutant',font='Arial 9 bold',command=AffgrilleJeuNiv2,bg='green',cursor='spraycan',height=3,width=10,relief='groove')
    Button2.pack(side=LEFT,padx=10,pady=10)
    Button3=Button(main,text='Apprentis',font='Arial 9 bold',command=AffgrilleJeuNiv3,bg='yellow',cursor='pirate',height=3,width=10,relief='groove')
    Button3.pack(side=LEFT,padx=10,pady=10)
    Button4=Button(main,text='Maître',font='Arial 9 bold',command=AffgrilleJeuNiv4,bg='orange',cursor='spider',height=3,width=10,relief='groove')
    Button4.pack(side=LEFT,padx=10,pady=10)
    Button5=Button(main,text='Demi-Dieu',font='Arial 9 bold',command=AffgrilleJeuNiv5,bg='red',cursor='star',height=3,width=10,relief='groove')
    Button5.pack(side=LEFT,padx=10,pady=10)
    
    main.mainloop()
    

jeu()
    
    
    