#### **Selección de Pareja con Discrepancia y Trabajo Realizado (Expanded)**

En la pareja **Timisoara → Sibiu**, ambos algoritmos (Greedy y A*) devolvieron el **mismo camino óptimo** 
(258 km, pasando por Arad). 
Para observar una **discrepancia clara** donde Greedy es engañado por la línea recta, 
se debe analizar la ruta **Zerind → Hirsova** o Timisoara → Bucharest en algoritmos informados:


| **Algoritmo (Instancia Zerind → Hirsova)** | **Path (Camino)**                                                                 | **Cost (g)** | **Expanded (Trabajo)** | **Estatus** |
|--------------------------------------------|-----------------------------------------------------------------------------------|--------------|------------------------|-------------|
| **Greedy Best-First Search**               | Zerind → Oradea → Sibiu → Fagaras → Bucharest → Urziceni → Hirsova                | 715 km       | **6 nodos**            | Subóptimo   |
| **A* Search**                              | Zerind → Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest → Urziceni → Hirsova | **676 km**   | **11 nodos**           | Óptimo      |


## ¿Cuál algoritmo "trabajó" más?
A* trabajó más (expandió 11 nodos vs. 6 de Greedy). 
Esto sucede porque Greedy evalúa siempre maximizando pero a la vez canibalizando el rendimiento buscado 
solo $h(n)$ y se lanza de inmediato por el camino que parece "más cercano en línea recta" 
(Oradea), sin verificar el costo real acumulado. 
A* necesita mantener la frontera de evaluación $f(n) = g(n) + h(n)$, lo que lo obliga a 
explorar y desestimar ramas alternativas para garantizar matemáticamente el costo mínimo.


Al correr UCS (búsqueda no informada, equivalente a la función de evaluación 
$f(n) = g(n)$) (<-- esto lo busque para poder expresar correctamente la relacion entre)
    
    + $g(n)$: Es el costo real acumulado del camino desde el nodo inicial (origen) 
      hasta el nodo actual $n$.
    + $h(n)$: Es la estimación heurística del costo restante desde el nodo actual
      $n$ hasta el objetivo.

para Timisoara → Sibiu:

| **Algoritmo**                                 | **Path**                 | **Cost (g)** | **Expanded** |
|-----------------------------------------------|--------------------------|--------------|--------------|
| **UCS** (`03_uniform_cost_search.py`)         | Timisoara → Arad → Sibiu | **258 km**   | 6 nodos      |
| **A*** (`04_a_star_search.py`)                | Timisoara → Arad → Sibiu | **258 km**   | 3 nodos      |
| **Greedy** (`03_greedy_best_first_search.py`) | Timisoara → Arad → Sibiu | 258 km       | 3 nodos      |



## Instruccion: 
- Cambia solo el destino (mismo origen): una vez a Bucharest y otra a una
  ciudad distinta. Observa cómo cambia la etiqueta de la heurística y si
  Greedy sigue (o deja de) coincidir con A*.

---
## Data, Corridas en la consola: 

<br>(.venv) PS E:\1 CLASES MAESTRIA\Maestria en IA\1er semestre\Apuntes\github\aimh\Unidad_1\04_Busqueda_informada\project> python .\03_greedy_best_first_search.py --from-city Timisoara --to Mehadia
<br>Algorithm: Greedy best-first search
<br>Problem:   Timisoara → Mehadia
<br>Heuristic: Euclidean distance to Mehadia (map coordinates)
<br>Status:    success
<br>Path:      Timisoara → Lugoj → Mehadia
<br>Depth:     2 roads
<br>Cost:      181 km

| **city**  | **g** | **h** | **f** |
|-----------|-------|-------|-------|
| Timisoara | 0     | 103   | 103   |
| Lugoj     | 111   | 40    | 151   |
| Mehadia   | 181   | 0     | 181   |

<br>Expanded:  2 nodes
<br>Generated: 5 nodes
<br>Frontier:  max size 2

<br>(.venv) PS E:\1 CLASES MAESTRIA\Maestria en IA\1er semestre\Apuntes\github\aimh\Unidad_1\04_Busqueda_informada\project> python .\04_a_star_search.py --from-city Timisoara --to Bucharest         
<br>Algorithm: A* search
<br>Problem:   Timisoara → Bucharest
<br>Heuristic: straight-line distance to Bucharest (AIMA table)
<br>Status:    success
<br>Path:      Timisoara → Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest
<br>Depth:     5 roads
<br>Cost:      536 km

