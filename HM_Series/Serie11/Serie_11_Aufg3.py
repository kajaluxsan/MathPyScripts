"""
Created on Sun Nov 29 14:43:17 2020

Höhere Mathematik 1, Serie 11, Aufgabe 3 (Gerüst)

@author (base code): knaa
"""
import numpy as np
import matplotlib.pyplot as plt

# Given parameters from the task description
detail = 1000  # number of pixels in x and y direction
maxit = 120  # maximum n for iterations (influences how detailed the structures are shown when zooming in)
x_min, x_max = -2.0, 0.7  # minimum and maximum value of x-interval
y_min, y_max = -1.4, 1.4  # minimum and maximum value of y-interval

# Define real and imaginary axis [x_min, x_max] and [y_min, y_max]
a = np.linspace(x_min, x_max, detail, dtype=np.float64)
b = np.linspace(y_min, y_max, detail, dtype=np.float64)

B = np.zeros((detail, detail))  # for color values n

# Create the complex plane with the axes defined by a and b
[x, y] = np.meshgrid(a, b)
C = np.array(x + y * 1j, dtype=np.complex128)  # creating the plane
Z = np.zeros(C.shape, dtype=np.complex128)  # initial conditions (first iteration), Z has same dimension as C

for n in np.arange(1, maxit + 1):  # start iteration
    Z = Z ** 2 + C  # calculating Z
    expl = np.abs(Z) > 2  # finding exploded values (i.e., with an absolute value > 2)
    Z[expl] = 0  # removing from iteration
    C[expl] = 0  # removing from plane
    B[expl] = n  # saving color value n

# Preparing to plot
plt.figure(1)
B = B / np.max(B)  # dividing by max value for correct color
plt.imshow(B, extent=[x_min, x_max, y_min, y_max], origin='lower', interpolation='bilinear')  # display image
plt.colorbar()  # add color bar to understand the color mapping
plt.title('Mandelbrot Set')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.show()