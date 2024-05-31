from analisisGrafico import rhoNicromo,rho1,rho2,rho3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

fig, ax1 = plt.subplots()

plt.hlines(rhoNicromo,0,300)
plt.plot(50,rho1,'o')
plt.plot(100,rho2,'o')
plt.plot(150,rho3,'o')
plt.xlim(0,300)

plt.show()


