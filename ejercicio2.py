"""
    file: ejercicio2.py
    autor: davidpillco
"""
# Listas
lista = [(100,2), (20, 4), (30, 1)]
lista2 = ["b", "a", "c"]
# Se imprime la lista 
print(list(zip(sorted(lista2), sorted (lista,key = lambda x: x[1]))))


