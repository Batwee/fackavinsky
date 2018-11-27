from random import *
from tkinter import *
from time import *


#|||| Initialisation du jeu ||||#

def fichier_score():
    aux=open('score.txt','a') #crée score.txt dans le même fichier que le jeu
    aux.write('') # n'écrit rien à l'interieur du fichier
    aux.close() # ferme le fichier
    if(len(open("score.txt","r").readlines())==0): # regarde si le fichier est vide et qu'il n'y a rien écrit dedans
        aux=open("score.txt","a") # ouvre le fichier
        aux.write("0") # écrit 0 pour dire que le meilleur score n'a pas été fait
        aux.close() # ferme le fichier
        
    
    
def nouvelle_partie():
    global cote,xd,yd,lignes,score,fini
    lignes=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #remet à zero de la liste de départ (#|||| ProgrammeTkinter ||||#) 
    cote,xd,yd=100,25,25 #remet à zero les valeurs du damier : du cote et de xd,yd (#|||| ProgrammeTkinter ||||#)
    fini=False
    can.delete(ALL) #supprime tous ce qui s'affiche sur dans le canevas
    damier() # recrée le terrain de jeu 2048
    poser_une_case() #repose une premiere case sur le terrain de jeu
    poser_une_case() #repose une deuxieme case sur le terrain de jeu
    score=0 #remet le score à 0


#|||| Construction de la table de jeu ||||#
	
def carre():
                                             #Dessine un carré dont le coin supérieur gauche est repéré par xd,yd
    global cote,xd,yd            
    can.create_rectangle(xd,yd,xd+cote,yd+cote,fill='#CDC1B4',width=10,outline='#BBADA0')#Couleur bordure et interieur du damier

def ligne():                                 #Dessine une ligne dont le premier carré est repéré par xd,yd
    global cote,xd,yd
    n=1                                      #n est le nombre de carrés (4)
    while n<=4:
        carre()
        xd=xd+cote
        n+=1

def damier():                                #Dessine le damier
    global xd,yd,cote
    n=1
    while n<=4:                              #n est le nombre de lignes (4)
        ligne()
        yd=yd+cote
        xd=25
        n+=1



#|||| Fonctions du jeu ||||# 

def creer_une_piece(x,y,nombre):            #case 2 4 8 16 32 64 128 256 512 1024 2048 en x et y
    if(nombre==2):
        can.create_rectangle(x,y,x+90,y+90, fill="#eee4da", outline="#eee4da") # brodure de même couleur que la case
        can.create_text(x+45,y+45,text="2",font="Arial 40",fill="#776e65") # couleur et police de la case
    if(nombre==4):
        can.create_rectangle(x,y,x+90,y+90, fill="#ede0c8", outline="#ede0c8")
        can.create_text(x+45,y+45,text="4",font="Arial 40",fill="#776e65")
    if(nombre==8):
        can.create_rectangle(x,y,x+90,y+90, fill="#f2b179", outline="#f2b179")
        can.create_text(x+45,y+45,text="8",font="Arial 40",fill="white")
    if(nombre==16):
        can.create_rectangle(x,y,x+90,y+90, fill="#f59563", outline="#f59563")
        can.create_text(x+45,y+45,text="16",font="Arial 40",fill="white")
    if(nombre==32):
        can.create_rectangle(x,y,x+90,y+90, fill="#f67c5f", outline="#f67c5f")
        can.create_text(x+45,y+45,text="32",font="Arial 40",fill="white")
    if(nombre==64):
        can.create_rectangle(x,y,x+90,y+90, fill="#f65e3b", outline="#f65e3b")
        can.create_text(x+45,y+45,text="64",font="Arial 40",fill="white")
    if(nombre==128):
        can.create_rectangle(x,y,x+90,y+90, fill="#edcf72", outline="#edcf72")
        can.create_text(x+45,y+45,text="128",font="Arial 30",fill="white")
    if(nombre==256):
        can.create_rectangle(x,y,x+90,y+90, fill="#edcc61", outline="#edcc61")
        can.create_text(x+45,y+45,text="256",font="Arial 30",fill="white")
    if(nombre==512):
        can.create_rectangle(x,y,x+90,y+90, fill="#edc850", outline="#edc850")
        can.create_text(x+45,y+45,text="512",font="Arial 30",fill="white")
    if(nombre==1024):
        can.create_rectangle(x,y,x+90,y+90, fill="#edc53f", outline="#edc53f")
        can.create_text(x+45,y+45,text="1024",font="Arial 20",fill="white")
    if(nombre==2048):
        can.create_rectangle(x,y,x+90,y+90, fill="#edc22e", outline="#edc22e")
        can.create_text(x+45,y+45,text="2048",font="Arial 20",fill="white")
        fen.after(1000,fini) # après 1000 ms la fontion fini est executée
        

