# Importación de bibliotecas necesarias
import numpy as np  # Biblioteca para operaciones numéricas con arreglos
import matplotlib.pyplot as plt  # Biblioteca para la creación de gráficos

# Importación de funciones de graficado desde módulos dentro de la carpeta "src"
from src.gaussiana import plot_gaussian  # Función para graficar una distribución gaussiana
from src.escalon import plot_step_function  # Función para graficar la función escalón
from src.identidad import plot_identidad  # Función para graficar la función identidad
from src.lineal_a_tramos import plot_piecewise_func  # Función para graficar una función lineal a tramos
from src.relu import plot_relu  # Función para graficar la función ReLU
from src.sigmoidal import plot_sigmoid  # Función para graficar la función sigmoide
from src.sinusoidal import plot_sinusoidal  # Función para graficar una señal sinusoidal
from src.tangente_hiperbolica import plot_tanh  # Función para graficar la tangente hiperbólica

# Definición de la función principal que ejecutará todas las funciones de graficado
def main():
    """
    Punto de entrada para ejecutar todas las funciones de graficado.
    """
    print("Generando gráficas...")  # Mensaje indicando el inicio del proceso de graficado

    # Llamado a cada una de las funciones importadas para generar las gráficas correspondientes
    plot_gaussian()
    plot_step_function()
    plot_identidad()
    plot_piecewise_func()
    plot_relu()
    plot_sigmoid()
    plot_sinusoidal()
    plot_tanh()

    print("Todas las gráficas han sido generadas correctamente.")  # Mensaje de confirmación al finalizar

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llama a la función principal si el script es ejecutado directamente
