import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset
from analisisResistividad import longitud, V1, V2, V3, m1, m2, m3

# Configuración de Matplotlib para usar LaTeX y estilo
plt.rcParams['text.usetex'] = True
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.style.use('seaborn-v0_8-deep')

# Crear figura y ejes principales
fig, ax1 = plt.subplots()

# Datos
m = [m1, m2, m3]
v = [V1, V2, V3]
label = ["0.49A", "0.35A", "0.25A"]

# Graficar datos y ajustes lineales en los ejes principales
for i in range(3):
    y_fit = m[i] * longitud
    ax1.plot(longitud, y_fit, ls='-', color="black", alpha=0.5)
    ax1.scatter(longitud, v[i], alpha=0.8, s=30, label=label[i])
    ax1.errorbar(longitud, v[i], xerr=0.001, fmt='None')

# Añadir leyenda y etiquetas
ax1.legend(loc='lower right')
ax1.set_ylabel(r'Voltaje $[V]$')
ax1.set_xlabel(r'Longitud $[m]$')

# Crear un eje de inserción (zoom)
axins = inset_axes(ax1, width="30%", height="30%", loc='upper left',
                   bbox_to_anchor=(0.1,-0.05, 1, 1),
                   bbox_transform=ax1.transAxes)

# Graficar los mismos datos y ajustes lineales en el eje de inserción
for i in range(3):
    y_fit = m[i] * longitud
    axins.plot(longitud, y_fit, ls='-', color="black", alpha=0.5)
    axins.scatter(longitud, v[i], alpha=0.8, s=30, label=label[i])
    axins.errorbar(longitud, v[i], xerr=0.001, fmt='None')

# Ajustar los límites del eje x para el zoom
axins.set_xlim(0.03, 0.2)

# Ajustar los límites del eje y para el zoom
axins.set_ylim(0.03, 0.4)

# Guardar y mostrar la gráfica
plt.savefig("F:\Facultad\Laboratorios\EyM\lab3\img2.png", dpi=300)
plt.show()