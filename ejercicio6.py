"""
    file: ejercicio6.py
    autor: davidpillco
"""
# Listas
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
nombres = ["Luis", "Ángel", "José", "Ana"]
# Unen las listas
lista4 = list(zip(paraleloA, nombres))
# Creo una lista con sus evaluaciones
lista3 = list(map(lambda x:(sum(x[0])/3,sum(x[0]),x[1]), lista4))
# Imprime lista con el filtro
print(list(filter(lambda x: x[0]<= 5 ,lista3)))
