import numpy as np
import matplotlib.pyplot as plt

# Definición de la función sinusoidal
def sin_func(x):
    return np.sin(x)

# Derivada de la función sinusoidal
def sin_deriv(x):
    return np.cos(x)

# Rango de valores para x (desde -2π hasta 2π)
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y = sin_func(x)
y_deriv = sin_deriv(x)

# Crear una figura y trazar ambas curvas en el mismo gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Función Sinusoidal (sin x)')
plt.plot(x, y_deriv, label='Derivada (cos x)', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('Valor')
plt.title('Función Sinusoidal y su Derivada')
plt.legend()
plt.grid(True)
plt.show()
