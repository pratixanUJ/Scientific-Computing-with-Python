# EXERCISE 9.2
# -----------------------------------------------
print('Exercise 9.2')
print('------------')

import numpy as np
import matplotlib.pyplot as plt
import random

Xg = []
Yg = []
Xr = []
Yr = []
areag = []
arear = []
for i in range(100):
    x = random.random()
    y = random.random()
    if x**2+y**2<1:
        Xg.append(x)
        Yg.append(y)
        areag.append(100*(x+y))
    else:
        Xr.append(x)
        Yr.append(y)
        arear.append(100*(x+y))
    
    
plt.scatter(Xg,Yg,c='g',s=areag)
plt.scatter(Xr,Yr,c='r',s=arear)
plt.savefig('Scatter.jpg')

print('Scatter plot saved to Scatter.jpg!')
