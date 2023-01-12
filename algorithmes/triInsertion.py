#-----------------------TRI PAR INSERTION-----------------------#

def triInsersion(liste):
    for i in range(1, len(liste)):
        j = i
        while j > 0 and liste[j] < liste[j-1]:
            liste[j], liste[j-1] = liste[j-1], liste[j]
        j -= 1
    return liste