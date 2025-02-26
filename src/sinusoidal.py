# Importación de bibliotecas necesarias
import numpy as np  # Biblioteca para operaciones matemáticas y manipulación de arreglos numéricos
import matplotlib.pyplot as plt  # Biblioteca para la generación de gráficos

# Definición de la función que grafica la función sinusoidal y su derivada
def plot_sinusoidal():
    """
    Función que calcula y grafica la función sinusoidal y su derivada.
    """

    # Definición de la función sinusoidal
    def sin_func(x):
        return np.sin(x)  # Devuelve el seno de x
    
    # Derivada de la función sinusoidal
    def sin_deriv(x):
        return np.cos(x)  # La derivada del seno es el coseno
    
    # Definir el rango de valores para x (desde -2π hasta 2π)
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)  # Genera 400 valores equidistantes en el rango [-2π, 2π]
    
    # Evaluar la función seno en los valores de x
    y = sin_func(x)
    
    # Evaluar la derivada (coseno) en los valores de x
    y_deriv = sin_deriv(x)

    # Crear una figura para la gráfica
    plt.figure(figsize=(8, 6))  # Define el tamaño de la figura en pulgadas (8x6)
    
    # Graficar la función sinusoidal
    plt.plot(x, y, label='Función Sinusoidal (sin x)')  
    
    # Graficar la derivada de la función sinusoidal (coseno) con línea punteada y color verde
    plt.plot(x, y_deriv, label='Derivada (cos x)', linestyle='--', color='green')
    
    # Etiquetas de los ejes
    plt.xlabel('x')
    plt.ylabel('Valor')
    
    # Título del gráfico
    plt.title('Función Sinusoidal y su Derivada')
    
    # Agregar leyenda para identificar las curvas
    plt.legend()
    
    # Agregar cuadrícula para mejorar la visualización
    plt.grid(True)
    
    # Mostrar la gráfica en pantalla
    plt.show()

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    plot_sinusoidal()  # Llama a la función para graficar la función sinusoidal y su derivada
