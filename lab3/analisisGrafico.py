import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
import math

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

df5 = pd.read_excel(r"datos3.xlsx", sheet_name="area",
                    usecols="C", skiprows=range(1), nrows=1, header=None)

df6 = pd.read_excel(r"datos3.xlsx", sheet_name="datos",
                    usecols="D", skiprows=range(24), nrows=21, header=None)

V1 = df1.to_numpy().flatten().transpose()
V2 = df2.to_numpy().flatten().transpose()
V3 = df3.to_numpy().flatten().transpose()

sigmaV1 = df6.to_numpy().flatten().transpose()
sigmaV1 = sigmaV1[1:]

longitud = np.arange(0, 1.05, 0.05)

area = df4.to_numpy().flatten().transpose()
d = df5.to_numpy().flatten().transpose()

intensidad = [0.49, 0.35, 0.25]

rhoNicromo = 1*10**(-6)


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
Ierror = []
Lerror = 0.001
areaError = 0.001


def rho(V, L, I, area):
    return [(v * area) / (I * l) for v, l in zip(V, L) if l != 0 and v != 0]

def calcular_delta_rho(V, d, I, L, delta_V, delta_d, delta_I, delta_L):
    # Constante pi
    pi = np.pi

    # Términos de la propagación del error
    term1 = (pi * d ** 2 / (4 * I * L)) * delta_V
    term2 = (2 * V * pi * d / (4 * I * L)) * delta_d
    term3 = (V * pi * d ** 2 / (4 * I ** 2 * L)) * delta_I
    term4 = (V * pi * d ** 2 / (4 * I * L ** 2)) * delta_L

    term1 = np.power((term1),2)


    # Cálculo de la incertidumbre combinada
    delta_rho = np.sqrt(term1 ** 2 + term2 ** 2 + term3 ** 2 + term4 ** 2)

    return delta_rho

listaRho1 = rho(V1, longitud, intensidad[0], area)
listaRho2 = rho(V2, longitud, intensidad[1], area)
listaRho3 = rho(V3, longitud, intensidad[2], area)

V1 = V1[1:]
longitud = longitud[1:]
sigmaRho1 = calcular_delta_rho(V1,d,intensidad[0],longitud,sigmaV1,0.00001,0.0647,0.001)
print(len(V1),len(sigmaRho1))
print(sigmaRho1)

### Graficacion

# Utilizar fuente de Latex
