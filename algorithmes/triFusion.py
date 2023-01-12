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