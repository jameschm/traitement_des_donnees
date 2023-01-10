def triInsersion(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
        j -= 1
    return lst


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