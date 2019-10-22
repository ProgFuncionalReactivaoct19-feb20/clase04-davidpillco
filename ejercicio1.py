"""
    file: ejercicio1.py
    autor: davidpillco
"""
# Listas
listaA = [10, 2, 3, 4]
listaB = ["a", "b", "c", "d"]
# Se ordena la listaA
listaC = sorted( listaA)
# Se desordena la listaB
listaD = sorted(listaB, reverse=True)
# Se imprime la listaC y listaD
print(list(zip(listaC, listaD)))
# Se imprime el maximo de las listaC y listaD
print(list(max(zip(listaC, listaD))))

