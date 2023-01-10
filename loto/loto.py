# importer le framework Numpy dans le script python
import numpy as np
# importer le framework Pandas dans le script python pour exporter en csv
import pandas as pd
# import format json
import json
# se deplacer dans les fichiers
from pathlib import Path
# pour iterer des listes dans des listes
import itertools
#importer matplotlib pour l'histogramme
import matplotlib as mp


# création d'une fonction pour le loto
def jeu_loto():
    # Commence par modifier la graine aléatoire pour qu'elle soit uniforme
    np.random.seed(50)
    # Définie les numéros que le joueur joue pour le(s) tirage(s) et donc reste contant
    lotoJoueur = [np.random.randint(1, 46) for _ in range(5)]
    # affiche les numéros du joueur
    print(f"\nLes bon numeros du loto sont : {lotoJoueur}")
    listeVT = []
    # demande au joueur le nombre de tirage qu'il souhaite faire
    nbTirage = int(input("\nEntrez le nombre de tirage : "))

    # créer une boucle pour faire les différents tirages en fonction du nombre donné par l'utilisateur
    for _ in range(nbTirage):

        # créer une liste avec les nombres utilisés par le tirage
        listTirage = [np.random.randint(1, 46) for _ in range(5)]
        # ajout de la liste listeTirage dans la liste listeVT
        listeVT.append(listTirage)
        # cherche les occurences entre les 2 listes avec la fonction trouve_occurences
        occurence = trouve_occurences(lotoJoueur, listTirage)
        # condition pour savoir si tous les chiffres sont présents dans chacunes des listes
        if len(occurence) == 5:
            # affiche ne numéro du tirage ainsi que l'acclamation
            print(f"\nTirage : {_}\nLOTO!!!\n")
        else:
            continue
    return listeVT


# créer une fonction qui détermine les occurences entres 2 listes
def trouve_occurences(liste1, liste2):
    # créer une liste afin de mettre les nombres qui sont présents dans les deux listes si il y en a
    resultat = []
    # créer une boucle qui donne une valeur dans la liste1
    for _ in liste1:
        # créer une condition qui cherche si la valeur de la liste 1 est dans la liste2
        if _ in liste2:
            # ajoute la valeur présente dans la liste resultat si elle est présente
            resultat.append(_)
    # donne en retour la liste avec les occurences
    return resultat


def exCsv(liste):
    # ajout des données dans pandas
    df = pd.DataFrame(liste)
    print(df)
    # conversion en csv
    filepath = Path('loto/exportCSV.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    return df.to_csv(filepath)


def exJson(liste):

    df = pd.DataFrame(
        liste, columns=['PREMIER', 'DEXIEME', 'TROISIEME', 'QUATRIEME', 'CINQUIEME'])
    print(df)
    filepath = Path('loto/exportJSON.json')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    return df.to_json(filepath, orient='columns')


def exBinaire(liste):
    int_array = list(itertools.chain(*liste))
    binary_lists = [np.binary_repr(x, width=8) for x in int_array]
    binary_data = "".join(binary_lists)
    filepath = Path('loto/exportBIN.bin')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "wb") as f:
        f.write(bytes(binary_data, "latin1"))


def exprotation2Formats(liste):
    return exCsv(liste), exJson(liste), exBinaire(liste)


def histogramme(tab):
    tabu = list(itertools.chain(*tab))
    n = min(tabu)
    print("| VALEUR | OCCURENCE(s) |")

    while n <= max(tabu)+1:
        v = 0
        for _ in range(len(tabu)):
            if tabu[_] == n:
                v += 1
            else:
                continue
        if v >= 1:
            print(f"| {n} | {v} |")
        else:
            pass
        n += 1


def process():
    LISTETIR = jeu_loto()
    exprotation2Formats(LISTETIR)
    histogramme(LISTETIR)


process()
