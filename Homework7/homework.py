# EXERCISE 7.1
# -----------------------------------------------
print('Exercise 7.1')
print('------------')

from vector3D import Vector

def find_axis(v1, v2):
    v = v1.cross(v2)
    N = v.length()
    if N == 0:
        raise ValueError('The vectors v1 and v2 are parallel')
    else:
        axis = Vector(v.x/N, v.y/N, v.z/N)
        print('The axis of the vectors v1 and v2 is: {}'.format(axis))
    

V1 = Vector(1,2,-3)
V2 = Vector(3,1,-5)
find_axis(V1,V2)

# EXERCISE 7.2
# -----------------------------------------------
print('Exercise 7.2')
print('------------')

import random

def inf_a():
    i = 0
    while True:
        yield i
        i += 1
        if i == 1:
            yield i
            i-=1
            
print(inf_a())

def inf_b():
    list = [0,1]
    while True:
        yield random.choice(list)

print(inf_b())

def inf_c():
    i = 0
    while True:
        for j in range(4):
            if j == 0:
                yield i
            elif j == 1:
                yield i+1
            elif j == 2:
                yield i
            elif j == 3:
                yield i-1

print(inf_c())
                
