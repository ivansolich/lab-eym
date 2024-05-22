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
#print(v0Ajuste, tauDescargaAjuste)
pesoTauDescarga = 1/pcov[1][1]
#print(pesoTauDescarga)
incertidumbre = np.sqrt(np.diag(pcov)) # Calculo la desv stnd con la matriz de covarianza
incertidumbreV0, incertidumbreTau = incertidumbre
#print(incertidumbreV0, incertidumbreTau)

# Media ponderada de tau

tau = np.array([tauCargaAjuste, tauDescargaAjuste])
pesos = np.array([pesoTauCarga, pesoTauDescarga])

def mediaPon(x, w):
    return (x*w).sum()/w.sum()

def devPon(w):
    return np.sqrt(1/w.sum())

mediaTau = mediaPon(tau, pesos)
incertPon = devPon(pesos)

# Valor de C

R = 46400 #ohm
C = mediaTau / R
print(C)

# Voltaje en funcion de tau

vTau = modeloDescarga(tauDescargaAjuste, v0Ajuste, tauDescargaAjuste)
#print(vTau)

# Graficacion

fix, ax = plt.subplots()

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

ax.hlines(0, 0, 300, colors="black", ls="--", label="$V_0$")
ax.plot(tiempoDescarga, voltajeDescarga, "o", color="black", markersize=4, alpha=0.5)
ax.plot(tiempoDescarga, modeloDescarga(tiempoDescarga, v0Ajuste, tauDescargaAjuste), '-', color="tab:red", markersize=4, alpha=0.5, label="Curva ajustada")
ax.plot(tauDescargaAjuste, vTau, "o", color="tab:green", markersize=4, label =r"$V(\tau)$")
plt.xlim(0, 300)

ax.legend(loc="center right")
ax.set_xlabel("Tiempo [s]")
ax.set_ylabel("Voltaje [V]")

plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img2.png",dpi=300)

plt.show()