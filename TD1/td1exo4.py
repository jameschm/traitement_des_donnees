#--------------------EXERCICE4--------------------#
  
def algo_bulle(tab, n):
    for i in range(n):
        for j in range(n):
            if tab[j]>tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]