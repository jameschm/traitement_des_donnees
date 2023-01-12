def dichoIte(v, liste):
    a = 0
    b = len(liste)-1
    m = (a+b)//2
    while a < b :
        if liste[m] == v:
            return m
        elif liste[m] > v:
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return a