import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

plt.rcParams['text.usetex'] = True

tau_carga = 22.2522530968308
tau_descarga = 22.242198494842533

fig, ax = plt.subplots()

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

# Gráfico principal
ax.errorbar(0.5, 479, 0.05, fmt='o', capsize=3,label='Valor obtenido')
ax.hlines(470, 0, 1, ls='--',label='Valor obtenido',color='k',alpha=0.5)
ax.fill_between([0, 1], 470*1.3, 470-470*0.3, alpha=0.3, color='tab:orange')

ax.set_ylabel(r"Capacitancia [$\mu F$]")
ax.set_xlim(0, 1)
ax.set_ylim(470-470*0.3-100, 470+470*0.3+100)
ax.legend(loc='upper left')

# Crear gráfico de inserción
ax_inset = inset_axes(ax, width="30%", height="30%", loc='upper right')
ax_inset.errorbar(0.5, 479, 0.05, fmt='o', capsize=3)
ax_inset.hlines(470, 0, 1, ls='--')
ax_inset.fill_between([0, 1], 470*1.3, 470-470*0.3, alpha=0.3, color='tab:orange')

# Ajustar límites del gráfico de inserción para mostrar el zoom
ax_inset.set_xlim(0.45, 0.55)
ax_inset.set_ylim(478.9, 479.1)


# Indicar visualmente la región de zoom
mark_inset(ax, ax_inset, loc1=2, loc2=4, fc="none", ec="0.5")

plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img8.png",dpi=300)

plt.show()