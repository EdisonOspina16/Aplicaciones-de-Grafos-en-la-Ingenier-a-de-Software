"""Análisis de cuellos de botella en flujos de navegación"""

import json

with open("datos/ejercicio2_datos.json") as f:
    datos = json.load(f)

grafo = datos["grafo"]
inicio = datos["inicio"]
objetivo = datos["objetivo"]


def cuello_de_botella(grafo, inicio, objetivo):
    nodos = {}
    visitados = set()
    cola = [(inicio, [inicio])]

    while cola:
        nodo_actual, camino = cola.pop(0)
        if nodo_actual == objetivo:
            for nodo in camino[1:-1]:
                nodos[nodo] = nodos.get(nodo, 0) + 1
            continue

        for siguiente in grafo[nodo_actual]:
            if siguiente not in camino:
                nuevo_camino = camino + [siguiente]
                cola.append((siguiente, nuevo_camino))

    return nodos


resultado = cuello_de_botella(grafo, inicio, objetivo)
print(resultado)
