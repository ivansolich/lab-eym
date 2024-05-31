import numpy as np
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

df4 = pd.read_excel(r"datos3.xlsx", sheet_name="datos",
                    usecols="G", skiprows=range(24), nrows=21, header=None)

df5 = pd.read_excel(r"datos3.xlsx", sheet_name="datos",
                    usecols="H", skiprows=range(24), nrows=21, header=None)

df6 = pd.read_excel(r"datos3.xlsx", sheet_name="datos",
                    usecols="I", skiprows=range(24), nrows=21, header=None)

V1 = df1.to_numpy().flatten().transpose()
V2 = df2.to_numpy().flatten().transpose()
V3 = df3.to_numpy().flatten().transpose()

sigmaV1 = df4.to_numpy().flatten().transpose()
sigmaV2 = df5.to_numpy().flatten().transpose()
sigmaV3 = df6.to_numpy().flatten().transpose()
sigmaV1 = sigmaV1[1:]
sigmaV2 = sigmaV2[1:]
sigmaV3 = sigmaV3[1:]

longitud = np.arange(0, 1.05, 0.05)

d = 0.000646

intensidad = [0.49, 0.35, 0.25]

rhoNicromo = 100*10**(-8)


def func(x, a):
    return a * x


m1, pcov1 = sp.optimize.curve_fit(func, longitud, V1)
m2, pcov2 = sp.optimize.curve_fit(func, longitud, V2)
m3, pcov3 = sp.optimize.curve_fit(func, longitud, V3)

### Obtencion de rho

# Metodo grafico

rho1 = (m1 * d**2 * np.pi) / (intensidad[0]*4)
rho2 = (m2 * d**2 * np.pi) / (intensidad[1]*4)
rho3 = (m3 * d**2 * np.pi) / (intensidad[2]*4)


# Metodo analitico

Lerror = 0.001
areaError = 0.001

def rho(V, L, I, d): # Funcion que calcula Rho
    return [(v * d**2 * np.pi) / (I * l * 4) for v, l in zip(V, L) if l != 0 and v != 0]

def calcular_delta_rho(V, d, I, L, delta_V, delta_d, delta_I, delta_L): # Funcion que propaga errores para rho
    pi = np.pi

    # Términos de la propagación del error
    term1 = (pi * d ** 2 / (4 * I * L)) * delta_V
    term2 = (2 * V * pi * d / (4 * I * L)) * delta_d
    term3 = (V * pi * d ** 2 / (4 * I ** 2 * L)) * delta_I
    term4 = (V * pi * d ** 2 / (4 * I * L ** 2)) * delta_L

    term1 = np.power((term1),2)
    term2 = np.power((term2),2)
    term3 = np.power((term3),2)
    term4 = np.power((term4), 2)

    # Cálculo de la incertidumbre combinada
    delta_rho = term1 + term2 + term3 + term4
    delta_rho.astype(float)

    def sqrtArray(array):
        for i in range(len(array)):
            array[i] = np.sqrt(array[i])

        return array

    return sqrtArray(delta_rho)


# Listas de rho para cada serie
listaRho1 = rho(V1, longitud, intensidad[0], d)
listaRho2 = rho(V2, longitud, intensidad[1], d)
listaRho3 = rho(V3, longitud, intensidad[2], d)

# Error de cada rho
sigmaRho1 = calcular_delta_rho(V1[1:],d,intensidad[0],longitud[1:],sigmaV1,0.00001,0.0647,0.001)
sigmaRho2 = calcular_delta_rho(V2[1:],d,intensidad[1],longitud[1:],sigmaV2,0.00001,0.0605,0.001)
sigmaRho3 = calcular_delta_rho(V3[1:],d,intensidad[2],longitud[1:],sigmaV3,0.00001,0.0575,0.001)


# Media monderada de rho para cada serie de mediciones

def mean(data,weights):
    mean_weighted = np.average(data, weights=weights)

    # Calcular la varianza ponderada
    weighted_variance = np.sum(weights * (data - mean_weighted) ** 2) / np.sum(weights)

    # Número de mediciones
    N = len(data)

    # Calcular el error estándar ponderado
    error_estandar_weighted = np.sqrt(weighted_variance / N)

    return mean_weighted, error_estandar_weighted

rho1_analitico, error1Analitico = mean(listaRho1, sigmaRho1)
rho2_analitico, error2Analitico = mean(listaRho2, sigmaRho2)
rho3_analitico, error3Analitico = mean(listaRho3, sigmaRho3)

### Graficacion

# Utilizar fuente de Latex
