# Importación de bibliotecas necesarias
import numpy as np  # Biblioteca para operaciones matemáticas y manejo de arreglos numéricos
import matplotlib.pyplot as plt  # Biblioteca para la generación de gráficos

# Definición de la función que grafica una función a tramos y su derivada
def plot_piecewise_func():
    """
    Función que calcula y grafica una función a tramos y su derivada.
    """

    # Definición de la función a tramos
    def piecewise_func(x):
        return np.piecewise(x, 
                            [x < -1, (x >= -1) & (x <= 1), x > 1],  # Condiciones para cada tramo
                            [lambda x: -1, lambda x: x, lambda x: 1])  # Valores correspondientes para cada tramo

    # Derivada de la función a tramos
    def piecewise_func_deriv(x):
        return np.piecewise(x, 
                            [x < -1, (x > -1) & (x < 1), x > 1],  # Se definen los intervalos donde la derivada cambia
                            [0, 1, 0])  # La derivada es 0 fuera de (-1,1) y 1 dentro del intervalo abierto (-1,1)

    # Definir el rango de valores para x
    x = np.linspace(-3, 3, 500)  # Crea un array con 500 valores equidistantes en el rango [-3, 3]
    
    # Evaluar la función a tramos en los valores de x
    y = piecewise_func(x)
    
    # Evaluar la derivada de la función a tramos en los valores de x
    y_deriv = piecewise_func_deriv(x)

    # Crear una figura para la gráfica
    plt.figure(figsize=(8, 6))  # Define el tamaño de la figura en pulgadas (8x6)
    
    # Graficar la función a tramos
    plt.plot(x, y, label='Función a tramos')  
    
    # Graficar la derivada de la función a tramos con línea punteada y color verde
    plt.plot(x, y_deriv, label='Derivada', linestyle='--', color='green')
    
    # Etiquetas de los ejes
    plt.xlabel('x')
    plt.ylabel('Valor')
    
    # Título del gráfico
    plt.title('Función a tramos y su Derivada')
    
    # Agregar leyenda para identificar las curvas
    plt.legend()
    
    # Agregar cuadrícula para mejorar la visualización
    plt.grid(True)
    
    # Mostrar la gráfica en pantalla
    plt.show()

# Verifica si el script se ejecuta directamente
if __name__ == "__main__":
    plot_piecewise_func()  # Llama a la función para graficar la función a tramos y su derivada