def fini():
    can.create_rectangle(30,30,420,420, fill='#edc53f')  # fait apparaitre une fenêtre de Victoire
    can.create_text(230,230,text="Gagné", font="Arial 75",fill="#f67c5f") # avec écrit gagné à l'interieur
        
 


def verifier_une_case(i):
    verifier_ligne=int((i-1)/4) # Retourne l'index qui va de 0 à 3 de la ligne à vérifier
    if(lignes[verifier_ligne][(i%4)-1]==0): # Pour la ligne vérifié on teste la colonne
        return True
    else:
        return False


def poser_une_case():
    import random
    global lignes
    i = randint(1,16) #aléatoire de 1 à 16 (nombre de case sur le jeu)
                      #qui permet de faire apparaitre une pièce aléatoirement sur l'une des 16 cases

    r = randint(1,100) # le pourcentage aléatoire qui permet de faire apparaitre un 2 ou un 4

    while(verifier_une_case(i)==False): #  
        i = randint(1,16)
    if i==1:
        
        if r<=90:
            creer_une_piece(30,30,2) #pose une case en position A1 de valeur 2 avec 90% de chance
            lignes[0][0]=2 # place le 2 au bon positionnement dans la liste
        else:
            creer_une_piece(30,30,4) #pose une case en position A1 de valeur 4 avec 10% de chance
            lignes[0][0]=4 # place le 4 au bon positionnement dans la liste
    elif i==2:
        
        if r<=90:
            creer_une_piece(130,30,2) #pose une case en position A2 de valeur 2 avec 90% de chance
            lignes[0][1]=2
        else:
            creer_une_piece(130,30,4)  #pose une case en position A2 de valeur 4 avec 10% de chance
            lignes[0][1]=4
    elif i==3:
        
        if r<=90:
            creer_une_piece(230,30,2) #pose une case en position A3 de valeur 2 avec 90% de chance
            lignes[0][2]=2
        else:
            creer_une_piece(230,30,4) #pose une case en position A3 de valeur 4 avec 10% de chance
            lignes[0][2]=4
    elif i==4:
       
        if r<=90:
            creer_une_piece(330,30,2) #pose une case en position A4 de valeur 2 avec 90% de chance
            lignes[0][3]=2
        else:
            creer_une_piece(330,30,4)  #pose une case en position A4 de valeur 4 avec 10% de chance
            lignes[0][3]=4
    elif i==5:
        
        if r<=90:
            creer_une_piece(30,130,2) #pose une case en position B1 de valeur 2 avec 90% de chance
            lignes[1][0]=2
        else:
            creer_une_piece(30,130,4) #pose une case en position B1 de valeur 4 avec 10% de chance
            lignes[1][0]=4
    elif i==6:
        
        if r<=90:
            creer_une_piece(130,130,2)  #pose une case en position B2 de valeur 2 avec 90% de chance
            lignes[1][1]=2
        else:
            creer_une_piece(130,130,4) #pose une case en position B2 de valeur 4 avec 10% de chance
            lignes[1][1]=4
    elif i==7:
        
        if r<=90:
            creer_une_piece(230,130,2) #pose une case en position B3 de valeur 2 avec 90% de chance
            lignes[1][2]=2
        else:
            creer_une_piece(230,130,4)  #pose une case en position B3 de valeur 4 avec 10% de chance
            lignes[1][2]=4
    elif i==8:
        
        if r<=90:
            creer_une_piece(330,130,2)  #pose une case en position B4 de valeur 2 avec 90% de chance
            lignes[1][3]=2
        else:
            creer_une_piece(330,130,4) #pose une case en position B4 de valeur 4 avec 10% de chance
            lignes[1][3]=4
    elif i==9:
        
        if r<=90:
            creer_une_piece(30,230,2)  #pose une case en position C1 de valeur 2 avec 90% de chance
            lignes[2][0]=2
        else:
            creer_une_piece(30,230,4)  #pose une case en position C1 de valeur 4 avec 10% de chance
            lignes[2][0]=4
    elif i==10:
        
        if r<=90:
            creer_une_piece(130,230,2)  #pose une case en position C2 de valeur 2 avec 90% de chance
            lignes[2][1]=2
        else:
            creer_une_piece(130,230,4)  #pose une case en position C2 de valeur 4 avec 10% de chance
            lignes[2][1]=4
    elif i==11:
        
        if r<=90:
            creer_une_piece(230,230,2)  #pose une case en position C3 de valeur 2 avec 90% de chance
            lignes[2][2]=2
        else:
            creer_une_piece(230,230,4)  #pose une case en position C3 de valeur 4 avec 10% de chance
            lignes[2][2]=4
    elif i==12:
        
        if r<=90:
            creer_une_piece(330,230,2)  #pose une case en position C4 de valeur 2 avec 90% de chance
            lignes[2][3]=2
        else:
            creer_une_piece(330,230,4)  #pose une case en position C4 de valeur 4 avec 10% de chance
            lignes[2][3]=4
    elif i==13:
        
        if r<=90:
            creer_une_piece(30,330,2)  #pose une case en position D1 de valeur 2 avec 90% de chance
            lignes[3][0]=2
        else:
            creer_une_piece(30,330,4)  #pose une case en position D1 de valeur 4 avec 10% de chance
            lignes[3][0]=4
    elif i==14:
        
        if r<=90:
            creer_une_piece(130,330,2)  #pose une case en position D2 de valeur 2 avec 90% de chance
            lignes[3][1]=2
        else:
            creer_une_piece(130,330,4)  #pose une case en position D2 de valeur 4 avec 10% de chance
            lignes[3][1]=4
    elif i==15:
        
        if r<=90:
            creer_une_piece(230,330,2)  #pose une case en position D3 de valeur 2 avec 90% de chance
            lignes[3][2]=2
        else:
            creer_une_piece(230,330,4)  #pose une case en position D3 de valeur 4 avec 10% de chance
            lignes[3][2]=4
    elif i==16:
        if r<=90:
            creer_une_piece(330,330,2)  #pose une case en position D4 de valeur 2 avec 90% de chance
            lignes[3][3]=2
        else:
            creer_une_piece(330,330,4)  #pose une case en position D4 de valeur 4 avec 10% de chance
            lignes[3][3]=4
    


