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
    # Commence par définir la graine aléatoire pour qu'elle soit uniforme
    np.random.seed(10)
    # Définie les numéros que le joueur joue pour le(s) tirage(s) et donc reste contant
    lotoJoueur = [np.random.randint(1, 46) for _ in range(5)]
    triCocktail(lotoJoueur)
    # affiche les numéros du joueur
    print(f"\nLes bon numeros du loto sont : {lotoJoueur}")
    # création d'une liste vide
    listeVT = []
    # demande au joueur le nombre de tirage qu'il souhaite faire
    nbTirage = int(input("\nEntrez le nombre de tirage : "))

    # créer une boucle pour faire les différents tirages en fonction du nombre donné par l'utilisateur
    for _ in range(nbTirage):

        # créer une liste avec les nombres utilisés par le tirage et le tri dans un ordre croissant avec le tri fusion
        listTirage = triFusion([np.random.randint(1, 46) for _ in range(5)])
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


# création de la fonction sauvegarde csv qui prend une liste en argument
def exCsv(liste):
    # La fonction crée un DataFrame Pandas à partir de la liste
    df = pd.DataFrame(liste)
    # création un chemin d'accès pour le fichier CSV à exporter
    filepath = Path('loto/sauvegarde_loto/exportCSV.csv')
    # la fonction exporte le DataFrame vers le fichier CSV spécifié
    filepath.parent.mkdir(parents=True, exist_ok=True)
    # retourne le résultat
    return df.to_csv(filepath)


# création de la fonction sauvegarde json qui prend une liste en argument
def exJson(liste):
    # La fonction crée un DataFrame à partir de la liste
    df = pd.DataFrame(
        liste, columns=['PREMIER', 'DEXIEME', 'TROISIEME', 'QUATRIEME', 'CINQUIEME'])
    # définit le chemin du fichier JSON à exporter
    filepath = Path('loto/sauvegarde_loto/exportJSON.json')
    # création d'un dossier parent pour le fichier si nécessaire et exporte le DataFrame vers le fichier JSON en spécifiant l'orientation des colonnes
    filepath.parent.mkdir(parents=True, exist_ok=True)
    # La fonction retourne ensuite le chemin du fichier exporté
    return df.to_json(filepath, orient='columns')


# création de la fonction sauvegarde binaire à partir d'une list
def exBinaire(liste):
    # convertit chaque élément de la liste en un tableau binaire à 8 bits
    int_array = list(itertools.chain(*liste))
    # il combine tous les tableaux binaires en une seule chaîne de caractères binaires
    binary_lists = [np.binary_repr(x, width=8) for x in int_array]
    # création d'un fichier binaire avec ce contenu
    binary_data = "".join(binary_lists)
    # définit le chemin du fichier binaire à exporter
    filepath = Path('loto/sauvegarde_loto/exportBIN.bin')
    # création d'un dossier parent pour le fichier si nécessaire et exporte le DataFrame vers le fichier Binaire en spécifiant l'orientation des colonnes
    filepath.parent.mkdir(parents=True, exist_ok=True)
    # ouverture du fichier binaire
    with open(filepath, "wb") as f:
        # écriture de la chane de caractère dans le fichier binaire
        f.write(bytes(binary_data, "latin1"))


# création de la fonction chargement binaire
def imBinaire():
    # Il lit le fichier binaire à partir du chemin de fichier spécifié
    filepath = Path('loto/sauvegarde_loto/exportBIN.bin')
    # ouverture du fichier binaire
    with open(filepath, 'rb') as f:
        # stocke dans la variable binary_data le contenue du fichier binaire
        binary_data = f.read()
    # il divise binary_data en sous-listes de 8 bits
    binary_lists = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    # convertit en entiers à l'aide de la fonction int ()
    int_array = [int(x, 2) for x in binary_lists]
    # Les entiers sont regroupés par lots de 5
    sous_listes = [int_array[i:i+5] for i in range(0, len(int_array), 5)]
    # définit le chemin du fichier binaire à charger en fichier texte lisible
    filepath = Path('loto/sauvegarde_loto/importBIN.txt')
    # ouverture du fichier texte
    with open(filepath, 'w') as f:
        # écrits dans un nouveau fichier texte
        return f.write(str(sous_listes))


