import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Calcular el gradiente
gradiente = np.gradient(y, x)

# Graficar los datos y el gradiente
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(x, y, label='Función original')
plt.title('Función original')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, gradiente, label='Gradiente')
plt.title('Gradiente')
plt.legend()

plt.tight_layout()
plt.show()
