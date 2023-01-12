# importer le framework Numpy dans le script python
import numpy as np
# importer le framework Pandas dans le script python pour exporter en csv
import pandas as pd
# se deplacer dans les fichiers
from pathlib import Path
# pour iterer des listes dans des listes
import itertools
# importer matplotlib pour l'histogramme
import matplotlib.pyplot as plt


# création d'une fonction pour le loto
def jeu_loto():
    # Commence par modifier la graine aléatoire pour qu'elle soit uniforme
    np.random.seed(50)
    # Définie les numéros que le joueur joue pour le(s) tirage(s) et donc reste contant
    lotoJoueur = [np.random.randint(1, 46) for _ in range(5)]
    triCocktail(lotoJoueur)
    # affiche les numéros du joueur
    print(f"\nLes bon numeros du loto sont : {lotoJoueur}")
    listeVT = []
    # demande au joueur le nombre de tirage qu'il souhaite faire
    nbTirage = int(input("\nEntrez le nombre de tirage : "))

    # créer une boucle pour faire les différents tirages en fonction du nombre donné par l'utilisateur
    for _ in range(nbTirage):

        # créer une liste avec les nombres utilisés par le tirage
        listTirage = [np.random.randint(1, 46) for _ in range(5)]
        triCocktail(listTirage)
        # ajout de la liste listeTirage dans la liste listeVT
        listeVT.append(listTirage)
        # cherche les occurences entre les 2 listes avec la fonction trouve_occurences
        occurence = trouve_occurences(lotoJoueur, listTirage)
        # condition pour savoir si tous les chiffres sont présents dans chacunes des listes
        if len(occurence) == 5:
            # affiche ne numéro du tirage ainsi que l'acclamation
            print(f"\nTirage : {_}\nLOTO!!!\n")
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


# création de la fonction sauvegarde csv
def exCsv(liste):
    # ajout des données dans pandas
    df = pd.DataFrame(liste)
    print(df)
    # conversion en csv
    filepath = Path('loto/exportCSV.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    return df.to_csv(filepath)


# création de la fonction sauvegarde json
def exJson(liste):

    df = pd.DataFrame(
        liste, columns=['PREMIER', 'DEXIEME', 'TROISIEME', 'QUATRIEME', 'CINQUIEME'])
    print(df)
    filepath = Path('loto/exportJSON.json')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    return df.to_json(filepath, orient='columns')


# création de la fonction sauvegarde binaire
def exBinaire(liste):
    int_array = list(itertools.chain(*liste))
    binary_lists = [np.binary_repr(x, width=8) for x in int_array]
    binary_data = "".join(binary_lists)
    filepath = Path('loto/exportBIN.bin')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "wb") as f:
        f.write(bytes(binary_data, "latin1"))


# création de la fonction chargement binaire
def imBinaire():
    filepath = Path('loto/exportBIN.bin')
    with open(filepath, 'rb') as f:
        binary_data = f.read()
    binary_lists = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    int_array = [int(x, 2) for x in binary_lists]
    liste = list(itertools.groupby(int_array, lambda x: int_array.index(x)//8))
    return liste


# création de la fonction de lancement de la sauvegarde et chargement
def expimpormats(liste):
    return exCsv(liste), exJson(liste), exBinaire(liste), imBinaire()


# création de la fonction de création de l'histogramme dans le shell
def histogramme(liste):
    n = min(liste)
    print("| VALEUR | OCCURENCE(s) |")

    while n <= max(liste)+1:
        v = 0
        for _ in range(len(liste)):
            if liste[_] == n:
                v += 1
            else:
                continue
        if v >= 1:
            print(f"| {n} | {v} |")
        else:
            pass
        n += 1


# création de la fonction de création de l'histogramme graphique
def histoGraph(liste):
    plt.hist(liste, bins=5, color='purple', edgecolor='black', alpha=0.7)
    plt.title("Histogramme", fontsize=14, fontweight='bold')
    plt.xlabel("Valeur", fontsize=12)
    plt.ylabel("Fréquence", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(visible=True, alpha=0.3)
    plt.show()


# création de la fonction de lancement des histogrammes
def doHistogram(liste):
    liste1 = list(itertools.chain(*liste))
    histogramme(liste1)
    histoGraph(liste1)


# création de la fonction pour effectuer un tri cocktaik
def triCocktail(liste):
    debut = 0
    fin = len(liste) - 1
    while debut < fin:
        echange = False
        for _ in range(debut, fin):
            if liste[_] > liste[_+1]:
                liste[_], liste[_+1] = liste[_+1], liste[_]
            echange = True
        fin -= 1
        if not echange:
            break
        for _ in range(fin-1, debut-1, -1):
            if liste[_] > liste[_+1]:
                liste[_], liste[_+1] = liste[_+1], liste[_]
            echange = True
        debut += 1
    return liste


# création de la fonction pour effectuer un tri fusion
def triFusion(lst):
    # Si la liste ne contient qu'un élément, elle est déjà triée
    if len(lst) <= 1:
        return lst

    # Détermine le milieu de la liste
    mid = len(lst) // 2

    # Tri la première moitié de la liste
    left = triFusion(lst[:mid])

    # Tri la seconde moitié de la liste
    right = triFusion(lst[mid:])

    # Fusionne les deux moitiés triées
    return merge(left, right)


# création de la fonction pour effectuer un tri fusion
def merge(left, right):
    # Initialise la liste qui contiendra les éléments fusionnés
    merged = []
    # Initialise les indices des éléments à comparer dans chaque liste
    left_index = 0
    right_index = 0
    # Tant que les deux listes ne sont pas vides, compare les éléments et ajoute le plus petit à la liste fusionnée
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Ajoute les éléments restants de la liste la plus longue à la liste fusionnée
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


# création de la fonction pour le lancement du programme
def process():
    LISTETIR = jeu_loto()
    expimpormats(LISTETIR)
    doHistogram(LISTETIR)


# lancement du programme
process()
