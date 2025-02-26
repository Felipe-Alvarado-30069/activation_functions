import numpy as np
import matplotlib.pyplot as plt

# Definición de la función a tramos:
#   - Para x < -1: f(x) = -1
#   - Para -1 ≤ x ≤ 1: f(x) = x
#   - Para x > 1: f(x) = 1
def piecewise_func(x):
    return np.piecewise(x, 
                        [x < -1, (x >= -1) & (x <= 1), x > 1], 
                        [lambda x: -1, lambda x: x, lambda x: 1])

# Derivada de la función a tramos:
#   - Para x < -1: f'(x) = 0
#   - Para -1 < x < 1: f'(x) = 1
#   - Para x > 1: f'(x) = 0
def piecewise_func_deriv(x):
    return np.piecewise(x, 
                        [x < -1, (x > -1) & (x < 1), x > 1], 
                        [0, 1, 0])

# Rango de valores para x
x = np.linspace(-3, 3, 500)
y = piecewise_func(x)
y_deriv = piecewise_func_deriv(x)

# Crear una figura única y trazar ambas curvas
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Función a tramos')
plt.plot(x, y_deriv, label='Derivada', linestyle='--', color='green')
plt.xlabel('x')
plt.ylabel('Valor')
plt.title('Función a tramos y su Derivada')
plt.legend()
plt.grid(True)
plt.show()
