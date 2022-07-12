# EXERCISE 8.1
# -----------------------------------------------
print('Exercise 8.1')
print('------------')

import numpy as np

arr1 = np.arange(0.0,1.1,0.1)
print('(a) Array with float from 0.0 to 1.0: {}\nShape = {}\n'.format(arr1,arr1.shape))

arr2 = np.zeros((5,6),dtype=int)
print('(b) Array with int zeros:\n {}\nShape = {}\n'.format(arr2,arr2.shape))

# EXERCISE 8.2
# -----------------------------------------------
print('Exercise 8.2')
print('------------')

v1 = np.array([1, 3, -2, 2, 8, -4, 0])
print('(a) v1 = {}'.format(v1))

v2 = v1[1::2]
print('(b) v2 = {}'.format(v2))

v3 = v1[::-1]
print('(c) v3 = {}'.format(v3))


# EXERCISE 8.3
# -----------------------------------------------
print('Exercise 8.3')
print('------------')

m1 = np.arange(20).reshape((4,5))
print('(a) m1 = \n{}\n'.format(m1))

m2 = m1[:,::-1]
print('(b) m2 = \n{}\n'.format(m2))

m3 = m1[::-1,:]
print('(c) m3 = \n{}\n'.format(m3))

m4 = m1[1:3,1:4]
print('(d) New matrix after cutoff = \n{}\n'.format(m4))

