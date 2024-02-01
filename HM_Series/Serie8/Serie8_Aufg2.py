"""
Created on Sat Nov  7 13:26:09 2020

Höhere Mathematik 1, Serie 8, Gerüst für Aufgabe 2

Description: calculates the QR factorization of A so that A = QR
Input Parameters: A: array, n*n matrix
Output Parameters: Q : n*n orthogonal matrix
                   R : n*n upper right triangular matrix            
Remarks: none
Example: A = np.array([[1,2,-1],[4,-2,6],[3,1,0]]) 
        [Q,R]=Serie8_Aufg2(A)

@author: knaa
"""

import numpy as np
import timeit


def Name_S8_Aufg2(A):

    A = np.copy(A)
    A = A.astype('float64')

    n = np.shape(A)[0]

    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square')

    Q = np.eye(n)
    R = A

    for j in range(n - 1):
        a = np.copy(R[j:, j]).reshape(n - j, 1)
        e = np.eye(n - j)[:, 0].reshape(n - j, 1)

        length_a = np.linalg.norm(a)
        sig = 1 if a[0] >= 0 else -1

        v = a + sig * length_a * e
        u = v / np.linalg.norm(v)
        H = np.eye(n - j) - 2 * np.outer(u, u)

        Qi = np.eye(n)
        Qi[j:, j:] = H
        R = np.dot(Qi, R)
        Q = np.dot(Q, Qi.T)

    return Q, R


# Matrix A aus Aufgabe 1
A = np.array([[1, -2, 3], [-5, 4, 1], [2, -1, 3]])

# Laufzeitmessung für die eigene Funktion
t1 = timeit.repeat("Name_S8_Aufg2(A)", "from __main__ import Name_S8_Aufg2, A", number=100)
avg_t1 = np.average(t1) / 100

# Laufzeitmessung für numpy.linalg.qr()
t2 = timeit.repeat("np.linalg.qr(A)", "from __main__ import np, A", number=100)
avg_t2 = np.average(t2) / 100

# Kommentar zu den Laufzeiten
print("Durchschnittliche Laufzeit meiner Funktion: ", avg_t1)
print("Durchschnittliche Laufzeit von numpy.linalg.qr(): ", avg_t2)
#  numpy.linalg.qr ist  schneller als unsere eigene Funktion.

# Laufzeitvergleich mit einer 100 x 100 Matrix
Test = np.random.rand(100, 100)

t1 = timeit.repeat("Name_S8_Aufg2(Test)", "from __main__ import Name_S8_Aufg2, Test", number=100)
avg_t1 = np.average(t1) / 100

t2 = timeit.repeat("np.linalg.qr(Test)", "from __main__ import np, Test", number=100)
avg_t2 = np.average(t2) / 100

print("Durchschnittliche Laufzeit meiner Funktion (100x100 Matrix): ", avg_t1)
print("Durchschnittliche Laufzeit von numpy.linalg.qr() (100x100 Matrix): ", avg_t2)
#Der Unterschied der Laufzeit wird bei grösseren Matrixen deutlicher.
