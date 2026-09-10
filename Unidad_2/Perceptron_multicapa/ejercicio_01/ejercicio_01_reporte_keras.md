### 1\. La red profunda (Keras)

-   **Topología:** Arquitectura de cuatro capas secuenciales (`4 x 3 x 3 x 3 x 3`), compuesta por 
- tres capas ocultas densas de 3 neuronas y una capa de salida final de 3 neuronas, todas con función de activación sigmoide.

-   **Dinámica de entrenamiento:** Al igual que en la versión manual, se ve fuertemente afectada por el desvanecimiento 
- del gradiente (*vanishing gradient*). Las derivadas sucesivas de la función sigmoide a través de
- sus cuatro capas reducen drásticamente la fuerza de actualización en las capas iniciales, provocando una larga meseta
- donde el error se estanca antes de intentar un leve descenso al final de las 500 épocas.

### 2\. La red original (Keras)

-   **Topología:** Arquitectura de dos capas (`4 x 3 x 3`), compuesta por una única capa oculta densa de 3 neuronas y
- una capa de salida final de 3 neuronas, ambas con activación sigmoide.

-   **Dinámica de entrenamiento:** Presenta una convergencia limpia y progresiva. Al tener menos capas consecutivas, 
- la retrogradación automatizada por TensorFlow/Keras distribuye los gradientes de manera eficiente, logrando una curva 
- de error descendente y continua que optimiza mejor el modelo dentro del límite de las 500 épocas.

### En resumen

A pesar de que ambas comparten exactamente los mismos hyperparámetros (un MLP con activación sigmoide, error MSE, SGD 
con $\eta = 0.03$ y 500 épocas), la adición de capas ocultas modifica drásticamente la optimización: mientras que 
la red original aprende de forma fluida, la red profunda colapsa en un cuello de botella de gradientes 
que impide un entrenamiento efectivo en el mismo número de iteraciones.

(EXPRESION de Gemini al analizar las graficas):
-   **Red original de Keras (`4 x 3 x 3`)**: La curva de pérdida (`grafica_error_keras_original_1.png`)
 muestra un descenso continuo y sostenido desde aproximadamente 0.26 hasta llegar cerca de 0.196 en la época 500. 
Aunque presenta una ligera inflexión cerca de la época 100, el modelo mantiene la capacidad de seguir optimizando 
el error de manera progresiva durante todo el entrenamiento.

-   **Red profunda de Keras (`4 x 3 x 3 x 3 x 3`)**: La curva de la versión con capas extra (`grafica_error_keras_extra_layers.png`) 
desciende con rapidez al principio, pero se estanca por completo ("plató") alrededor de la época 200 en un valor 
de error cercano a 0.222, quedándose totalmente plana hasta finalizar las 500 épocas.

A pesar de que Keras inicializa los pesos por defecto mediante *Glorot Uniform* 
(lo que evita el colapso total de gradientes que ocurría en la implementación manual con NumPy), añadir 
dos capas ocultas adicionales satura la red prematuramente en este problema. El modelo se atrapa en 
una solución subóptima y pierde la capacidad de seguir aprendiendo mucho antes de alcanzar 
el límite de las 500 épocas, obteniendo un error final más alto que la arquitectura original.
