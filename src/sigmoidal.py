import numpy as np
import matplotlib.pyplot as plt

# Definición de la función sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide
def sigmoid_deriv(x):
    s = sigmoid(x)
    return s * (1 - s)

# Rango de valores para x
x = np.linspace(-10, 10, 400)
y = sigmoid(x)
y_deriv = sigmoid_deriv(x)

# Crear una figura y trazar ambas curvas en el mismo gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Función Sigmoide')
plt.plot(x, y_deriv, label='Derivada Sigmoide', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('Valor')
plt.title('Función Sigmoide y su Derivada')
plt.legend()
plt.grid(True)
plt.show()
