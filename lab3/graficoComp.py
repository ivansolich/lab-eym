from analisisGrafico import rhoNicromo,rho1_analitico,error1Analitico,rho2_analitico,rho3_analitico,error2Analitico,error3Analitico
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

fig, ax1 = plt.subplots()

plt.hlines(rhoNicromo,0,6)

plt.plot(1,rho1_analitico,'o',color='black')
plt.errorbar(1,rho1_analitico,yerr=error1Analitico,capsize=3)

plt.plot(2,rho2_analitico,'o')
plt.errorbar(2,rho2_analitico,yerr=error2Analitico,capsize=3)

plt.plot(3,rho3_analitico,'o')
plt.errorbar(3,rho3_analitico,yerr=error3Analitico,capsize=3)



plt.show()


