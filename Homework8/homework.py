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


if v1.shape[0] % 2 != 0:
    v2 = np.zeros(int((v1.shape[0]-1)/2),dtype=int)
else:
    v2 = np.zeros(int(v1.shape[0]/2),dtype=int)

for idx, item in np.ndenumerate(v2): 
    i = idx[0]
    v2[i] = v1[2*i+1]

print('(b) v2 = {}'.format(v2))

v3 = np.zeros(v1.shape[0],dtype=int)
for idx, item in np.ndenumerate(v3):
    i = idx[0]
    v3[i] = v1[v1.shape[0]-1-i]

print('(c) v3 = {}'.format(v3))


# EXERCISE 8.3
# -----------------------------------------------
print('Exercise 8.3')
print('------------')

m1 = np.random.randint(10,size=(4,5))
print('(a) m1 = \n{}\n'.format(m1))

m2 = np.zeros((4,5),dtype=int)

for idx, item in np.ndenumerate(m1):
    i = idx[0]
    j = idx[1]
    m2[i][j] = m1[i][m1.shape[1]-1-j]

print('(b) m2 = \n{}\n'.format(m2))

m3 = np.zeros((4,5),dtype=int)

for idx, item in np.ndenumerate(m1):
    i = idx[0]
    j = idx[1]
    m3[i][j] = m1[m1.shape[0]-1-i][j]

print('(c) m3 = \n{}\n'.format(m3))

m1_1=np.delete(m1,0,0)
m1_2=np.delete(m1_1,2,0)
m1_3=np.delete(m1_2,0,1)
m1_new=np.delete(m1_3,3,1)
        
print('(d) New matrix after cutoff = \n{}\n'.format(m1_new))

