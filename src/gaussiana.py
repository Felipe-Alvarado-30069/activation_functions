import numpy as np
import matplotlib.pyplot as plt

# Definición de la función gaussiana (distribución normal estándar)
def gaussian(x):
    return (1/np.sqrt(2*np.pi)) * np.exp(-x**2 / 2)

# Derivada de la función gaussiana
def gaussian_deriv(x):
    return -x * gaussian(x)

# Rango de valores para x
x = np.linspace(-10, 10, 400)
y = gaussian(x)
y_deriv = gaussian_deriv(x)

# Crear una figura y trazar ambas curvas en el mismo eje
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Función Gaussiana')
plt.plot(x, y_deriv, label='Derivada', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('Valor')
plt.title('Función Gaussiana y su Derivada')
plt.legend()
plt.grid(True)
plt.show()
