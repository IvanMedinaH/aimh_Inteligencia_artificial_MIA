
Criterios utilizados: 
###### Se omitio como pareja origen–destino:
### Arad → Bucharest.
Se utilizo las pareja, listada a continuacion, buscando entender el comportamiento del algoritmo en busquedas de conexiones
donde el algoritmo se encargue de  resolver el problema de hallar la ruta mas corta en un grafo no dirigido considerando el menor
costo.

Busqueda de ruta mas corta:

    [x] Oradea - Craiova (BFS, UCS)


# Se corrieron los 5 algoritmos de busqueda no informada: 
    -BFS
        -Oradea - Craiova
    -UCS
        -Oradea - Craiova
    -DFS
        -Oradea - Craiova
    -DLS (con ≥ 2 límites)
         -Oradea - Craiova
    
    -IDS (sobre esa misma pareja).
         -Oradea - Craiova
---
    -ALTERNATIVOS(*nota estos no estaban en el requierimiento pero se hizo con la intencion de revisar el comportamiento en busquedas mas largas)
  
         -BFS
            -Oradea - Drobeta
            -Oradea - Eforie
            -Oradea - Vaslui
        -UCS
            -Oradea - Drobeta
            -Oradea - Eforie
            -Oradea - Vaslui
        -DFS
            -Timisoara - Fagaras
            -Timisoara - Neamt

---
***Nota:** Dentro de la ruta Unidad_1/03_Busqueda_no_informada/ejercicio_01, se encuentran los archivos con el siguiente
formato :

    -[Algoritmo]_--from-city [ciudad] --to [ciudad].png
---
<br><br>
# Reporte:

## Revision de casos

###### **BFS y UCS devolvieron el mismo camino**:
Sí, devolvieron exactamente el mismo camino (Oradea → Sibiu → Rimnicu Vilcea → Craiova, 377 km, 3 carreteras)
,aunque en rutas cortas, en rutas mas largas, UCS tomo un camino extra
como se puede observar en los archivos alternativos testeados:

    UCS: -Unidad_1/03_Busqueda_no_informada/ejercicio_01/CASO ALTERNATIVOS/UCS_--from-city Oradea --to Vaslui.png 
    BFS: -Unidad_1/03_Busqueda_no_informada/ejercicio_01/CASO ALTERNATIVOS/BFS_--from-city Oradea --to Vaslui.png

###### o no, y por qué;
En este caso si devolvieron el mismo camino al ser una ruta corta, pero como expreso en los ejemplos anteriores con mas 
nodos por visitar, UCS fue mas optimo en km, pero en nodos expandidos, nodos generados
y profundidad tuvo un mayor impacto que BFS

**_DFS_** fue el mas costoso de todos los algoritmos con 785 km de ruta acumulados (`[Unidad_1/03_Busqueda_no_informada/ejercicio_01/Tabla_rutas_ALGORITMOS.md]()`).

###### IDS coincide con BFS en profundidad? (número de carreteras)
IDS vs. BFS (Coincidencia en profundidad): Sí, IDS coincide con BFS en una profundidad de 3 carreteras. IDS 
realiza búsquedas en profundidad incrementales ($L=0, 1, 2, 3$) y garantiza encontrar la solución a la profundidad 
mínima $d$, al igual que BFS.

###### Qué pasó con DLS en el límite bajo (cutoff)
###### frente al límite suficiente.
DLS con límite bajo vs. límite suficiente: Con $L=2$ ocurre un cutoff porque la solución más cercana está a 3 pasos.
Al subir el límite a $L=3$, alcanza la profundidad mínima requerida y devuelve la solución óptima en carreteras (377 km).

---

---

## Datos de casos:

# A Oradea- Craiova  / BFS
    [SCRIPT]: python .\02_breadth_first_search.py --from-city Oradea --to Craiova 
<br>Algorithm: Breadth-first search
<br>Problem:   Oradea → Craiova
<br>Status:    success
<br>Path:      Oradea → Sibiu → Rimnicu Vilcea → Craiova
<br>Depth:     3 roads
<br>Cost:      377 km
<br>Expanded:  6 nodes
<br>Generated: 15 nodes
<br>Frontier:  max size 4

# A Oradea- Craiova  / UCS
    [SCRIPT]:python .\03_uniform_cost_search.py --from-city Oradea --to Craiova 
<br>Algorithm: Uniform-cost search
<br>Problem:   Oradea → Craiova
<br>Status:    success
<br>Path:      Oradea → Sibiu → Rimnicu Vilcea → Craiova
<br>Depth:     3 roads
<br>Cost:      377 km
<br>Expanded:  9 nodes
<br>Generated: 24 nodes
<br>Frontier:  max size 4

# A Oradea - Craiova  / DFS
    [SCRIPT]python .\04_depth_first_search.py --from-city Oradea --to Craiova        
<br>Algorithm: Depth-first search
<br>Problem:   Oradea → Craiova
<br>Status:    success
<br>Path:      Oradea → Sibiu → Arad → Timisoara → Lugoj → Mehadia → Drobeta → Craiova
<br>Depth:     7 roads
<br>Cost:      785 km
<br>Expanded:  7 nodes
<br>Generated: 18 nodes
<br>Frontier:  max size 4

# A Oradea - Craiova  / DLS
    [SCRIPT]python .\05_depth_limited_search.py --from-city Oradea --to Craiova --limit 3
<br>Algorithm: Depth-limited search
<br>Problem:   Oradea → Craiova
<br>Status:    success
<br>Detail:    limit=3
<br>Path:      Oradea → Sibiu → Rimnicu Vilcea → Craiova
<br>Depth:     3 roads
<br>Cost:      377 km
<br>Expanded:  5 nodes
<br>Generated: 12 nodes
<br>Frontier:  max size 6

# A Oradea - Craiova  / DLS
    [SCRIPT]python .\05_depth_limited_search.py --from-city Oradea --to Craiova --limit 2
<br>Algorithm: Depth-limited search
<br>Problem:   Oradea → Craiova
<br>Status:    cutoff
<br>Detail:    limit=2
<br>Expanded:  3 nodes
<br>Generated: 9 nodes
<br>Frontier:  max size 6


# A Oradea - Craiova  / IDS
    [SCRIPT]python .\06_iterative_deepening_search.py --from-city Oradea --to Craiova         
<br>Algorithm: Iterative deepening search
<br>Problem:   Oradea → Craiova
<br>Status:    success
<br>Detail:    last_limit=3
<br>Path:      Oradea → Sibiu → Rimnicu Vilcea → Craiova
<br>Depth:     3 roads
<br>Cost:      377 km
<br>Expanded:  9 nodes
<br>Generated: 25 nodes
<br>Frontier:  max size 6

---

---

<br><br>
<br><br>
***Nota:** Las evidencias (capturas o salida de terminal) de las corridas.
Unidad_1/03_Busqueda_no_informada/ejercicio_01/CASO PRINCIPAL IMG