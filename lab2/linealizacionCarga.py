import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['text.usetex'] = True

df1 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="lineal",
                    usecols="A", skiprows=range(2), nrows=121, header=None)

df2 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="lineal",
                    usecols="B", skiprows=range(2), nrows=121, header=None)

# Elimino celdas indefinidas
df1 = df1.dropna()
df2 = df2.dropna()

tiempo_carga = df1.to_numpy().flatten().transpose()[:len(df2)] # Fuerzo
lineal = df2.to_numpy().flatten().transpose()

fitCoef = np.polyfit(tiempo_carga,lineal,1, full=True)
print(fitCoef)
fity = fitCoef[0]*tiempo_carga + fitCoef[1]

tau = 1/fitCoef[0]
print(tau)
interp = np.interp(8.4688,lineal,tiempo_carga)


voltaje_fuente = 14.12


##Graficacion
fix,ax = plt.subplots()

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.family']='STIXGeneral'


ax.plot(tiempo_carga, lineal, "bo", color="black", markersize=4)
ax.plot(tiempo_carga, fity, "-", color="red", markersize=4)

#ax.legend(loc="center right")
ax.set_xlabel("Tiempo [s]")
ax.set_ylabel("$ln(V_0-V)$")



plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img1.png")

plt.show()