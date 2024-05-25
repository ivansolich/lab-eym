import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

plt.rcParams['text.usetex'] = True

# Generaciond de datos

df1 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="datos",
                    usecols="B", skiprows=range(2), nrows=121, header=None)

tiempoCarga = np.arange(0, 605, 5)
voltajeCarga = df1.to_numpy().flatten().transpose()


# Ajuste exponencial
def modeloCarga(x, a, tau):
    return a * (1 - np.exp(-(1/tau) * x))

params,_ = sp.optimize.curve_fit(modeloCarga, tiempoCarga, voltajeCarga) # Coeficientes
v0Ajuste, tauAjuste = params
vPredicho = modeloCarga(tiempoCarga, v0Ajuste, tauAjuste)
residuos = voltajeCarga - vPredicho
mediaResiduos = np.mean(residuos)


# Graficacion

fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2,figsize=(10.5,4))

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

ax1.hlines(0, vPredicho.min(), vPredicho.max())
ax1.plot(vPredicho, residuos, "o", color="black", markersize=4)
ax1.set_xlabel("Valores Ajustados")
ax1.set_ylabel("Residuos")
#ax1.set_ylim([residuos.min()-0.11, residuos.max()+0.01])

ax2.hlines(0, tiempoCarga.min(), tiempoCarga.max())
ax2.plot(tiempoCarga, residuos, "o", color="black", markersize=4)
ax2.set_ylabel("Residuos")
ax2.set_xlabel("Tiempo [s]")

plt.tight_layout()

plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img5-1.png",dpi=300)

plt.show()