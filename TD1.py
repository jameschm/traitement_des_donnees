#--------------------EXERCICE1--------------------#

def facto_itera(n):
    x = 1
    for _ in range(n):
        x *= n
        n -= 1
    return x

#--------------------EXERCICE2--------------------#

def facto_recur(n):
    if n == 1:
        return 1
    else:
        return n * facto_recur(n-1)

#--------------------EXERCICE3--------------------#

def algo_bulle_v2(tab, n):
    for i in range(n):
        for j in range(n):
            if tab[j]>tab[j+1]:
                temp = tab[j]
                tab[j]=tab[j+1]
                tab[j+1]=temp

#--------------------EXERCICE4--------------------#
  
def algo_bulle(tab, n):
    for i in range(n):
        for j in range(n):
            if tab[j]>tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]

#--------------------EXERCICE6--------------------#

def occurence(tab):
    n = min(tab)
    print("| VALEUR | OCCURENCE(s) |")
    
    while n <= max(tab):
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

r = [1,1,1,1,3,3,2,2,2,3,2,1,55,3,1]         

occurence(r)      

        