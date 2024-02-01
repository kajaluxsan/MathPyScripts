import numpy as np

tolerance = 1e-6
number_digits = 6


def secant_procedure(f, x0, x1, tol, counter=0):
    y = x1 - ((x1 - x0) / (f(x1) - f(x0))) * f(x1)
    print('Iteration #' + str(counter + 1) + ': x' + str(counter + 2) + ' = ' + str(round(y, number_digits)) + ' - x' +
          str(counter + 1) + ' = ' + str(round(x1, 6)))
    if abs(y - x1) >= tol:
        secant_procedure(f, x1, y, tol, counter + 1)


def sample_func(x):
    return np.e ** (x ** 2) + x ** -3 - 10


sample_x0 = -1
sample_x1 = -1.2

secant_procedure(sample_func, sample_x0, sample_x1, tolerance)

"""
Frage zu Aufgabe 3: 
Das Newton-Verfahren benötigt zusätzlich die Ableitung, wenn diese nicht bekannt oder schwierig zu berechnen ist, wird das komplex. 
"""

