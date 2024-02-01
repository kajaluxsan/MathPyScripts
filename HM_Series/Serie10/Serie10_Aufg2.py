import numpy as np
np.set_printoptions(precision=4, suppress=True)


def calculate_gauss_seidel(L, D, R, b, expected_iterations, start_x):

    current_x = start_x
    DL_inverse = np.linalg.inv(np.add(D, L))

    for i in range(expected_iterations):
        new_x =  np.add(np.dot( -DL_inverse, np.dot(R, current_x)) , np.dot(DL_inverse, b))
        current_x = new_x
        print(  f'i:\n{i + 1}\n' + f'x:\n{current_x }\n')


a = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
l = np.array([[0, 0, 0], [5, 0, 0], [4, 2, 0]])
r = np.array([[0, 5, 2], [0, 0, 1], [0, 0, 0]])
d = np.diag(np.diag(a))
zero_x = np.array([[1], [-1], [3]])
b = np.array([[19], [5], [34]])

calculate_gauss_seidel(l, d, r, b, 3, zero_x )
