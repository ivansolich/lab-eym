import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

plt.rcParams['text.usetex'] = True

# Generaciond de datos

df1 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="datos",
                    usecols="D", skiprows=range(2), nrows=61, header=None)

tiempoDescarga = np.arange(0, 305, 5)
voltajeDescarga = df1.to_numpy().flatten().transpose()

v_tau = voltajeDescarga[-1] * 0.632  # %63,2 de carga de la fuente
interp = np.interp(8.4688, voltajeDescarga, tiempoDescarga)


# Ajuste exponencial
def modeloDescarga(x, v0, tau):
    return v0 * np.exp(-x * (1 / tau))


params, _ = sp.optimize.curve_fit(modeloDescarga, tiempoDescarga, voltajeDescarga)  # Coeficientes
v0Ajuste, tauAjuste = params
vPredicho = modeloDescarga(tiempoDescarga, v0Ajuste, tauAjuste)
residuos = voltajeDescarga - vPredicho

# Graficacion

fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2,figsize=(10.5,4))

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

ax1.hlines(0, vPredicho.min(), vPredicho.max())
ax1.plot(vPredicho, residuos, "o", color="black", markersize=4)
ax1.set_xlabel("Valores ajustados")
ax1.set_ylabel("Residuos")

ax2.hlines(0, tiempoDescarga.min(), tiempoDescarga.max())
ax2.plot(tiempoDescarga, residuos, "o", color="black", markersize=4)
ax2.set_ylabel("Residuos")
ax2.set_xlabel("Tiempo [s]")

plt.tight_layout()

plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img6.png",dpi=300)

plt.show()