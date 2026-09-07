

## **Los algoritmos de búsqueda no informada (o búsquedas a ciegas):**
son estrategias que exploran el espacio de estados utilizando únicamente
la estructura del mapa o grafo (las conexiones entre nodos),
    
    -No disponen de información extra. 
    -No disponen de heurísticas que les indiquen qué tan cerca están de la meta.
    -Saben reconocer cuándo llegaron al objetivo. 
    -No tienen intuición de hacia dónde conviene avanzar.
---
## Explicación por Algoritmo

BFS (Breadth-First Search / Búsqueda en Amplitud):
Explora el mapa nivel por nivel de manera uniforme, evaluando todos los vecinos directos del origen 
antes de avanzar al siguiente nivel de profundidad. 
Garantiza encontrar el camino con el menor número de saltos, pero consume una cantidad enorme de 
memoria RAM al almacenar todos los nodos abiertos.

UCS (Uniform-Cost Search / Búsqueda de Costo Uniforme):Prioriza expandir el camino con el menor costo acumulado
$g(n)$ en lugar de la menor profundidad. Es la variante adaptada a grafos con pesos 
y garantiza encontrar la ruta óptima de menor costo total (por ejemplo, el menor kilometraje real en carretera).

DFS (Depth-First Search / Búsqueda en Profundidad):Explora una sola rama lo más profundo posible hasta llegar 
a un fondo o a un ciclo antes de retroceder (backtracking). Requiere muy poco espacio en memoria, pero no 
garantiza encontrar la solución óptima y corre el riesgo de perderse en ramas infinitas si no se controlan los estados 
repetidos.

DLS(Depth-Limited Search / Búsqueda con Profundidad Limitada):Es un algoritmo DFS al que se le impone un límite máximo 
de profundidad $L$ para evitar que se pierda en ramas infinitas. 
Su principal inconveniente es que si la solución se encuentra a una profundidad mayor que $L$, 
el algoritmo fallará sin encontrar el objetivo.

IDS (Iterative Deepening Search / Búsqueda en Profundidad Iterativa):Ejecuta DLS de forma sucesiva incrementando 
el límite $L$ en 1 en cada iteración ($L=0, 1, 2...$). 
Logra combinar la garantía de encontrar la solución con menos saltos (como BFS) utilizando la mínima cantidad de memoria
RAM (como DFS).

---

| Algoritmo | 	Qué optimiza (o no)                  | Estrategia de Búsqueda                                                        |
|-----------|---------------------------------------|-------------------------------------------------------------------------------|
| BFS       | Menor número de carreteras (hops)     | Explora por niveles                                                           |
| UCS       | Menor costo en km                     | Explora por menor costo acumulado                                             |
| 	DFS      | 	Ninguna garantía de optimalidad      | Explora lo mas profundo posible                                               |
| 	DLS	     | DFS con límite de profundidad         | Variante del anterior pero con un limite<br/> de profundidad maximo<br/>en L  |
| 	IDS	     | Misma optimalidad de hops que BFS     | Variante del anterior pero con un limite de profundidad iterativo (L=0,1,2,3) |


| algoritmo | Encuentra la ruta optima?                   | Complejidad  |
|--------|------------------------------------------------|--------------|
| BFS    | Solo si todas las aristas tienen el mismo coste |              |
| UCS    | Si, siempre                                    |              |
| DFS    | No                                             |              |
| DLS    | No                                             |              |
| IDS    | Solo en numero de pasos                        |              |


