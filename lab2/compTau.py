import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True

tau_carga = 22.2522530968308
tau_descarga = 22.242198494842533

fig,ax = plt.subplots()

# Utilizar fuente de Latex
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'

plt.errorbar(1,tau_carga,yerr= 0.05,fmt="o",capsize=3,label="Carga")
plt.errorbar(2,tau_descarga,yerr= 0.1443664160957533,fmt="o",capsize=3,label="Descarga")

plt.xlim(0,3)
plt.ylabel(r"Constante del tiempo $\tau$")
plt.legend()

plt.savefig("F:\Facultad\Laboratorios\EyM\lab2\img7.png",dpi=300)

plt.show()