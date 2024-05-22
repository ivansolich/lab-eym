
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Circle


# # Función que retorna el campo Eléctrico.


def set_LaTEX_font():
    matplotlib.rcParams['mathtext.fontset']='stix'
    matplotlib.rcParams['font.family']='STIXGeneral'

def E(q, r0, x, y):
    """Retorna el vector de campo eléctrico E=(Ex,Ey) de una carga q en r0"""
    den = np.hypot(x-r0[0], y-r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den

set_LaTEX_font()

# # puntos de los ejes x e y.
nx, ny = 200, 200
x = np.linspace(-8, 8, nx)
y = np.linspace(-8, 8, ny)
X, Y = np.meshgrid(x, y)


# # Crear un multipolo con nq cargas
# count = número de q. En ese caso es 1 dipolo

nq = 80 # nq determina la longitud de los electrodos
charges = []
for i in range(nq):
    q1 = -nq+1
    charges.append((q1, (4,-4+i*(0.1))))
    q2 = nq+1
    charges.append((q2, (-6,-3.5+i*(0.075))))

# # Vector de campo eléctrico como componentes separados (Ex,Ey)
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))

for charge in charges:
    ex, ey = E(*charge, x=X, y=Y)
    Ex += ex
    Ey += ey


fig = plt.figure()
ax = fig.add_subplot(111)


# # Dibujar las líneas de flujo con mapa de colores y estilos apropiados.

color = 1 * np.log(np.hypot(Ex, Ey))

ax.streamplot(
    x, y, Ex, Ey, color = color, linewidth = 1,
    cmap = plt.cm.autumn, density = 0.4,
    arrowstyle = '->', arrowsize = 1, broken_streamlines = False, zorder = -1)


# # Agregar circulos para las cargas.

charge_colors = {True: 'black', False: 'black'}
for q, pos in charges:
    ax.add_artist(Circle(pos, 0.15, color = charge_colors[q>0]))


x1=[0,0,0,0,-0.2,-0.3,-0.1,-0.2,-0.2,-0.3,-0.4]
y1=[0,1,2,3,5,6,-1,-2,-3,-5,-6]

x2=[2,2,2.1,2.2,2.4,2.5,1.9,1.8,2.1,2.5,2.3]
y2=[0,1,2,3,4,5,-1,-2,-3,-5,-4]

x3=[-2,-2,-2.1,-2.2,-2.4,-2.7,-2.2,-2.2,-2.3,-2.7]
y3=[0,1,2,3,4,5,-1,-2,-3,-5]

x4=[-4,-4.1,-4.2,-4.2,-4.5,-4,-4.2,-4.4,-4.6]
y4=[0,1,2,3,4,-1,-2,-3,-4]

x5=[-1,-1,-1,-1.2,-1.1,-1.4,-1.1,-1.1,-1.1,-1.2,-1.3]
y5=[0,1,2,4,3,5,-1,-2,-3,-4,-5]

x6=[1,1.1,1.2,1.3,1.3,1.3,0.9,1,1.1,1.3,1.4]
y6=[0,1,2,3,4,5,-1,-2,-3,-4,-5]

v1 = plt.plot(x1, y1, 'o',color="black",label="V1")
v2 = plt.plot(x2, y2, 'o',color="black",label="V2")
v3 = plt.plot(x3, y3, 'd',color="black",label="V3")
v4= plt.plot(x4, y4, '^',color="black",label="V4")
v5 = plt.plot(x5, y5, 's',color="black",label="V5")
v6 = plt.plot(x6, y6, 'v',color="black",label="V6")


# # Graficar
ax.set_xlabel('$x$ [cm]')
ax.set_ylabel('$y$ [cm]')
ax.set_xlim(-8,8)
ax.set_ylim(-8,8)
ax.set_aspect('equal')

plt.legend()
#plt.grid()
ax.legend(bbox_to_anchor=(1.05, 0.7))

plt.show()

#plt.savefig("F:\Facultad\Laboratorios\EyM\Lab1\graficos\img2.png")


#import subprocess # me permite utilizar comandos de la terminal
#subprocess.run(['ps2eps', '-B', '-f', 'F:\Facultad\Laboratorios\EyM\Lab1\graficos\img2.png']) # ps2eps -B -f figuras/lineasCampo.ps es para transformar de .ps a .eps

#plt.show()