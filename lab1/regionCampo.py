import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

df1 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab1\electricidad (2).xlsx", sheet_name="datos",
                   usecols="F", skiprows=range(26), nrows=5, header=None)

df2 = pd.read_excel(r"F:\Facultad\Laboratorios\EyM\Lab1\electricidad (2).xlsx", sheet_name="datos",
                   usecols="G", skiprows=range(26), nrows=5, header=None)

campo_electrico = df1.to_numpy().flatten().transpose()
campo_electrico[0] = 140

error = df2.to_numpy().flatten().transpose()
print(error)


x1 = [-0.4, -0.3, -0.2, -0.2, -0.1, 0, 0, 0, 0, -0.2, -0.3]
y1 = [-6, -5, -3, -2, -1, 0, 1, 2, 3, 5, 6]

x2 = [2.5, 2.3, 2.1, 1.8, 1.9, 2, 2, 2.1, 2.2, 2.4, 2.5]
y2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

x3 = [-2.7, -2.3, -2.2, -2.2, -2, -2, -2.1, -2.2, -2.4, -2.7]
y3 = [-5, -3, -2, -1, 0, 1, 2, 3, 4, 5]

x4 = [-4.6, -4.4, -4.2, -4, -4, -4.1, -4.2, -4.2, -4.5]
y4 = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

x5 = [-1.3, -1.2, -1.1, -1.1, -1.1, -1, -1, -1, -1.1, -1.2, -1.4]
y5 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

x6 = [1.4, 1.3, 1.1, 1, 0.9, 1, 1.1, 1.2, 1.3, 1.3, 1.3]
y6 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


def coordenadasEje(x, y): # Extrae solamente los puntos sobre el eje x
    for i in range(len(x)):
        if y[i] == 0:
            return x[i], y[i]


P1 = coordenadasEje(x1, y1)
P2 = coordenadasEje(x2, y2)
P3 = coordenadasEje(x3, y3)
P4 = coordenadasEje(x4, y4)
P5 = coordenadasEje(x5, y5)
P6 = coordenadasEje(x6, y6)



listPuntos = [P1, P2, P3, P4, P5, P6]
sorted_listPuntos = sorted(listPuntos) # Ordena los puntos
x = []
y = np.zeros(6)
for i in range(len(sorted_listPuntos)): # Extrae los valores de x
    x.append(sorted_listPuntos[i][0])

fig, ax = plt.subplots()

colors = list(matplotlib.colors.TABLEAU_COLORS.keys())

for i in range(len(x)-1):
    plt.plot((x[i],x[i+1]), (y[i],y[i+1]),"|",ls="-",label=round(campo_electrico[i]))
    #plt.fill_between((x[i],x[i+1]), (y[i]-error[i],y[i+1]-error[i]),(y[i]+error[i],y[i+1]+error[i]),alpha=0.3)

plt.rcParams['text.usetex'] = True

ax.set_xlabel(r'$x$ [cm]')
ax.set_ylabel(r'$y$ [cm]')
plt.xlim(-7, 7)
plt.ylim(-7, 7)
ax.set_aspect("equal")
ax.legend(bbox_to_anchor=(1.05, 0.7), loc=2, borderaxespad=0.,title="[N/C]")



cir = plt.Circle((0, 0), 9, color="black", fill=False)
ax.add_artist(cir)
plt.vlines(-6, -3, 3, colors="black", lw=5)
plt.vlines(4, -5, 5, colors="black", lw=5)

plt.savefig("F:\Facultad\Laboratorios\EyM\Lab1\img2.png",dpi=250)

plt.show()


