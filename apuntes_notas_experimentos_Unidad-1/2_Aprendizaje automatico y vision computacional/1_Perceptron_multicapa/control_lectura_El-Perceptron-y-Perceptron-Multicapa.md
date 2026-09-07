### A. El Perceptrón Simple (Rosenblatt, 1958)
Es la unidad básica del aprendizaje profundo, inspirada en la neurona biológica. Su funcionamiento consta de los siguientes pasos:
* Recibe un conjunto de entradas.
* Les aplica un peso de importancia a cada una.
* Suma un sesgo (*bias*).
* Pasa el resultado por una función de decisión (activación).

#### Modelo matemático
Dado un vector de entradas $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$ y un vector de pesos $\mathbf{w} = [w_1, w_2, \dots, w_n]^T$, se lleva a cabo el cálculo de la **suma ponderada** ($z$):

$$z = \sum_{i=1}^{n} w_i x_i + b = \mathbf{w}^T \mathbf{x} + b$$

**¿Cómo lo leemos?**

* **$z =$** : «$z$ es igual a...»
<br><br>
* **$\sum_{i=1}^{n}$** : «La sumatoria desde $i$ igual a uno hasta $n$ de...» (indica que vas a sumar una serie de elementos desde el primero hasta el número $n$).
<br><br>
* **$w_i x_i$** : «$w$ sub $i$ por $x$ sub $i$» (o simplemente «$w$ subíndice $i$ por $x$ subíndice $i$»).
Representa la multiplicación de cada peso por su respectiva entrada.
<br><br>
* **$+ b$** : «Más $b$» (normalmente llamado sesgo o *bias* en contextos de Inteligencia Artificial).
<br><br>
* **$=$** : «Lo cual es igual a...»
<br><br>
* **$\mathbf{w}^T \mathbf{x}$** : «$w$ transpuesta por $x$» (las letras en negrita indican que $\mathbf{w}$ y $\mathbf{x}$ son vectores. Multiplicar el vector fila $\mathbf{w}^T$ por el vector columna $\mathbf{x}$ es la forma matricial abreviada de escribir exactamente la misma sumatoria anterior).
<br><br>
**Salida ($\hat{y}$):**

$$\hat{y} = f(z)$$

Donde:
* **$b$** es el sesgo o *bias* (permite desplazar la función de activación).
* **$f(z)$** es una función de paso unitario (Heaviside), definida como:

$$f(z) = \begin{cases} 1 & \text{si } z \ge 0 \\ 0 & \text{si } z < 0 \end{cases}$$


##### **El perceptrón simple solo puede resolver problemas linealmente separables<br> (donde una línea recta o hiperplano puede dividir las clases)**


---------

---------

---------

<br_><br><br><br>


## 1. Estructura de un MLP (Multilayer perceptron):
-**Capa de Entrada (Input Layer):** Recibe las características del problema (ej. los 784 píxeles de una imagen de MNIST).

-**Capas Ocultas (Hidden Layers):**
Capas intermedias donde las neuronas extraen representaciones y características abstractas de los datos.

-**Capa de Salida (Output Layer):** Produce la predicción final (ej. 10 probabilidades para 
los dígitos 0 al 9).

-**El Teorema de Aproximación Universal:** Establece que un Perceptrón Multicapa con una sola capa oculta y
funciones de activación no lineales puede aproximar cualquier función continua,
independientemente de su complejidad.


## 2. Aplicar Funciones de Activación

Si solo multiplicamos entradas por pesos y las sumamos ($W_2(W_1 x + b_1) + b_2$), 
la red entera colapsa matemáticamente en una sola operación lineal.

Las funciones de activación no lineales se introducen después de **la suma ponderada**
para romper la linealidad y permitir que la red aprenda fronteras de decisión complejas.

Funciones de activacion mas importantes: 

    Sigmoide
    Tangente Hiperbolica
    ReLu
    SoftMax





