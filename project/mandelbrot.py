import numpy as np
import matplotlib.pyplot as plt
import sys
import agrparse

#To avoid warnings thrown due to vectorization
np.warnings.filterwarnings("ignore")

# Defining the recursion relation for the Mandelbrot set: z(i)=z(i-1)**2 + C
def z(i,C):
    if i==0:
        return 0
    else:
        return z(i-1,C)**2 + C

# Defining a grid over which the mandelbrot set will be generated
def complex_grid(xmin, xmax, ymin, ymax, grid_points):
    Re = np.linspace(xmin, xmax, int((xmax-xmin)*grid_points))
    Im = np.linspace(ymin, ymax, int((ymax-ymin)*grid_points))
    return Re[np.newaxis,:]+Im[:,np.newaxis]*1j

# Checking convergence of the complex point C
def converge(c,num_iter):
    z = 0 #initial point
    j = 0
    while j<=num_iter:
        z = z**2 + c
        j+= 1
    return abs(z) <= 2

#Passing the parameter values as arguments
parser = argparse.ArgumentParser(description='Argument parameters to generate the Mandelbrot Set')
parser.add_argument('-N',type=int,help='No. of iterations to run')
parser.add_argument('-d',type=int,help='No. of grid points')
args = parser.parse_args()

c = complex_grid(-2,1,-2,2,args.d) #creating the grid of complex numbers to be used for generating the set

# Plotting
plt.imshow(converge(c,args.N), cmap = "binary")
plt.axis("off")
plt.title("Mandelbrot Set")
plt.savefig("Mandelbrot.jpg")
