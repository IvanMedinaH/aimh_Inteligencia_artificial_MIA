



Cual es el nombre de la eficiencia en terminos de algoritmos?
    
    - Runtime
    - Uso de memoria?
    - Comparaciones?
    - Velocidad de procesamiento
    - *Parametros propios

### "la "eficiencia" no es un concepto absoluto: depende enteramente de qué recurso quieras o necesites optimizar en tu contexto."

Para comparar algoritmos de búsqueda teóricos y prácticos, las ciencias de la computación estandarizan dos recursos físicos principales que limitan a cualquier computadora:

<br>

    - el tiempo de procesamiento (operaciones de CPU) 
    - el espacio en memoria (almacenamiento en RAM)

<br>

---

## Complejidad de Tiempo
Mide cuántas operaciones o evaluaciones de nodos debe realizar el algoritmo antes de encontrar la solución (o determinar que no existe), en función del tamaño del problema.

### ¿Cómo se mide?
Se usa la notación Big-O,
- expresada mediante:($b$, $d$ o $m$)
  - $b$ (branching factor / factor de ramificación): 
    El número promedio de nodos conectadas a cada nodo (en Rumania, $b \approx 3$).
  - $d$ (depth / profundidad): El número de pasos/saltos desde el origen hasta
    la solución más cercana.
  - $m$ (maximum depth / profundidad máxima): El número máximo de saltos 
    que se pueden dar en el espacio de estados.



## Complejidad de Memoria (Espacio)
Mide cuánta memoria RAM necesita la computadora al mismo tiempo para almacenar los nodos que tiene en espera (la "frontera" o fringe) y los nodos ya visitados.

### ¿Como se mide?
La complejidad de memoria también se mide usando la Notación Big-O, especificando cuánta memoria crecerá en función de los parámetros del problema
(como $b$, $d$ o $m$).

    + En la práctica: Se cuantifica en número de nodos almacenados simultáneamente 
    en la frontera y en memoria. Por ejemplo, en BFS la memoria es $O(b^d)$, lo que significa que si $b=3$ y $d=5$, 
    la RAM debe almacenar aproximadamente $3^5 = 243$ nodos al mismo tiempo.
    
    + A nivel de hardware: Esos nodos representan >bytes reales< ocupados en las 
    estructuras de datos (como colas o listas) dentro de la memoria RAM.





| **Métrica**                     | **Pregunta que responde**                                             |
|---------------------------------|-----------------------------------------------------------------------|
| **Completado** (*Completeness*) | ¿El algoritmo garantiza encontrar una solución si esta existe?        |
| **Optimicidad** (*Optimality*)  | ¿La solución encontrada es la de menor costo (menor distancia en km)? |
| **Complejidad de Tiempo**       | ¿Cuánto tarda en encontrar la solución?                               |
| **Complejidad de Memoria**      | ¿Cuánta memoria RAM requiere durante el proceso?                      |



**Runtime**: la cantidad de unidades de tiempo, que le toma a un algoritmo para resolver un problema

***Nota:** Establecer un modelo estandar para la comprobacion de la eficiencia es lo ideal,
ya que en la practica:
"No siempre se obtendra el mismo valor de runtime"


### Runtime complexity (Complejidad en Tiempo de Ejecución) 
es una medida teórica que describe cómo escala el tiempo de procesamiento de un algoritmo conforme
aumenta el tamaño de la entrada de datos ($n$).
 
ejemplo:





runtime complexity mide el número total de **operaciones elementales** u
**Operaciones primitivas**



