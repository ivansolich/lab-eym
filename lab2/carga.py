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

# Log scale

a,b = np.polyfit(tiempoCarga, v0Ajuste-voltajeCarga, 1)
print(a,b)

# Graficacion

if __name__ == "__main__":

    fix, (ax1,ax2) = plt.subplots(1,2,figsize = (10,5))

    # Utilizar fuente de Latex
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'

    ax1.hlines(14.12, 0, 600, colors="black", ls="--", label="$V_{0}$")
    ax1.plot(tiempoCarga, voltajeCarga, "o", color="black", markersize=4, alpha=0.5)
    ax1.plot(tiempoCarga, modeloCarga(tiempoCarga, v0Ajuste, tauCargaAjuste), '-', color="tab:red", markersize=4, alpha=0.5, label="Curva ajustada")
    ax1.plot(tauCargaAjuste, vTau, "o", color="tab:green", markersize=4, label =r"$V(\tau)$")


    ax1.legend(loc="center right")
    ax1.set_xlabel("Tiempo [s]")
    ax1.set_ylabel("Voltaje [V]")

    ax2.plot(tiempoCarga, v0Ajuste - voltajeCarga, 'o', color="black", markersize=4,alpha=0.5, label="Curva ajustada")



    ax2.set_xlabel("Tiempo [s]")
    ax2.set_ylabel("Voltaje [V]")
    ax2.set_xlim(0,250)
    ax2.set_yscale("log")
    ax2.set_title("Escala Log")

    plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img1.png",dpi=300)

    plt.show()