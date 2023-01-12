#-----------------------TRI PAR INSERTION-----------------------#

def triInsersion(liste):
    for i in range(1, len(liste)):
        j = i
        while j > 0 and liste[j] < liste[j-1]:
            liste[j], liste[j-1] = liste[j-1], liste[j]
        j -= 1
    return liste

#-----------------------TRI COCKTAIL-----------------------#

def triCocktail(liste):
    d = 0
    f = len(liste) - 1
    while d < f:
        echange = False
        for _ in range(d, f):
            if liste[_] > liste[_+1]:
                liste[_], liste[_+1] = liste[_+1], liste[_]
            echange = True
        f -= 1
        if not echange:
            break
        for _ in range(f-1, d-1, -1):
            if liste[_] > liste[_+1]:
                liste[_], liste[_+1] = liste[_+1], liste[_]
            echange = True
        d += 1
    return liste

#-----------------------TRI FUSION-----------------------#

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

def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    else:
        m = len(liste) // 2
        return interclassement(tri_fusion(liste[:m]), tri_fusion(liste[m:]))
    
liste = [[7, 38, 7, 23, 6], [3, 32, 8, 5, 15], [36, 29, 28, 27, 27], [7, 21, 44, 32, 22], [43, 42, 1, 7, 20], [3, 16, 31, 42, 36], [27, 3, 13, 33, 4], [3, 11, 1, 30, 30], [31, 1, 12, 31, 27], [8, 29, 25, 28, 14]]
    
for i in liste:
    print(tri_fusion(i))
