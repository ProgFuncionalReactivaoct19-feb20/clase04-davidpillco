"""
    file: ejercicio4.py
    autor: davidpillco
"""
# Listas
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]
# Se transforma a mayusculas la lista 2
lista3 = list(map(lambda x:(x[0]+x[1]+ x[2])/3, paraleloA))
# Se imprime la lista 
print(list(zip(lista3, nombres)))
