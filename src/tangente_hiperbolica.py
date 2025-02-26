import numpy as np
import matplotlib.pyplot as plt

# Definición de la función tangente hiperbólica
def tanh_func(x):
    return np.tanh(x)

# Derivada de la tangente hiperbólica: 1 - tanh(x)^2
def tanh_deriv(x):
    return 1 - np.tanh(x)**2

# Rango de valores para x
x = np.linspace(-5, 5, 400)
y = tanh_func(x)
y_deriv = tanh_deriv(x)

# Crear una figura y trazar ambas curvas en el mismo gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Tangente Hiperbólica (tanh x)')
plt.plot(x, y_deriv, label='Derivada', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('Valor')
plt.title('Función Tangente Hiperbólica y su Derivada')
plt.legend()
plt.grid(True)
plt.show()
