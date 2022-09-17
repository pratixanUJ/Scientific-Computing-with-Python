import numpy as np
import matplotlib.pyplot as plt

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
def converge(c,iter):
    z = 0 #initial point
    j = 0
    while j<=iter:
        z = z**2 + c
        j+= 1
    return abs(z) <= 2


c = complex_grid(-2,1,-2,2,grid_points=1024) #creating the grid of complex numbers to be used for generating the set

# Plotting
plt.imshow(converge(c,iter=50), cmap = "RdBu")
plt.axis("off")
plt.title("Mandelbrot Set")
plt.show()
plt.savefig("Mandelbrot.jpg")
