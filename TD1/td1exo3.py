#--------------------EXERCICE3--------------------#

def algo_bulle_v2(tab, n):
    for i in range(n):
        for j in range(n):
            if tab[j]>tab[j+1]:
                temp = tab[j]
                tab[j]=tab[j+1]
                tab[j+1]=temp