import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

plt.rcParams['text.usetex'] = True

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['text.usetex'] = True

df1 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="lineal",
                    usecols="A", skiprows=range(2), nrows=121, header=None)

df2 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="lineal",
                    usecols="C", skiprows=range(2), nrows=121, header=None)

# Elimino celdas indefinidas
df1 = df1.dropna()
df2 = df2.dropna()

tiempo_carga = df1.to_numpy().flatten().transpose()[:len(df2)] # Fuerzo
lineal = df2.to_numpy().flatten().transpose()

def func(x,a):
    return a*x

fit = sp.optimize.curve_fit(func, tiempo_carga, lineal)


#Graficacion
fix,ax = plt.subplots()

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.family']='STIXGeneral'



ax.plot(tiempo_carga, lineal, "bo", color="black", markersize=4)
ax.plot(tiempo_carga, (-0.0372*tiempo_carga - 0.3356), color="tab:red")


ax.set_xlabel("Tiempo [s]")
ax.set_ylabel(r"$ln(V/V_0)$")


plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img4.png")

plt.show()