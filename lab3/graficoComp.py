from analisisResistividad import  rhoGrafico, errorRhoGrafico, rhoAnalitico, errorRhoAnalitico
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.color_palette("muted").as_hex())

plt.rcParams['text.usetex'] = True

rhoNicromo = 108.1*10**(-8) # MWS Wire - Fabricante


# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

plt.style.use('seaborn-v0_8-deep')

fig, ax1 = plt.subplots()

colors_analitico = ['#c44e52', '#8172b3', '#937860']  # azul, naranja, verde
colors_grafico = ['#797979', '#d5bb67', '#82c6e2']    # rojo, púrpura, marrón

for i in range(3):
    plt.errorbar(i+1, rhoAnalitico[i], yerr=errorRhoAnalitico[i], capsize=3, ecolor='black')
    plt.plot(i+1, rhoAnalitico[i], 'o')

for i in range(len(rhoGrafico)):
    plt.errorbar(i+4, rhoGrafico[i], yerr=errorRhoGrafico[i], capsize=3, ecolor='black')
    plt.plot(i+4, rhoGrafico[i], 'o')

# Area 100-150*10**-8
# plt.fill_between([0,7],100*10**-8,150*10**-8,alpha=0.1,label="Engineering ToolBox")

# Nicromo 75-25
plt.hlines(118*10**-8, 0, 7, ls='dotted', color="black",label="Nicromo 75-25")
#plt.text(0.5, 119.3 * 10 ** (-8), "Nicromo 70/30", fontsize=10, color="black")

# Nicromo 60-15
plt.hlines(112*10**-8, 0, 7, ls='dashdot', color="black",label="Nicromo 60-15")
#plt.text(0.5, 113.3 * 10 ** (-8), "Nicromo 60/15", fontsize=10, color="black")

# Nicromo 80-20
plt.hlines(rhoNicromo, 0, 7, ls='--', color="black",label="Nicromo 80-20")
#plt.text(0.5, 109.3 * 10 ** (-8), "Nicromo 80/20", fontsize=10, color="black")


labels = ["","0.49A","0.35A",'0.25A',"0.49A","0.35A","0.25A"]
plt.xticks(ticks=range(7), labels=labels, rotation=45, ha="right")
plt.xlim([0, 7])

plt.ylabel(r"Resistividad [$\Omega m$]")

#ax1.axes.get_xaxis().set_visible(False)  # Oculta el eje x


plt.annotate("Analítico", xy=(0.2, 1.02), xycoords='axes fraction', ha='left', fontsize=12, weight='bold')
plt.annotate("Gráfico", xy=(0.7, 1.02), xycoords='axes fraction', ha='left', fontsize=12, weight='bold')

plt.legend()

plt.savefig("F:\Facultad\Laboratorios\EyM\lab3\img1.png",dpi=300)


plt.show()