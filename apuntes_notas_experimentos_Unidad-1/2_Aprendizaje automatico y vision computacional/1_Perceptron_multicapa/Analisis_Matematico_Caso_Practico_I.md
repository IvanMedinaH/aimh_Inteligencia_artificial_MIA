### Capa de Entrada
$$\mathbf{a}^{(0)} = \mathbf{x}$$

### Capa Oculta
* **Suma ponderada:**  
  $$\mathbf{z}^{(1)} = \mathbf{W}^{(1)} \mathbf{a}^{(0)} + \mathbf{b}^{(1)}$$
* **Activación (ReLU):**  
  $$\mathbf{a}^{(1)} = \max(0, \mathbf{z}^{(1)})$$

### Capa de Salida
* **Suma ponderada:**  
  $$\mathbf{z}^{(2)} = \mathbf{W}^{(2)} \mathbf{a}^{(1)} + \mathbf{b}^{(2)}$$
* **Activación (Softmax) / Predicción:**  
  $$\hat{\mathbf{y}} = \frac{e^{\mathbf{z}^{(2)}}}{\sum e^{\mathbf{z}^{(2)}}}$$

