#--------------------EXERCICE2--------------------#

def facto_recur(n):
    if n == 1:
        return 1
    else:
        return n * facto_recur(n-1)