import numpy as np
import matplotlib.pyplot as plt
import math


def minimos_cuadrados(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(x_i ** 2 for x_i in x)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_xy = 0
    mean_x = sum_x / n
    mean_y = sum_y / n

    for i in range(n):
        # Multiplicamos los elementos correspondientes de x e y y los sumamos a sum_xy
        sum_xy += x[i] * y[i]

    # Calcula la pendiente (m) y la ordenada al origen (b) utilizando las fórmulas
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x ** 2)
    b = (sum_y - m * sum_x) / n

    # Calcula los errores estándar de la pendiente (m) y de la ordenada al origen (b)
    error_m = math.sqrt(
        (sum((y[i] - (m * x[i] + b)) ** 2 for i in range(n)) / (n - 2)) * (1 / sum((x_i - mean_x) ** 2 for x_i in x)))
    error_b = math.sqrt((sum((y[i] - (m * x[i] + b)) ** 2 for i in range(n)) / (n - 2)) * (
            sum(x_i ** 2 for x_i in x) / (n * sum(x_i ** 2 for x_i in x) - sum_x ** 2)))

    # Calcula el coeficiente de determinación R^2
    ss_total = sum((y_i - mean_y) ** 2 for y_i in y)
    ss_res = sum((y[i] - (m * x[i] + b)) ** 2 for i in range(n))
    r_squared = 1 - (ss_res / ss_total)

    return m, b, error_m, error_b, r_squared
