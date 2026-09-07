## **Una estructura de datos**: 
Es una forma organizada de:

    -almacenar, 
    -administrar 
    -formatear datos 

En la memoria de una computadora para que puedan ser consultados y modificados de manera eficiente.

---

---
## Las estructuras de datos se dividen en 2:

### 1\. Estructuras Lineales

Los datos se organizan de forma secuencial, uno detrás de otro. Cada elemento tiene un único predecesor y un único sucesor (excepto el primero y el último).

-   **Arreglos / Vectores (Arrays):** Secuencias contiguas de elementos del mismo tipo con un tamaño fijo. Permiten un acceso rápido por índice, pero cambiar su tamaño es costoso.


-   **Listas Enlazadas (Linked Lists):** Colecciones de nodos donde cada uno contiene su dato y un puntero/enlace hacia la dirección de memoria del siguiente nodo. Son flexibles para insertar y eliminar elementos, pero no permiten acceso directo rápido por posición.


-   **Pilas (Stacks - LIFO):** Estructura del tipo *"Last In, First Out"* (el último en entrar es el primero en salir). Pensada para operaciones de apilado; se utiliza en la gestión de llamadas a funciones y en algoritmos como **DFS**.


-   **Colas (Queues - FIFO):** Estructura del tipo *"First In, First Out"* (el primero en entrar es el primero en salir). Los elementos entran por el final y salen por el frente; es la base para algoritmos como **BFS**.


-   **Colas de Prioridad (Priority Queues / Heaps):** Variante de cola donde los elementos se extraen según un valor de prioridad asociado, no solo por su orden de llegada. Es la estructura que permite implementar **UCS**.

### 2\. Estructuras No Lineales

Los datos no siguen un orden secuencial, sino una jerarquía o una red de relaciones múltiples.

-   **Árboles (Trees):** Estructuras jerárquicas formadas por un nodo raíz y subnodos conectados sin ciclos. Muy útiles para búsquedas rápidas (ej. Árboles de Búsqueda Binaria) y organización jerárquica de archivos.


-   **Grafos (Graphs):** Conjuntos de nodos (vértices) unidos por conexiones (aristas). Representan redes arbitrarias (redes sociales, mapas de carreteras como el de Rumania) y pueden ser dirigidos, no dirigidos, ponderados o no ponderados.


-   **Tablas Hash (Hash Tables / Diccionarios):** Estructuras que asocian claves con valores (*key-value*). Utilizan una función hash para transformar la clave en un índice de memoria, lo que permite búsquedas, inserciones y eliminaciones prácticamente instantáneas ($O(1)$).

---

| Estructura | Acceso por Posición | Inserción/Eliminación | Caso de Uso Principal |
|:---:|:---:|:---:|:---:|
| **Array** | Rápido (O(1)) | Lento (O(n)) | Lectura masiva por índice con datos de tamaño fijo. |
| **Lista Enlazada** | Lento (O(n)) | Rápido (O(1) si se conoce el nodo) | Inserción constante de elementos en memoria dinámica. |
| **Pila (Stack)** | Lento (solo tope) | Rápido (O(1)) | Historial de navegación, *backtracking* (DFS). |
| **Cola (Queue)** | Lento (solo frente) | Rápido (O(1)) | Colas de procesamiento, exploración por niveles (BFS). |
| **Tabla Hash** | No aplica | Rápido (O(1) por clave) | Búsqueda por nombre/ID, conteo de frecuencias. |
| **Grafo** | Depende del recorrido | Depende del diseño | Mapas, redes sociales, sistemas de recomendación. |

*NOTA:
los árboles son una subclase o caso especial de los grafos, al ser un "tipo particular" de grafo, su comportamiento 
técnico en las operaciones fundamentales es esencialmente