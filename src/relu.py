# Importación de bibliotecas necesarias
import numpy as np  # Biblioteca para operaciones matemáticas y manipulación de arreglos numéricos
import matplotlib.pyplot as plt  # Biblioteca para la generación de gráficos

# Definición de la función que grafica la función ReLU y su derivada
def plot_relu():
    """
    Función que calcula y grafica la función ReLU y su derivada.
    """

    # Definición de la función ReLU (Rectified Linear Unit)
    def relu(x):
        return np.maximum(0, x)  # Devuelve x si x > 0, y 0 si x ≤ 0
    
    # Derivada de la función ReLU
    def relu_deriv(x):
        return np.where(x > 0, 1, 0)  # La derivada es 1 si x > 0, y 0 si x ≤ 0
    
    # Definir el rango de valores para x
    x = np.linspace(-10, 10, 400)  # Crea un array con 400 valores equidistantes en el rango [-10, 10]
    
    # Evaluar la función ReLU en los valores de x
    y = relu(x)
    
    # Evaluar la derivada de la función ReLU en los valores de x
    y_deriv = relu_deriv(x)

    # Crear una figura para la gráfica
    plt.figure(figsize=(8, 6))  # Define el tamaño de la figura en pulgadas (8x6)
    
    # Graficar la función ReLU
    plt.plot(x, y, label='Función ReLU')  
    
    # Graficar la derivada de la función ReLU con línea punteada y color verde
    plt.plot(x, y_deriv, label='Derivada ReLU', linestyle='--', color='green')
    
    # Etiquetas de los ejes
    plt.xlabel('x')
    plt.ylabel('Valor')
    
    # Título del gráfico
    plt.title('Función ReLU y su Derivada')
    
    # Agregar leyenda para identificar las curvas
    plt.legend()
    
    # Agregar cuadrícula para mejorar la visualización
    plt.grid(True)
    
    # Mostrar la gráfica en pantalla
    plt.show()

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    plot_relu()  # Llama a la función para graficar la función ReLU y su derivada
