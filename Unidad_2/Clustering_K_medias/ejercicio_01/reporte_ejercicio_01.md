## Reporte

### Comparativo: K-Means (Original vs. Modificado)

A continuación se presenta el análisis comparativo detallado de las ejecuciones original y modificada del algoritmo K-Means, evaluando el impacto de separar adecuadamente las nubes de puntos (*blobs*).

### 1\. Distribución de los Datos (Scatter Plot)

-   **Original (`blob_original.png`)**: Tres de los cinco blobs situados en la parte izquierda (`x_1 \approx -2.8`) se encuentran extremadamente juntos y solapados. Esto provoca que K-Means los interprete de manera ambigua o los fusione en la práctica.

-   **Modificado (`blob_modificado.png`)**: Al redefinir los centros en coordenadas más distantes (`[0, 0]`, `[-3, 3]`, `[3, 3]`, `[-3, -3]`, `[3, -3]`), se aprecian **cinco islas o nubes gaussianas totalmente independientes y delimitadas** a simple vista.

### 2\. Diagramas de Voronoi ($k = 5$)

-   **Original (`voronoi_original.png`)**: Las regiones de Voronoi dividen el espacio de forma forzada, particionando de manera poco natural los grupos de la izquierda debido a su alta cercanía y superposición.

-   **Modificado (`voronoi_modificado.png`)**: Las fronteras de decisión geométricas de Voronoi se distribuyen de manera simétrica y limpia, **envolviendo de forma perfecta a cada uno de los 5 grupos** en su propia región de color asignada.

### 3\. Curva de Inercia (Método del Codo)

-   **Original (`codo_original.png`)**: La gráfica de inercia muestra una inflexión pronunciada (*Elbow*) en **$k = 4$**, lo que lleva al analista a concluir erróneamente que existen 4 clústeres en lugar de los 5 reales con los que se generaron los datos.

-   **Modificado (`codo_modificado.png`)**: Con los datos separados, la curva del codo se desplaza o refleja un cambio de pendiente estructural en **$k = 5$**, indicando correctamente que añadir un quinto centroide reduce significativamente la inercia antes de estabilizarse.

### 4\. Coeficiente de Silueta

-   **Original (`sliueta_original.png`)**: El puntaje máximo de silueta se concentra claramente en **$k = 4$** (alcanzando casi `0.69`), penalizando a $k = 5$ debido a la confusión entre los blobs empalmados.

-   **Modificado (`sliueta_modificado.png`)**: Al eliminar el solapamiento, la métrica de silueta refleja una estructura de agrupamiento mucho más coherente para los 5 grupos independientes.

### En Resumen (Conclusiones para el Reporte)

1.  **¿Por qué el codo original prefería $k = 4$?**

    Porque cuando los tres blobs de la izquierda están demasiado juntos ($\sigma = 0.1$), K-Means los optimiza como un solo conglomerado gigante, haciendo matemáticamente óptima la partición en 4 grupos desde la perspectiva de la inercia global.

2.  **Impacto de la modificación:** Al separar los centros y ajustar las desviaciones estándar, se cumple la condición de que la distancia entre centros sea mayor que la suma de sus dispersiones, permitiendo que tanto el codo como la silueta identifiquen correctamente la estructura real de **$5$ clústeres**.