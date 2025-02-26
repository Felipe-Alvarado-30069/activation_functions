import numpy as np
import matplotlib.pyplot as plt

# Definición de la función ReLU
def relu(x):
    return np.maximum(0, x)

# Derivada de la función ReLU
# Se define como 1 para x > 0 y 0 para x <= 0
def relu_deriv(x):
    return np.where(x > 0, 1, 0)

# Rango de valores para x
x = np.linspace(-10, 10, 400)
y = relu(x)
y_deriv = relu_deriv(x)

# Crear una figura y trazar ambas curvas en el mismo gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Función ReLU')
plt.plot(x, y_deriv, label='Derivada ReLU', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('Valor')
plt.title('Función ReLU y su Derivada')
plt.legend()
plt.grid(True)
plt.show()
