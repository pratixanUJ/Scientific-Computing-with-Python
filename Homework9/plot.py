# EXERCISE 9.1
# -----------------------------------------------
print('Exercise 9.1')
print('------------')

import numpy as np
import matplotlib.pyplot as plt
import math


x = np.arange(0,10.01,0.01)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)

plt.plot(x,y1,color='r',label='sin(x)',linestyle='solid')
plt.plot(x,y2,color='g',label='cos(x)',linestyle='dashed')
plt.plot(x,y3,color='b',label='exp(-x)',linestyle='dotted')
plt.legend()
plt.savefig('plot.jpg')

print('Plot saved to plot.jpg!')
