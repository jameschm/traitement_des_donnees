#--------------------EXERCICE1--------------------#

def facto_itera(n):
    x = 1
    for _ in range(n):
        x *= n
        n -= 1
    return x   

        