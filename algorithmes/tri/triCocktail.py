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