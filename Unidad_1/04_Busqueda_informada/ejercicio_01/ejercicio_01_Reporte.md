
<br>python .\02_heuristics.py --from-city Zerind --to Hirsova          
<br>Heuristic: Euclidean distance to Hirsova (map coordinates)
<br>
<br>  h(n)  city
<br>      0  Hirsova  <- goal
<br>     64  Eforie
<br>     78  Urziceni
<br>     97  Vaslui
<br>    136  Bucharest
<br>    168  Iasi
<br>    178  Giurgiu
<br>    215  Pitesti
<br>    227  Neamt
<br>    249  Fagaras
<br>    288  Craiova
<br>    307  Rimnicu Vilcea
<br>    344  Sibiu
<br>    366  Mehadia
<br>    370  Lugoj
<br>    373  Drobeta
<br>    444  Timisoara
<br>    460  Oradea
<br>    463  Zerind  <- start
<br>    465  Arad

---

<br>python .\03_greedy_best_first_search.py --from-city Zerind --to Hirsova
<br>Algorithm: Greedy best-first search
<br>Problem:   Zerind → Hirsova
<br>Heuristic: Euclidean distance to Hirsova (map coordinates)
<br>Status:    success
<br>Path:      Zerind → Oradea → Sibiu → Fagaras → Bucharest → Urziceni → Hirsova
<br>Depth:     6 roads
<br>Cost:      715 km

| city      | g   | h   | f   |
|-----------|-----|-----|-----|
| Zerind    | 0   | 463 | 463 |
| Oradea    | 71  | 460 | 531 |
| Sibiu     | 222 | 344 | 566 |
| Fagaras   | 321 | 249 | 570 |
| Bucharest | 532 | 136 | 668 |
| Urziceni  | 617 | 78  | 695 |
| Hirsova   | 715 | 0   | 715 |

<br>Expanded:  6 nodes
<br>Generated: 18 nodes
<br>Frontier:  max size 6

---

<br>python .\04_a_star_search.py --from-city Zerind --to Hirsova
<br>Algorithm: A* search
<br>Problem:   Zerind → Hirsova
<br>Heuristic: Euclidean distance to Hirsova (map coordinates)
<br>Status:    success
<br>Path:      Zerind → Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest → Urziceni → Hirsova
<br>Depth:     7 roads
<br>Cost:      676 km

| city                  | g    | h   | f   |
|-----------------------|------|-----|-----|
| Zerind                | 0    | 463 | 463 |
| Arad                  | 75   | 465 | 540 |
| Sibiu                 | 215  | 344 | 559 |
| Rimnicu Vilcea        | 295  | 307 | 602 |
| Pitesti               | 392  | 215 | 607 |
| Bucharest             | 493  | 136 | 629 |
| Urziceni              | 578  | 78  | 656 |
| Hirsova               |  676 | 0   | 676 |

Expanded:  11 nodes
Generated: 31 nodes
Frontier:  max size 6
---

# Reporte:
Reporte de Comparación: 
 **Greedy Best-First Search vs. A* Search**

**Ruta analizada:** 
[Zerind → Hirsova]

**Heurística utilizada:** Distancia euclidiana hacia Hirsova (coordenadas del mapa)

### 1\. Comparación de Resultados y Caminos Encontrados

Los algoritmos **NO** devolvieron el mismo camino:

-   **A* Search:**

    -   **Ruta:** Zerind → Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest → Urziceni → Hirsova

    -   **Costo total ($g$):** 676 km

    -   **Profundidad:** 7 carreteras

    -   **Desempeño:** Expandió 11 nodos (generó 31).

-   **Greedy Best-First Search:**

    -   **Ruta:** Zerind → Oradea → Sibiu → Fagaras → Bucharest → Urziceni → Hirsova

    -   **Costo total ($g$):** 715 km

    -   **Profundidad:** 6 carreteras

    -   **Desempeño:** Expandió 6 nodos (generó 18).


### **¿Por qué difieren los caminos?**

**_Greedy_** elige con un criterio muy corto, únicamente el nodo con el menor valor heurístico $h(n)$
(distancia en línea recta al destino), sin importar la distancia ya recorrida $g(n)$. 
<br>
**_A*_** evalúa la función de evaluación global $f(n) = g(n) + h(n)$, lo que le permite encontrar
la ruta verdaderamente óptima (676 km) haciendo un mayor número de expansiones en el arbol de busqueda.

### Heurística Empleada

Se utilizó la **distancia euclidiana** calculada a partir de las coordenadas del mapa para
el destino Hirsova (a diferencia de la tabla estándar de AIMA que comúnmente reporta 
distancias en línea recta hacia Bucharest). De acuerdo con la consulta a `02_heuristics.py`,
los valores de $h(n)$ de interés son:



## Criterios de aceptación(diseño de reporte final)

  - si Greedy y A* devolvieron el **mismo** camino o no, y por qué;
  - qué heurística se usó (tabla AIMA vs. euclidiana);
  - en al menos un punto de decisión, cómo `h(n)` (Greedy) frente a
    `f(n) = g(n) + h(n)` (A*) explica la ciudad que cada algoritmo expandió.
- Incluyes evidencias (capturas o salida de terminal) de las corridas.