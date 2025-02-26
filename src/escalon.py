import numpy as np
import matplotlib.pyplot as plt

# Definición de la función escalón (Heaviside)
def step_function(x):
    return np.where(x < 0, 0, 1)

# Rango de valores para x
x = np.linspace(-10, 10, 400)
y = step_function(x)

# Derivada aproximada: cero en casi todo el dominio (x=0 es un punto de discontinuidad)
y_deriv = np.zeros_like(x)

# Crear una figura y un eje
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Función Escalón')
plt.plot(x, y_deriv, label='Derivada (apróximada)', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('Valor')
plt.title('Función Escalón y su Derivada')
plt.legend()
plt.grid(True)
plt.show()
