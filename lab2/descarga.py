import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from carga import tauCargaAjuste, pesoTauCarga

plt.rcParams['text.usetex'] = True

df1 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="datos",
                    usecols="D", skiprows=range(2), nrows=61, header=None)


voltajeDescarga = df1.to_numpy().flatten().transpose()
tiempoDescarga = np.arange(0, 305, 5)


# Ajuste exponencial
def modeloDescarga(x, v0, tau):
    return v0*np.exp(-x*(1/tau))

params, pcov = sp.optimize.curve_fit(modeloDescarga, tiempoDescarga, voltajeDescarga) # Coeficientes
v0Ajuste, tauDescargaAjuste = params
pesoTauDescarga = 1/pcov[1][1]
incertidumbre = np.sqrt(np.diag(pcov)) # Calculo la desv stnd con la matriz de covarianza
incertidumbreV0, incertidumbreTau = incertidumbre

print(tauDescargaAjuste,incertidumbreTau)


# Voltaje en funcion de tau

vTau = modeloDescarga(tauDescargaAjuste, v0Ajuste, tauDescargaAjuste)


# Graficacion

fix, (ax1,ax2) = plt.subplots(1,2,figsize = (10,5), sharex=True)

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

# axis 1

ax1.plot(tiempoDescarga, voltajeDescarga, "o", color="black", markersize=4, alpha=0.5)
ax1.plot(tiempoDescarga, modeloDescarga(tiempoDescarga, v0Ajuste, tauDescargaAjuste), '-', color="tab:red", markersize=4, alpha=0.5, label="Curva ajustada")
ax1.plot(tauDescargaAjuste, vTau, "o", color="tab:green", markersize=4, label =r"$V(\tau)$")
#plt.xlim(0, 300)

ax1.legend(loc="upper right")
ax1.set_xlabel("Tiempo [s]")
ax1.set_ylabel("Voltaje [V]")



# axis 2

ax2.plot(tiempoDescarga, voltajeDescarga, "o", color="black", markersize=4, alpha=0.5)
#ax2.plot(tiempoDescarga, modeloDescarga(tiempoDescarga, v0Ajuste, tauDescargaAjuste), '-', color="tab:red", markersize=4, alpha=0.5, label="Curva ajustada")
#ax2.plot(tauDescargaAjuste, vTau, "o", color="tab:green", markersize=4, label =r"$V(\tau)$")
#plt.xlim(0, 300)

ax2.set_xlabel("Tiempo [s]")
ax2.set_ylabel("Voltaje [V]")
ax2.set_yscale("log")
ax2.set_title("Escala Log")

plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img2.png",dpi=300)

plt.show()