# Importación de bibliotecas necesarias
import numpy as np  # Biblioteca para operaciones matemáticas y manipulación de arreglos numéricos
import matplotlib.pyplot as plt  # Biblioteca para la generación de gráficos

# Definición de la función que grafica la función identidad y su derivada
def plot_identidad():
    """
    Función que calcula y grafica la función identidad y su derivada.
    """

    # Definición de la función identidad (f(x) = x)
    def identidad(x):
        return x  # La función identidad simplemente devuelve el mismo valor de entrada
    
    # Derivada de la función identidad (f'(x) = 1 para todo x)
    def identidad_deriv(x):
        return np.ones_like(x)  # La derivada es siempre 1, por lo que se usa un arreglo lleno de unos
    
    # Definir el rango de valores para x
    x = np.linspace(-10, 10, 400)  # Crea un array con 400 valores equidistantes en el rango [-10, 10]
    
    # Evaluar la función identidad en los valores de x
    y = identidad(x)
    
    # Evaluar la derivada de la función identidad en los valores de x
    y_deriv = identidad_deriv(x)
    
    # Crear una figura para la gráfica
    plt.figure(figsize=(8, 6))  # Define el tamaño de la figura en pulgadas (8x6)
    
    # Graficar la función identidad
    plt.plot(x, y, label='Función Identidad')  
    
    # Graficar la derivada de la función identidad con línea punteada y color verde
    plt.plot(x, y_deriv, label='Derivada (Constante 1)', linestyle='--', color='green')
    
    # Etiquetas de los ejes
    plt.xlabel('x')
    plt.ylabel('Valor')
    
    # Título del gráfico
    plt.title('Función Identidad y su Derivada')
    
    # Agregar leyenda para identificar las curvas
    plt.legend()
    
    # Agregar cuadrícula para mejorar la visualización
    plt.grid(True)
    
    # Mostrar la gráfica en pantalla
    plt.show()

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    plot_identidad()  # Llama a la función para graficar la función identidad y su derivada