def update_score():
    global score,record,fini
    can.delete("score") #supprime l'ancien score pour affiché la nouvelle valeur
    can.create_text(230,480,text="Score : "+str(score), font=('Arial 20'), tags="score", fill='#BBADA0') # nouvelle valeur du score (actualise le score à l'écran)
    if(score<int(open("score.txt","r").readlines()[0])): # compare la valeur du score actuel avec celle dans le score.txt 
        record=(open("score.txt","r").readlines()[0]) # enregistre la valeur dans la variable record
    else:
        record=score  # le score va s'actualiser en même temps que le record car il est égal
        aux=open("score.txt","w") 
        aux.write(str(score)) # écrit la valeur du record dans le score.txt
        aux.close() 
    can.create_text(230,510,text="Record : "+str(record), font=('Arial 20'), tags="score", fill='red') #Met le texte en dessous du score sur le terrain de jeu
    
def move(direction,a,a_bouge): # direction=(up/down/left/right) a=(0/1/2/3) a_bouge=(True/False)
    global score,fini
    if(a==3 and a_bouge==True): # les trois mouvements posibles ont été effectué sachant que l'on a bien bougé
        
        poser_une_case() # une case apparait
        update_score() # et réactualise le score

    elif(direction=="up" and a<3):#  on appuie sur up sachant que la valeur du a est inferieur à 3 ( a : nombre de mouvements possibles)
        
        for i in range(1,4): # nombre de lignes possibles à déplacer pour le up (1à3 pour une liste qui correspond à la ligne 2 à la ligne 4)
            for j in range(0,4): # nombre de colonnes possibles à déplacer pour le up (0à3 pour une liste qui correspond à la ligne 1 à la ligne 4)
                if(lignes[i-1][j]==0 and lignes[i][j]!=0): # si la case en question([i][j]) n'est pas vide et que la case de haut dessus est vide alors le mouvement est possible 
                    items = can.find_overlapping(40+100*j,40+100*i,110+100*j,110+100*i) # met dans une variable les coordonnées trouvées par le overlapping de 1 à 16 détecté sur le terrain (position + valeur)
                    print(can.find_overlapping(40+100*j,40+100*i,110+100*j,110+100*i))# la premier coordonnée correspond à son emplacement
                    lignes[i-1][j]=lignes[i][j] #la pièce en question monte d'une case
                    lignes[i][j]=0 # supprime l'ancienne pièce dans la liste
                    for c in range(1,3):
                        can.move(items[c],0,-100) # fait le mouvement sur le terrain de 100 vers le haut
                    a_bouge=True # dit qu'il y eu un mouvement
                if(lignes[i-1][j]==lignes[i][j] and lignes[i-1][j]!=0): # vérifie si un fusionnement est possible avec la case de haut dessus
                    items = can.find_overlapping(40+100*j,40+100*i,110+100*j,110+100*i) # redétecte les pièces sur le terrain
                    print(items)
                    for c in range(1,3):
                        can.delete(items[c])# supprime la pièce en question sur le terrain
                    lignes[i-1][j]=(lignes[i-1][j])*2 # multiplie par 2 la pièce au dessus
                    score+=lignes[i-1][j] # le score ajoute à chaque fois le résultat du fusionnement de deux cases
                    lignes[i][j]=0 # supprime la pièce dans la liste (car elle est montée d'une case)
                    items = can.find_overlapping(40+100*j,40+100*(i-1),110+100*j,110+100*(i-1))
                    print(items)
                    print(lignes)
                    
                    for c in range(1,3):
                        can.delete(items[c]) #supprime la pièce en question sur le terrain
                    creer_une_piece(30+100*j,30+100*(i-1),lignes[i-1][j]) #Crée une pièce qui a bougé vers le haut de 100 (monter d'un ligne)
                    a_bouge=True #dit qu'il y a eu un mouvement

        move(direction,a+1,a_bouge) # on fait a+1 car un mouvement à été fait

    elif(direction=="down" and a<3): #même principe avec mouvement vers le bas
        for i in range(2,-1,-1):
            for j in range(0,4):
                if(lignes[i+1][j]==0 and lignes[i][j]!=0): 
                    items = can.find_overlapping(40+100*j,40+100*i,110+100*j,110+100*i)
                    lignes[i+1][j]=lignes[i][j]
                    lignes[i][j]=0
                    for c in range(1,3):
                        can.move(items[c],0,100)
                    a_bouge=True
                if(lignes[i+1][j]==lignes[i][j] and lignes[i+1][j]!=0):
                    items = can.find_overlapping(40+100*j,40+100*i,110+100*j,110+100*i)
                    print(items)
                    for c in range(1,3):
                        can.delete(items[c])
                    lignes[i+1][j]=(lignes[i+1][j])*2
                    score+=lignes[i+1][j]
                    lignes[i][j]=0
                    items = can.find_overlapping(40+100*j,40+100*(i+1),110+100*j,110+100*(i+1))
                    print(items)
                    print(lignes)
                    for c in range(1,3):
                        can.delete(items[c])
                    creer_une_piece(30+100*j,30+100*(i+1),lignes[i+1][j])
                    a_bouge=True

        move(direction,a+1,a_bouge) # on fait a+1 car un mouvement à été fait

    elif(direction=="right" and a<3): #même principe avec un mouvement vers la droite
        for i in range(0,4):
            for j in range(2,-1,-1):
                if(lignes[i][j+1]==0 and lignes[i][j]!=0):
                    items = can.find_overlapping(40+100*j,40+100*i,110+100*j,110+100*i)
                    lignes[i][j+1]=lignes[i][j]
                    lignes[i][j]=0
                    for c in range(1,3):
                        can.move(items[c],100,0)
                    a_bouge=True
                if(lignes[i][j+1]==lignes[i][j] and lignes[i][j+1]!=0):
                    items = can.find_overlapping(40+100*j,40+100*i,110+100*j,110+100*i)
                    for c in range(1,3):
                        can.delete(items[c])
                    lignes[i][j+1]=(lignes[i][j+1])*2
                    score+=lignes[i][j+1]
                    lignes[i][j]=0
                    items = can.find_overlapping(40+100*(j+1),40+100*i,110+100*(j+1),110+100*i)
                    print(items)
                    print(lignes)
                    for c in range(1,3):
                        can.delete(items[c])
                    creer_une_piece(30+100*(j+1),30+100*i,lignes[i][j+1])
                    a_bouge=True

        move(direction,a+1,a_bouge)  # on fait a+1 car un mouvement à été fait     

    elif(direction=="left" and a<3): #même principe avec un mouvement vers la gauche
        for i in range(0,4):
            for j in range(1,4):
                if(lignes[i][j-1]==0 and lignes[i][j]!=0):
                    items = can.find_overlapping(40+100*j,40+100*i,110+100*j,110+100*i)
                    lignes[i][j-1]=lignes[i][j]
                    lignes[i][j]=0
                    for c in range(1,3):
                        can.move(items[c],-100,0)
                    a_bouge=True
                if(lignes[i][j-1]==lignes[i][j] and lignes[i][j-1]!=0):
                    items = can.find_overlapping(40+100*j,40+100*i,110+100*j,110+100*i)
                    for c in range(1,3):
                        can.delete(items[c])
                    lignes[i][j-1]=(lignes[i][j-1])*2
                    score+=lignes[i][j-1]
                    lignes[i][j]=0
                    items = can.find_overlapping(40+100*(j-1),40+100*i,110+100*(j-1),110+100*i)
                    print(items)
                    print(lignes)
                    for c in range(1,3):
                        can.delete(items[c])
                    creer_une_piece(30+100*(j-1),30+100*i,lignes[i][j-1])
                    a_bouge=True
                    
        move(direction,a+1,a_bouge) # on fait a+1 car un mouvement à été fait 
    
    elif(a_bouge==False):
        for i in range(1,3): 
            for j in range(1,3): 
                if(lignes[i][j-1]!=lignes[i][j] and lignes[i][j+1]!=lignes[i][j] and lignes[i+1][j]!=lignes[i][j] and lignes[i-1][j]!=lignes[i][j] and lignes[i][j]!=0 and lignes[i][j-1]!=0 and lignes[i][j+1]!=0 and lignes[i-1][j]!=0 and lignes[i+1][j]!=0):
                    can.create_rectangle(30,30,420,420, fill="#f67c5f")  # Le problème de cette fonction est que la valeur du i et du j est plus grande que la liste (out of range)
                    can.create_text(230,230,text="Loose", font="Arial 40",fill="#edc53f")
                    fini=True
        

            
