from analisisGrafico import rhoNicromo, rhoGrafico, errorRhoGrafico, rhoAnalitico, errorRhoAnalitico
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

fig, ax1 = plt.subplots()

plt.errorbar(1, rhoAnalitico[0], yerr=errorRhoAnalitico[0], capsize=3, ecolor='black')
plt.plot(1, rhoAnalitico[0], 'o', color='tab:red', label='Analitico - 0.49A')

plt.errorbar(2, rhoAnalitico[1], yerr=errorRhoAnalitico[1], capsize=3, ecolor='black')
plt.plot(2, rhoAnalitico[1], 'o', color='tab:blue', label='Analitico - 0.35A')

plt.errorbar(3, rhoAnalitico[2], yerr=errorRhoAnalitico[2], capsize=3, ecolor='black')
plt.plot(3, rhoAnalitico[2], 'o', color='tab:orange', label='Analitico - 0.25A')

plt.errorbar(4, rhoGrafico[0], yerr=errorRhoGrafico[0], capsize=3, ecolor='black')
plt.plot(4, rhoGrafico[0], 'o', color='tab:cyan', label='Gráfico - 0.49A')

plt.errorbar(5, rhoGrafico[1], yerr=errorRhoGrafico[1], capsize=3, ecolor='black')
plt.plot(5, rhoGrafico[1], 'o', color='tab:green', label='Gráfico - 0.35A')

plt.errorbar(6, rhoGrafico[2], yerr=errorRhoGrafico[2], capsize=3, ecolor='black')
plt.plot(6, rhoGrafico[2], 'o', color='tab:purple', label='Gráfico - 0.25A')

plt.hlines(rhoNicromo, 0, 7, ls='--', color="black")
plt.text(0.2, 1.01 * 10 ** (-6), "Resistividad del Nicromo", fontsize=10, color="black")
plt.ylabel(r"Resistividad [$\Omega m$]")

ax1.axes.get_xaxis().set_visible(False)  # Oculta el eje x
plt.xlim([0, 7])
ax1.legend()

plt.legend()

plt.show()
