import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['text.usetex'] = True

df1 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="datos",
                    usecols="B", skiprows=range(2), nrows=121, header=None)

tiempo_carga = np.arange(0, 605, 5)
tiempo_carga_10 = np.arange(0, 610, 10)
voltaje_carga = df1.to_numpy().flatten().transpose()
voltaje_carga_10 = np.empty(0)


for i in range(len(voltaje_carga)):
    if i % 2 == 0 or i == 0:
        voltaje_carga_10 = np.append(voltaje_carga_10, voltaje_carga[i])


df2 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab2\datos.xlsx", sheet_name="datos",
                    usecols="D", skiprows=range(2), nrows=61, header=None)

voltaje_descarga = df2.to_numpy().flatten().transpose()
tiempo_descarga = np.arange(0, 305, 5)

voltaje_fuente = 14.12

#fig, (ax1,ax2) = plt.subplots(1,2,figsize = (9,4))
fix,ax = plt.subplots()

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.family']='STIXGeneral'


ax.hlines(0,0,300, colors="black",ls = "--")
#ax2.plot(tiempo_descarga, voltaje_descarga, "-", color="tab:blue")
ax.plot(tiempo_descarga, voltaje_descarga, "o", color="tab:red")

#ax1.legend(loc="center right")


plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img1.png")

plt.show()