#importer le framework Numpy dans le script python
import numpy as np

#Commence par modifier la graine aléatoire pour qu'elle soit uniforme
np.random.seed(50)

#Définie les numéros que le joueur joue pour le(s) tirage(s) et donc reste contant
lotoJoueur = [np.random.randint(1, 45) for _ in range(5)]

#affiche les numéros du joueur
print(f"\nLes bon numeros du loto sont : {lotoJoueur}")

#création d'une fonction pour le jeu
def jeu_loto(list1):
    
    #demande au joueur le nombre de tirage qu'il souhaite faire
    nbTirage = int(input("\nEntrez le nombre de tirage : "))
    
    #créer une boucle pour faire les différents tirages en fonction du nombre donné par l'utilisateur
    for _ in range(nbTirage):
        
        #créer une liste avec les nombres utilisés par le tirage
        listTirage = [np.random.randint(1, 45) for _ in range(5)]
        #cherche les occurences entre les 2 listes avec la fonction trouve_occurences
        occurence = trouve_occurences(list1, listTirage)
        #condition pour savoir si tous les chiffres sont présents dans chacunes des listes
        if len(occurence) == 5:
            #affiche ne numéro du tirage ainsi que l'acclamation
            print(f"\nTirage : {_}\nLOTO!!!\n")

            
#créer une fonction qui détermine les occurences entres 2 listes
def trouve_occurences(liste1, liste2):
    #créer une liste afin de mettre les nombres qui sont présents dans les deux listes si il y en a 
    resultat = []
    #créer une boucle qui donne une valeur dans la liste1
    for _ in liste1:
        #créer une condition qui cherche si la valeur de la liste 1 est dans la liste2
        if _ in liste2:
            #ajoute la valeur présente dans la liste resultat si elle est présente
            resultat.append(_)
    #donne en retour la liste avec les occurences
    return resultat
    

#exécution du jeu avec la liste du joueur en argument créer au début du script
jeu_loto(lotoJoueur)

    