# création de la fonction de lancement de la sauvegarde et chargement
def expimpormats(liste):
    # éxécution des différentes fonction d'export import
    return exCsv(liste), exJson(liste), exBinaire(liste), imBinaire()


# création de la fonction de création de l'histogramme qui prend en paramètre une liste de nombre
def histogramme(liste):
    # La fonction commence par définir trois variables. n est égal à la valeur minimale de la liste, m est égal à la valeur maximale de la liste et l est égal à la longueur de la liste
    n, m, l = min(liste), max(liste), len(liste)
    # La fonction définit ensuite deux listes: listN et listV. La fonction imprime ensuite un tableau avec les valeurs et leurs occurrences
    listN, listV = [], []
    # afficher le format pour l'affichage
    print("\n| VALEUR | OCCURENCE(s) | HISTOGRAMME |\n\n", end='')

    # La fonction itère ensuite sur chaque élément de la liste pour compter le nombre d'occurrences de chaque valeur
    while n < m+1:
        # soit v le nombre d'occurence
        v = 0
        # boucle qui ajout une unité à v si il trouve la meme valeur que n
        for _ in range(l):
            if liste[_] == n:
                v += 1
            else:
                continue
        # Les valeurs sont ajoutées à la liste N et leurs occurrences sont ajoutées à la liste V
        listN.append(n)
        listV.append(v)
        # La fonction imprime ensuite un histogramme pour chaque valeur avec le nombre d'occurrences correspondant
        r = v / len(liste)*2000
        if v >= 1:
            print(f"| {n} | {v} | : ")
            for _ in range(int(r)):
                print("*", end='')
            print("\n")
        else:
            pass
        # on passe à l'itération du nombre n+1
        n += 1
    print(listN, listV)
    # les deux listes sont retournées à la fin de l'exécution de la fonction
    return listN, listV


# création de la fonction de création de l'histogramme graphique qui prend en paramètre une liste
def histoGraph(liste):
    # La fonction génère un histogramme à partir de cette liste avec la bibliothèque matplotlib
    plt.hist(liste, bins=45, color='purple', edgecolor='black', alpha=0.7)
    # Elle définit le titre, les étiquettes des axes et les paramètres de style pour le graphique.
    plt.title("Histogramme", fontsize=14, fontweight='bold')
    plt.xlabel("Valeur", fontsize=12)
    plt.ylabel("Fréquence", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(visible=True, alpha=0.3)
    # affiche le graphique à l'aide de la fonction plt.show()
    plt.show()


# création de la fonction de lancement des histogrammes qui prend en paramètre une liste
def doHistogram(liste):
    # La fonction commence par convertir la liste en une seule liste à l'aide de la méthode itertools.chain
    liste1 = list(itertools.chain(*liste))
    # appel de la fonction histogramme et pour l'afficher graphiquement
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


# création de la fonction pour effectuer un tri fusion par interclassement
def interclassement(lst1, lst2):
    lst_totale = []
    n1, n2 = len(lst1), len(lst2)
    i1, i2 = 0, 0
    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst_totale.append(lst1[i1])
            i1 += 1
        else:
            lst_totale.append(lst2[i2])
            i2 += 1
    return lst_totale + lst1[i1:] + lst2[i2:]


# création de la fonction pour effectuer un tri fusion
def triFusion(liste):
    if len(liste) <= 1:
        return liste
    else:
        m = len(liste) // 2
        return interclassement(triFusion(liste[:m]), triFusion(liste[m:]))


# création de la fonction pour le lancement du programme et le sens de fonctionnement
def process():
    LISTETIR = jeu_loto()
    expimpormats(LISTETIR)
    doHistogram(LISTETIR)


# lancement du programme
process()
