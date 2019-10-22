"""
    file: ejercicio5.py
    autor: davidpillco
"""
# Listas
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
nombres = ["Ángel", "José", "Ana"]
lista4 = list(zip(paraleloA,nombres))
# Se transforma a mayusculas la lista 2
lista3 = list(map(lambda x:(sum(x[0])/3,x[1]), lista4))
print(list(lista3))
print(list(max(lista3)))
lista3.reverse()
# Se imprime la lista 
print(lista3)


