import numpy
import math
import numba
from random import *


@numba.jit(nopython=True)
def calc_pi(pi,N_total):
    N_acc = 0
    for i in range(0, N_total):
        x = random()
        y = random()
        if math.sqrt(x**2 + y**2)<=1:
            N_acc += 1
    pi = 4*N_acc/N_total
    return pi

pi = math.pi
for N_total in [10,10**2,10**3,10**4,10**5,10**6]:
    Pi = calc_pi(pi,N_total)
    print("Total number of points = {}\nValue of Pi = {}\n".format(N_total,Pi))


