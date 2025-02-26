# Importación de bibliotecas necesarias
import numpy as np  # Biblioteca para operaciones matemáticas y manejo de arreglos numéricos
import matplotlib.pyplot as plt  # Biblioteca para la generación de gráficos

# Definición de la función que grafica la función gaussiana y su derivada
def plot_gaussian():
    """
    Función que calcula y grafica la función gaussiana estándar y su derivada.
    """

    # Definición de la función gaussiana (distribución normal estándar)
    def gaussian(x):
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)  # Fórmula de la distribución normal estándar

    # Derivada de la función gaussiana
    def gaussian_deriv(x):
        return -x * gaussian(x)  # Derivada de la función gaussiana con respecto a x
    
    # Definir el rango de valores para x
    x = np.linspace(-10, 10, 400)  # Crea un array con 400 valores equidistantes en el rango [-10, 10]
    
    # Evaluar la función gaussiana en los valores de x
    y = gaussian(x)
    
    # Evaluar la derivada de la función gaussiana en los valores de x
    y_deriv = gaussian_deriv(x)
    
    # Crear una figura para la gráfica
    plt.figure(figsize=(8, 6))  # Define el tamaño de la figura en pulgadas (8x6)
    
    # Graficar la función gaussiana
    plt.plot(x, y, label='Función Gaussiana')  
    
    # Graficar la derivada de la función gaussiana con línea punteada y color verde
    plt.plot(x, y_deriv, label='Derivada', linestyle='--', color='green')
    
    # Etiquetas de los ejes
    plt.xlabel('x')
    plt.ylabel('Valor')
    
    # Título del gráfico
    plt.title('Función Gaussiana y su Derivada')
    
    # Agregar leyenda para identificar las curvas
    plt.legend()
    
    # Agregar cuadrícula para mejorar la visualización
    plt.grid(True)
    
    # Mostrar la gráfica en pantalla
    plt.show()

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    plot_gaussian()  # Llama a la función para graficar la función gaussiana y su derivada
