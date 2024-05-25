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
def modeloCarga(x, v0, tau):
    return v0 * (1 - np.exp(-(1/tau) * x))

params, pcov = sp.optimize.curve_fit(modeloCarga, tiempoCarga, voltajeCarga) # Coeficientes
v0Ajuste, tauCargaAjuste = params

pesoTauCarga = 1/pcov[1][1]

incertidumbre = np.sqrt(np.diag(pcov)) # Calculo la desv stnd con la matriz de covarianza
incertidumbreV0, incertidumbreTau = incertidumbre

"""if __name__ == "__main__":
    print(v0Ajuste, tauCargaAjuste)
    print(pesoTauCarga)
    print(incertidumbreV0, incertidumbreTau)"""

# Voltaje en funcion de tau

vTau = modeloCarga(tauCargaAjuste, v0Ajuste, tauCargaAjuste) # Esto corresponderia al 63,2% de la carga

# Graficacion

if __name__ == "__main__":

    fix, ax = plt.subplots()

    # Utilizar fuente de Latex
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'

    ax.hlines(14.12, 0, 600, colors="black", ls="--", label="$V_{0}$")
    ax.plot(tiempoCarga, voltajeCarga, "o", color="black", markersize=4, alpha=0.5)
    ax.plot(tiempoCarga, modeloCarga(tiempoCarga, v0Ajuste, tauCargaAjuste), '-', color="tab:red", markersize=4, alpha=0.5, label="Curva ajustada")
    ax.plot(tauCargaAjuste, vTau, "o", color="tab:green", markersize=4, label =r"$V(\tau)$")

    plt.xlim(0, 600)
    ax.legend(loc="center left")
    ax.set_xlabel("Tiempo [s]")
    ax.set_ylabel("Voltaje [V]")
    plt.yscale("log")

    plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img1.png",dpi=300)

    plt.show()