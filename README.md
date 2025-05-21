# Taller: Aplicaciones de Grafos en la Ingeniería de Software

Este repositorio contiene las soluciones a los tres ejercicios propuestos en el taller de grafos. Cada ejercicio aborda un problema real en el contexto de la ingeniería de software. Los datos de prueba se proporcionan en archivos externos para facilitar la validación.

## 📁 Estructura del repositorio

```
/
├── ejercicio1_camino_mas_corto.py
├── ejercicio2_cuellos_de_botella.py
├── ejercicio3_arbol_expansion_minima.py
├── datos/
│   ├── ejercicio1_datos.json
│   ├── ejercicio2_datos.json
│   └── ejercicio3_datos.py
└── README.md
```

---

## 🚀 Ejercicio 1: Camino más corto entre servicios

- **Archivo de datos:** `datos/ejercicio1_datos.json`
- **Formato:** JSON con un grafo dirigido ponderado y los nodos de origen y destino.
- **Instrucciones:**
  1. Carga el archivo con `json.load()`.
  2. Usa el algoritmo de Dijkstra para calcular el camino más corto.
  3. Imprime el camino y el costo total.

```python
import json

with open("datos/ejercicio1_datos.json") as f:
    datos = json.load(f)

grafo = datos["grafo"]
origen = datos["origen"]
destino = datos["destino"]
```

✅ **Resultado esperado con los datos de prueba:**
```
Camino más corto: ['frontend', 'auth', 'db', 'cache', 'storage']
Costo total: 45
```

---

## 🧭 Ejercicio 2: Cuellos de botella en navegación

- **Archivo de datos:** `datos/ejercicio2_datos.json`
- **Formato:** JSON con un grafo dirigido ponderado, nodo de inicio y nodo objetivo.
- **Instrucciones:**
  1. Carga el grafo y aplica BFS o DFS para contar los caminos posibles.
  2. Cuenta cuántos caminos pasan por cada nodo intermedio.
  3. Imprime un diccionario con los nodos más transitados.

```python
import json

with open("datos/ejercicio2_datos.json") as f:
    datos = json.load(f)

grafo = datos["grafo"]
inicio = datos["inicio"]
objetivo = datos["objetivo"]
```

✅ **Resultado esperado con los datos de prueba (puede variar según la estrategia de recorrido):**
```
{
  'login': 1,
  'dashboard': 4,
  'search': 3,
  'product': 2,
  'cart': 2,
  'faq': 1,
  'profile': 1,
  'settings': 1
}
```

---

## 🛰️ Ejercicio 3: Árbol de expansión mínima

- **Archivo de datos:** `datos/ejercicio3_datos.py`
- **Formato:** Script de Python con un grafo no dirigido y ponderado.
- **Instrucciones:**
  1. Importa el archivo o copia la estructura del grafo.
  2. Usa el algoritmo de Prim o Kruskal para obtener el MST.
  3. Imprime el conjunto de aristas del MST y su costo total.

```python
from datos.ejercicio3_datos import grafo
```

✅ **Resultado esperado con los datos de prueba:**
```
MST: [('Srv2', 'Srv3', 1), ('Srv1', 'Srv2', 3), ('Srv3', 'Srv5', 2), ('Srv4', 'Srv5', 3), ('Srv5', 'Srv6', 4)]
Costo total: 13
```

---

## ✅ Recomendaciones

- Asegúrate de modularizar tu código.
- Incluye comentarios explicativos.
- Valida tus resultados usando los datos de prueba antes de subir tu solución.

## 📤 Entrega

Publica este repositorio en GitHub y entrega el enlace en la plataforma asignada.