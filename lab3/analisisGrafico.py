import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

plt.rcParams['text.usetex'] = True

# Generaciond de datos

df1 = pd.read_excel(r"datos3.xlsx", sheet_name="datos",
                    usecols="E", skiprows=range(1), nrows=21, header=None)

df2 = pd.read_excel(r"datos3.xlsx", sheet_name="datos",
                    usecols="I", skiprows=range(1), nrows=21, header=None)

df3 = pd.read_excel(r"datos3.xlsx", sheet_name="datos",
                    usecols="M", skiprows=range(1), nrows=21, header=None)

df4 = pd.read_excel(r"datos3.xlsx", sheet_name="area",
                    usecols="D", skiprows=range(1), nrows=1, header=None)

V1 = df1.to_numpy().flatten().transpose()
V2 = df2.to_numpy().flatten().transpose()
V3 = df3.to_numpy().flatten().transpose()

longitud = np.arange(0, 1.05, 0.05)

area = df4.to_numpy().flatten().transpose()

intensidad = [0.49, 0.35, 0.25]


def func(x, a):
    return a * x


m1, pcov1 = sp.optimize.curve_fit(func, longitud, V1)
m2, pcov2 = sp.optimize.curve_fit(func, longitud, V2)
m3, pcov3 = sp.optimize.curve_fit(func, longitud, V3)

### Obtencion de rho

# Metodo grafico

rho1 = (m1 * area) / intensidad[0]
rho2 = (m2 * area) / intensidad[1]
rho3 = (m3 * area) / intensidad[2]


# Metodo analitico

Verror = 0.001
Ierror = 0.01
Lerror = 0.001
areaError = 0.001


def rho(V, L, I, area):
    return [(v * area) / (I * l) for v, l in zip(V, L) if l != 0 and v != 0]


def rhoError(V, L, I, area, Verror, Lerror, Ierror, areaError):
    return [np.sqrt(((area * Verror) / (I * L)) ** 2 + ((V * areaError) / (I * L)) ** 2 + (
                (-V * area * Ierror) / (L * np.power(I, 2))) ** 2 + ((-V * area * Lerror) / (I * np.power(L, 2))) ** 2)]


listaRho1 = rho(V1, longitud, intensidad[0], area)
listaRho2 = rho(V2, longitud, intensidad[1], area)
listaRho3 = rho(V3, longitud, intensidad[2], area)

errorRho1 = rhoError(V1, longitud, intensidad[0], area, Verror, Lerror, Ierror, areaError)

mean = np.mean(listaRho1)
print(rho1, rho2, rho3)
print(listaRho1)
print(errorRho1)

### Graficacion

# Utilizar fuente de Latex
