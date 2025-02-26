# Importación de bibliotecas necesarias
import numpy as np  # Biblioteca para operaciones matemáticas y manipulación de arreglos numéricos
import matplotlib.pyplot as plt  # Biblioteca para la generación de gráficos

# Definición de la función que grafica la función sigmoide y su derivada
def plot_sigmoid():
    """
    Función que calcula y grafica la función sigmoide y su derivada.
    """

    # Definición de la función sigmoide
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))  # Fórmula de la función sigmoide

    # Derivada de la función sigmoide
    def sigmoid_deriv(x):
        s = sigmoid(x)  # Primero se calcula la sigmoide
        return s * (1 - s)  # Fórmula de la derivada de la sigmoide: f'(x) = f(x) * (1 - f(x))

    # Definir el rango de valores para x
    x = np.linspace(-10, 10, 400)  # Crea un array con 400 valores equidistantes en el rango [-10, 10]
    
    # Evaluar la función sigmoide en los valores de x
    y = sigmoid(x)
    
    # Evaluar la derivada de la función sigmoide en los valores de x
    y_deriv = sigmoid_deriv(x)

    # Crear una figura para la gráfica
    plt.figure(figsize=(8, 6))  # Define el tamaño de la figura en pulgadas (8x6)
    
    # Graficar la función sigmoide
    plt.plot(x, y, label='Función Sigmoide')  
    
    # Graficar la derivada de la función sigmoide con línea punteada y color verde
    plt.plot(x, y_deriv, label='Derivada Sigmoide', linestyle='--', color='green')
    
    # Etiquetas de los ejes
    plt.xlabel('x')
    plt.ylabel('Valor')
    
    # Título del gráfico
    plt.title('Función Sigmoide y su Derivada')
    
    # Agregar leyenda para identificar las curvas
    plt.legend()
    
    # Agregar cuadrícula para mejorar la visualización
    plt.grid(True)
    
    # Mostrar la gráfica en pantalla
    plt.show()

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    plot_sigmoid()  # Llama a la función para graficar la función sigmoide y su derivada

