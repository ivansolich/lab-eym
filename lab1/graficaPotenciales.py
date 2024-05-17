import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import matplotlib
from mpltools import special

#x1, y1 = map(list, zip(*sorted(zip(x1, y1), key=lambda row: row[1])))

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

fig = plt.figure()
ax = fig.add_subplot(111)

plt.rcParams['text.usetex'] = True

poli = Polynomial.fit(y4, x4, 2, domain=[min(y4), max(y4)])
fit_y, fit_x = poli.linspace(100)
plt.plot(fit_x, fit_y, color="tab:pink")
v1 = plt.plot(x4, y4, '^', color="tab:pink", label="1,47V")
plt.errorbar(x4, y4, yerr=0.2, xerr=0.2, fmt="None", color="Black")

poli = Polynomial.fit(y3, x3, 2, domain=[min(y3), max(y3)])
fit_y, fit_x = poli.linspace(100)
plt.plot(fit_x, fit_y, color="tab:blue")
v2 = plt.plot(x3, y3, 'd', color="tab:blue", label="4,28V")
plt.errorbar(x3, y3, yerr=0.2, xerr=0.2, fmt="None", color="Black")

poli = Polynomial.fit(y5, x5, 2, domain=[min(y5), max(y5)])
fit_y, fit_x = poli.linspace(100)
plt.plot(fit_x, fit_y, color="tab:orange")
v3 = plt.plot(x5, y5, 's', color="tab:orange", label="5,38V")
plt.errorbar(x5, y5, yerr=0.2, xerr=0.2, fmt="None", color="Black")

poli = Polynomial.fit(y1, x1, 2, domain=[min(y1), max(y1)])
fit_y, fit_x = poli.linspace(100)
plt.plot(fit_x, fit_y, color="tab:red")
v4 = plt.plot(x1, y1, 'o', color="tab:red", label="6,38V")
plt.errorbar(x1, y1, yerr=0.2, xerr=0.2, fmt="None", color="Black")

poli = Polynomial.fit(y6, x6, 2, domain=[min(y6), max(y6)])
fit_y, fit_x = poli.linspace(100)
plt.plot(fit_x, fit_y, color="tab:cyan")
v5 = plt.plot(x6, y6, 'v', color="tab:cyan", label="7,40V")
plt.errorbar(x6, y6, yerr=0.2, xerr=0.2, fmt="None", color="Black")

poli = Polynomial.fit(y2, x2, 2, domain=[min(y2), max(y2)])
fit_y, fit_x = poli.linspace(100)
plt.plot(fit_x, fit_y, color="tab:green")
v6 = plt.plot(x2, y2, 'o', color="tab:green", label="8,50V")
plt.errorbar(x2, y2, yerr=0.2, xerr=0.2, fmt="None", color="Black")

ax.legend(bbox_to_anchor=(1.05, 0.7), loc=2, borderaxespad=0.)

plt.plot(-6.3, 3.5, "_", color="red", markersize=15)
plt.plot(4.5, 5.5, "+", color="red", markersize=15)
cir = plt.Circle((0, 0), 9, color="black", fill=False)
ax.add_artist(cir)

ax.set_xlabel(r'$x$ [cm]')
ax.set_ylabel(r'$y$ [cm]')
ax.set(xlim=(-7, 7))
ax.set(ylim=(-7, 7))
ax.set_aspect('equal')

plt.vlines(-6, -3, 3, colors="black", lw=5)
plt.vlines(4, -5, 5, colors="black", lw=5)

plt.savefig("F:\Facultad\Laboratorios\EyM\Lab1\img1.png", dpi=300)

plt.show()
