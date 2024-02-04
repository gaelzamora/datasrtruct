# Realiza un algoritmo que imprima la cantidad de letras del abedecario que contiene una cadena se permiten letras duplicadas
# Ejemplo: hola
# a
# h
# l
# o

def countLetter(string: str):
    if len(string) <= 1: return string
    abc = "abcdefghijklmnñopqrstuvwxyz"
    myMap = {}

    for s in string:
        if s in myMap:
            myMap[s] += 1
        else:
            myMap[s] = 1

    for letter in abc:
        if letter in myMap:
            print(letter*myMap[letter])

    return string

print(countLetter("lluvia de estrellas"))