#--------------------EXERCICE6--------------------#

def occurence(tab):
    n = min(tab)
    print("| VALEUR | OCCURENCE(s) |")
    
    while n <= max(tab)+1:
        v = 0
        for _ in range(len(tab)):
            if tab[_] == n:
                v += 1
            else:
                continue
        if v >= 1:
            print(f"| {n} | {v} |")
        else:
            pass
        n += 1