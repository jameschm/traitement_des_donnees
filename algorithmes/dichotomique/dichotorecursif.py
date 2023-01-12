def dichoRec(v, liste):
    if len(liste)==1 :
        return 0
    moyenne = len(liste)//2
    if liste[moyenne] == v:
        return moyenne
    elif liste[moyenne] > v:
        return dichoRec(v, liste[:moyenne])
    else :
        return moyenne + dichoRec(v, liste[moyenne:])