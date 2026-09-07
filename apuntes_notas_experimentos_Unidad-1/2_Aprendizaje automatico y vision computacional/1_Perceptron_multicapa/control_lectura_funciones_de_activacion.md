Si solo multiplicamos entradas por pesos y las sumamos ($W_2(W_1 x + b_1) + b_2$), 
la red entera colapsa matemáticamente en una sola operación lineal.
Las funciones de activación no lineales se introducen después de **la suma ponderada**
para 

    - romper la linealidad 
    - permitir que la red aprenda fronteras de decisión complejas.


#### 1\. Sigmoide ($\sigma$)

-   **Fórmula:**

    $$\sigma(z) = \frac{1}{1 + e^{-z}}$$

-   **Rango:** $(0, 1)$

-   **Uso:** Históricamente usada en capas ocultas; actualmente se reserva para la **capa de salida en clasificación binaria** (interpretable como probabilidad).

-   **Desventaja:** Sufre del problema de *desvanecimiento del gradiente* (*vanishing gradient*) para valores extremos de $z$.

#### 2\. Tangente Hiperbólica ($\tanh$)

-   **Fórmula:**

    $$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$$

-   **Rango:** $(-1, 1)$

-   **Uso:** Capas ocultas. Al estar centrada en cero, facilita la convergencia respecto a la sigmoide.

#### 3\. ReLU (*Rectified Linear Unit*)

-   **Fórmula:**

    $$\text{ReLU}(z) = \max(0, z)$$

-   **Rango:** $[0, \infty)$

-   **Uso:** **El estándar en capas ocultas** para la mayoría de redes neuronales profundas.

-   **Ventaja:** Es computacionalmente muy rápida y no sufre de desvanecimiento de gradiente para valores positivos.

#### 4\. Softmax

-   **Fórmula (para la $i$-ésima neurona de salida):**

    $$\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

-   **Rango:** $(0, 1)$, con la propiedad de que $\sum \text{Softmax}(z_i) = 1$.

-   **Uso:** Exclusivo para la **capa de salida en clasificación multiclase** (ej. clasificando los 10 dígitos de MNIST).