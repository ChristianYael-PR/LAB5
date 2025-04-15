# Laboratorio 5: Divide y Vencerás

## Descripción

Este proyecto implementa y compara tres algoritmos de multiplicación de matrices cuadradas `n x n`, donde `n` es una potencia de 2:

- Método Tradicional
- Método Divide and Conquer (DaC)
- Método de Strassen

El objetivo es observar cómo varía el rendimiento de cada método en función del tamaño de la matriz y determinar experimentalmente a partir de qué tamaño se observan diferencias significativas entre ellos.

---

## Estructura del Proyecto

- `traditional.py`: Implementación del algoritmo tradicional `O(n^3)`.
- `dac.py`: Implementación del algoritmo por Divide and Conquer.
- `strassen.py`: Implementación del algoritmo de Strassen `O(n^log7)`.
- `main.py`: Generación de matrices, ejecución de los algoritmos y medición de tiempos.

---

## Requisitos

- Python 3.x
- NumPy

Instalación de dependencias:

```bash
pip install numpy

n | Tradicional (s) | Divide y vencerás (s) | Strassen (s)
2 | 0.000022 | 0.000049 | 0.000054
4 | 0.000071 | 0.000187 | 0.000193
8 | 0.000280 | 0.001168 | 0.001309
16 | 0.002258 | 0.008504 | 0.009095
32 | 0.017488 | 0.069831 | 0.063431
64 | 0.150722 | 0.571104 | 0.461203
128 | 1.168715 | 4.356102 | 3.085846
