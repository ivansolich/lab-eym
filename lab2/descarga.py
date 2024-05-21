import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['text.usetex'] = True

df1 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="datos",
                    usecols="D", skiprows=range(2), nrows=61, header=None)

voltaje_descarga = df1.to_numpy().flatten().transpose()
tiempo_descarga = np.arange(0, 305, 5)

voltaje_fuente = 14.12

fix, ax = plt.subplots()

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

ax.hlines(0, 0, 300, colors="black", ls="--")
ax.plot(tiempo_descarga, voltaje_descarga, "o", color="black", alpha=0.5, markersize=4)

plt.legend(loc="center right")

plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img1.png")

plt.show()
