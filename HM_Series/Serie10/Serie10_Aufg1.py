import numpy as np


def jacobi_procedure(d_inverse_m, l_m, r_m, current_x_m, b_m):
    return np.dot(-d_inverse_m, (np.dot((l_m + r_m), current_x_m) - b_m))


a = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
d_inverse = np.array([[1 / 8, 0, 0], [0, 1 / 9, 0], [0, 0, 1 / 7]])
l = np.array([[0, 0, 0], [5, 0, 0], [4, 2, 0]])
r = np.array([[0, 5, 2], [0, 0, 1], [0, 0, 0]])
zero_x = np.array([[1], [-1], [3]])
b = np.array([[19], [5], [34]])

x_1 = jacobi_procedure(d_inverse, l, r, zero_x, b)
x_2 = jacobi_procedure(d_inverse, l, r, x_1, b)
x_3 = jacobi_procedure(d_inverse, l, r, x_2, b)
x_4 = jacobi_procedure(d_inverse, l, r, x_3, b)
x_5 = jacobi_procedure(d_inverse, l, r, x_4, b)
x_6 = jacobi_procedure(d_inverse, l, r, x_5, b)
x_7 = jacobi_procedure(d_inverse, l, r, x_6, b)
x_8 = jacobi_procedure(d_inverse, l, r, x_7, b)
x_9 = jacobi_procedure(d_inverse, l, r, x_8, b)
x_10 = jacobi_procedure(d_inverse, l, r, x_9, b)
x_11 = jacobi_procedure(d_inverse, l, r, x_10, b)
x_12 = jacobi_procedure(d_inverse, l, r, x_11, b)

correct_x = np.linalg.solve(a, b)
print(x_2)
print(x_3)
print(x_3 - x_2)