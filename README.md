# README - Funciones de Activación en Redes Neuronales

## Información del Proyecto
**Materia:** Sistemas de visión artificial\
**Tarea:** Tarea 2.1_Graficas de funciones de activación con su derivada\
**Estudiante:** Luis Felipe Alvarado Resendez\
**Fecha:** 03/03/2025

## Descripción General
Este repositorio contiene un conjunto de scripts en Python que grafican diversas funciones de activación junto con sus derivadas. Cada función está implementada en su propio módulo dentro de la carpeta `src/`. El archivo `main.py` es el punto de entrada para ejecutar todas las gráficas de manera conjunta.

## Funciones de Activación en Redes Neuronales
Las funciones de activación son funciones matemáticas que se aplican a las neuronas de una red neuronal para introducir no linealidad en el modelo. Sin ellas, la red neuronal simplemente actuaría como una combinación lineal de sus entradas, lo que limitaría su capacidad para resolver problemas complejos como clasificación de imágenes, reconocimiento de voz o traducción automática.

En términos simples, una función de activación:
- Recibe una entrada numérica proveniente de la capa anterior.
- Transforma esa entrada en un valor de salida, generalmente en un rango específico.
- Permite que la red neuronal aprenda relaciones complejas entre los datos de entrada y salida.

## Requisitos Previos
Antes de ejecutar el código, asegúrate de tener instaladas las siguientes bibliotecas en tu entorno de Python:
```bash
pip install numpy matplotlib
```

## Estructura del Repositorio
```
📂 proyecto_funciones/
├── 📂 src/                            # Código fuente
│   ├── escalon.py                     # Función Escalón
│   ├── gaussiana.py                   # Función Gaussiana
│   ├── identidad.py                    # Función Identidad
│   ├── lineal_a_tramos.py             # Función Lineal a Tramos
│   ├── relu.py                         # Función ReLU
│   ├── sigmoidal.py                    # Función Sigmoide
│   ├── sinusoidal.py                   # Función Sinusoidal
│   ├── tangente_hiperbolica.py         # Función Tangente Hiperbólica
├── main.py                             # Punto de entrada para ejecutar todas las funciones
├── README.md                           # Este documento
```

## Explicación del Código

### 1. `main.py`
Este archivo se encarga de importar y ejecutar todas las funciones de graficado. Contiene la función `main()`, que llama a cada una de las funciones definidas en los módulos de `src/`.
```python
from src.gaussiana import plot_gaussian
from src.escalon import plot_step_function
from src.identidad import plot_identidad
from src.lineal_a_tramos import plot_piecewise_func
from src.relu import plot_relu
from src.sigmoidal import plot_sigmoid
from src.sinusoidal import plot_sinusoidal
from src.tangente_hiperbolica import plot_tanh
```

### 2. Funciones Implementadas
Cada función implementada genera una gráfica de la función de activación correspondiente junto con su derivada.

#### **a) Función Escalón** (`escalon.py`)
Representa la función de Heaviside, que es una función discontinua.
```python
def step_function(x):
    return np.where(x < 0, 0, 1)
```

#### **b) Función Gaussiana** (`gaussiana.py`)
Modelo de distribución normal con su derivada.
```python
def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-x**2 / 2)
```

#### **c) Función Identidad** (`identidad.py`)
Función lineal `f(x) = x` y su derivada constante `f'(x) = 1`.
```python
def identidad(x):
    return x
```

#### **d) Función Lineal a Tramos** (`lineal_a_tramos.py`)
Define una función por partes con distintos valores de pendiente.
```python
def piecewise_func(x):
    return np.piecewise(x, [x < -1, (x >= -1) & (x <= 1), x > 1], [-1, lambda x: x, 1])
```

#### **e) Función ReLU** (`relu.py`)
Función Rectified Linear Unit (ReLU), usada en redes neuronales.
```python
def relu(x):
    return np.maximum(0, x)
```

#### **f) Función Sigmoide** (`sigmoidal.py`)
Transforma cualquier valor real en el rango (0,1).
```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

#### **g) Función Sinusoidal** (`sinusoidal.py`)
Genera una onda senoidal y su derivada coseno.
```python
def sin_func(x):
    return np.sin(x)
```

#### **h) Función Tangente Hiperbólica** (`tangente_hiperbolica.py`)
Transformación no lineal que oscila entre (-1,1).
```python
def tanh_func(x):
    return np.tanh(x)
```

## Cómo Ejecutar el Código
Para ejecutar el código y generar todas las gráficas, usa el siguiente comando:
```bash
python main.py
```
Se generarán y mostrarán las gráficas de cada función con su respectiva derivada.

## Resultados Esperados
El programa generará ocho gráficas, cada una mostrando la función de activación y su derivada correspondiente.

## Conclusión
Este proyecto ilustra cómo graficar funciones de activación y sus derivadas utilizando NumPy y Matplotlib. Puede servir como base para estudios de análisis matemático, redes neuronales y transformaciones en señales.

---

¡Gracias por revisar este proyecto! Si tienes dudas o sugerencias, abre un issue en el repositorio. 🚀