def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """   
    global fini

    touche = event.keysym # associe à la variable touche les touches directionnelles du clavier
    print(touche)
    a_bouge=False #aucun mouvement n'a été fait
    
    # déplacement vers le haut
    if (touche == 'Up' and fini==False): #pour ne pas faire bouger le terrain quand la partie est perdue
        move("up",0,a_bouge) # a=0 car aucun mouvement n'a été fait

    # déplacement vers le bas
    if (touche == 'Down' and fini==False):
        move("down",0,a_bouge)

    # déplacement vers la droite
    if (touche == 'Right' and fini==False):
        move("right",0,a_bouge)
        
        
    # déplacement vers la gauche
    if (touche == 'Left' and fini==False):
        move("left",0,a_bouge)
        
        
    
    



#|||| ProgrammeTkinter ||||#

 
lignes=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]  #Liste qui permet de situer une pièce
    #    A1A2A3A4  B1B2B3B4  C1C2C3C4  D1D2D3D4


# Met toute les variables à zéro
record=0
fini=False
score=0
cote,xd,yd=100,25,25
fen=Tk()
fen.title('2048')
fen.wm_state(newstate="zoomed")

can=Canvas(fen,bg='#FAF8EF',width=445,height=545)# taille (longeur/largeur) et couleur d'arriere fond de la fenetre
can.pack()

bouton = Button(fen, text="Nouvelle partie", command=nouvelle_partie, fg='#edc53f') # bouton nouvelle
bouton.pack()


bou1 = Button(fen,text='Quitter',command=fen.quit,fg='#f65e3b')# bouton quitter
bou1.pack()


fichier_score()
 
damier()  #  1°


poser_une_case()  #  2° pose une première case sur le terrain de jeu
poser_une_case()  #     pose une deuxième case sur le terrain de jeu




can.focus_set()

can.bind('<KeyRelease>',Clavier,) #  3° Touches => fonction clavier
can.pack()
 
fen.mainloop()
fen.destroy()