| **city**       | **g** | **h** | **f** |
|----------------|-------|-------|-------|
| Timisoara      | 0     | 329   | 329   |
| Arad           | 118   | 366   | 484   |
| Sibiu          | 258   | 253   | 511   |
| Rimnicu Vilcea | 338   | 193   | 531   |
| Pitesti        | 435   | 100   | 535   |
| Bucharest      | 536   | 0     | 536   |

<br>Expanded:  10 nodes
<br>Generated: 27 nodes
<br>Frontier:  max size 5

<br>(.venv) PS E:\1 CLASES MAESTRIA\Maestria en IA\1er semestre\Apuntes\github\aimh\Unidad_1\04_Busqueda_informada\project> python .\04_a_star_search.py --from-city Timisoara --to Mehadia  
<br>Algorithm: A* search
<br>Problem:   Timisoara → Mehadia
<br>Heuristic: Euclidean distance to Mehadia (map coordinates)
<br>Status:    success
<br>Path:      Timisoara → Lugoj → Mehadia
<br>Depth:     2 roads
<br>Cost:      181 km

| **city**  | **g** | **h** | **f** |
|-----------|-------|-------|-------|
| Timisoara | 0     | 103   | 103   |
| Lugoj     | 111   | 40    | 151   |
| Mehadia   | 181   | 0     | 181   |

<br>Expanded:  2 nodes
<br>Generated: 5 nodes
<br>Frontier:  max size 2

<br>(.venv) PS E:\1 CLASES MAESTRIA\Maestria en IA\1er semestre\Apuntes\github\aimh\Unidad_1\04_Busqueda_informada\project> python .\03_greedy_best_first_search.py --from-city Timisoara --to Bucharest
<br>Algorithm: Greedy best-first search
<br>Problem:   Timisoara → Bucharest
<br>Heuristic: straight-line distance to Bucharest (AIMA table)
<br>Status:    success
<br>Path:      Timisoara → Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest
<br>Depth:     6 roads
<br>Cost:      615 km

| **city**  | **g** | **h** | **f** |
|-----------|-------|-------|-------|
| Timisoara | 0     | 329   | 329   |
| Lugoj     | 111   | 244   | 355   |
| Mehadia   | 181   | 241   | 422   |
| Drobeta   | 256   | 242   | 498   |
| Craiova   | 376   | 160   | 536   |
| Pitesti   | 514   | 100   | 614   |
| Bucharest | 615   | 0     | 615   |

<br>Expanded:  6 nodes
<br>Generated: 15 nodes
<br>Frontier:  max size 3

---


### **Análisis de Cambio de Destino desde Timisoara**

### **1\. Destino: Bucharest**

-   **Etiqueta de Heurística:** *straight-line distance to Bucharest (AIMA table)*. 
     Al usar la tabla estática estándar de AIMA hacia Bucharest, los valores de $h(n)$ cambian completamente con respecto a las distancias euclidianas del mapa.

-   **Greedy:** Toma la ruta por el sur vía **Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest** (Costo: **615 km**, 6 carreteras, 6 nodos expandidos).

-   **A*:** Toma la ruta por el norte vía **Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest** (Costo: **536 km**, 5 carreteras, 10 nodos expandidos).

-   **Resultado:** **Greedy y A* NO coinciden.** Greedy se deja llevar por valores $h$ más 
     bajos hacia el sur, pero termina pagando **79 km más** de recorrido real.
     A* explora más nodos (10 vs. 6) para encontrar la ruta óptima.

### **2\. Destino: Mehadia**

-   **Etiqueta de Heurística:** *Euclidean distance to Mehadia (map coordinates)*. El script conmuta automáticamente a calcular la distancia en línea recta en el mapa hacia el nuevo punto geográfico objetivo.

-   **Greedy:** Toma la ruta **Lugoj → Mehadia** (Costo: **181 km**, 2 carreteras, 2 nodos expandidos).

-   **A*:** Toma la misma ruta **Lugoj → Mehadia** (Costo: **181 km**, 2 carreteras, 2 nodos expandidos).

-   **Resultado:** **Greedy y A* SÍ coinciden exactamente** en camino, costo y número de nodos expandidos.





