# EXERCISE 9.2
# -----------------------------------------------
print('Exercise 9.2')
print('------------')

import numpy as np
import matplotlib.pyplot as plt
import random

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x,y,c=np.where(x**2+y**2<1,'g','r'),s=(x+y)*100)

plt.savefig('Scatter.jpg')
print('Scatter plot saved to Scatter.jpg!')
