"""
    file: ejercicio3.py
    autor: davidpillco
"""
# Listas
lista = [(100,2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]
# Se transforma a mayusculas la lista 2
lista3 = list(map(lambda x:x.upper(), lista2))
# Se imprime la lista 
print(list(zip(sorted (lista,key = lambda x: x[0]),sorted(lista3, reverse = True))))
