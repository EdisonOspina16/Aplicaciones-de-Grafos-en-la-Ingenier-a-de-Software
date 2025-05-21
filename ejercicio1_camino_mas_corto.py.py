"""Rutas óptimas entre servicios de una arquitectura distribuida"""

import json
import heapq

with open("datos/ejercicio1_datos.json") as f:
    datos = json.load(f)

grafo = datos["grafo"]
destino = datos["destino"]
origen = datos["origen"]


def dijkstra(grafo, origen, destino):
    heap = [(0, origen, [origen])]
    visitados  = set()

    while heap:
        distancia, v_actual, ruta_actual = heapq.heappop(heap)
        if v_actual == destino:
            return ruta_actual, distancia

        if v_actual in visitados:
            continue

        visitados.add(v_actual)
        for v_siguiente, distancia_siguiente in grafo[v_actual].items():
            if v_siguiente in visitados:
                heapq.heappush(heap, (distancia + distancia_siguiente, v_siguiente, ruta_actual + [v_siguiente]))

    return None, float("inf")

ruta_actual, distancia = dijkstra(grafo, origen, destino)
if ruta_actual:
    print("camino mas corto", ruta_actual)
    print("costo total ", distancia)
else:
    print(f"no se encontro un camino {origen} a {destino}")

