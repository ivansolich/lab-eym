from analisisGrafico import rhoNicromo,rhoGrafico,errorRhoGrafico,rhoAnalitico,errorRhoAnalitico
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

fig, ax1 = plt.subplots()

plt.hlines(rhoNicromo,0,6)

plt.errorbar(1,rhoAnalitico[0],yerr=errorRhoAnalitico[0],capsize=3,ecolor='black')
plt.plot(1,rhoAnalitico[0],'o',color='tab:red',label='Analitico - 0.49A')

plt.errorbar(2,rhoAnalitico[1],yerr=errorRhoAnalitico[1],capsize=3,ecolor='black')
plt.plot(2,rhoAnalitico[1],'o',color='tab:blue',label='Analitico - 0.35A')

plt.errorbar(3,rhoAnalitico[2],yerr=errorRhoAnalitico[2],capsize=3,ecolor='black')
plt.plot(3,rhoAnalitico[2],'o',color='tab:orange',label='Analitico - 0.25A')

plt.errorbar(4,rhoGrafico[0],yerr=errorRhoGrafico[0],capsize=3,ecolor='black')
plt.plot(4,rhoGrafico[0],'o',color='tab:orange',label='Analitico - 0.25A')

plt.errorbar(5,rhoGrafico[1],yerr=errorRhoGrafico[1],capsize=3,ecolor='black')
plt.plot(5,rhoGrafico[1],'o',color='tab:orange',label='Analitico - 0.25A')

plt.errorbar(6,rhoGrafico[2],yerr=errorRhoGrafico[2],capsize=3,ecolor='black')
plt.plot(6,rhoGrafico[2],'o',color='tab:orange',label='Analitico - 0.25A')



plt.legend()

plt.show()


