import numpy as np
import matplotlib.pyplot as plt

# Definición de la función identidad
def identidad(x):
    return x

# Derivada de la función identidad
def identidad_deriv(x):
    return np.ones_like(x)

# Rango de valores para x
x = np.linspace(-10, 10, 400)
y = identidad(x)
y_deriv = identidad_deriv(x)

# Crear una figura y trazar ambas curvas en el mismo gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Función Identidad')
plt.plot(x, y_deriv, label='Derivada (Constante 1)', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('Valor')
plt.title('Función Identidad y su Derivada')
plt.legend()
plt.grid(True)
plt.show()
