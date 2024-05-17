import numpy as np
import matplotlib.pyplot as plt
import math


def minimos_cuadrados(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(x_i ** 2 for x_i in x)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_xy=0
    mean_x = sum_x / n

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

    return m, b, error_m, error_b

# Ejemplo de uso
x = [49.2,
46.2,
42.5,
39,
35.6,
31.2,
26.8,
21.7,
15.8,
13.9]
y = [49.5,
53.2,
57.3,
61.4,
65.1,
70.1,
74.9,
80.8,
87.2,
89.5]

m,b,error_m, error_b = minimos_cuadrados(x,y)
print(m,b,error_m, error_b)

