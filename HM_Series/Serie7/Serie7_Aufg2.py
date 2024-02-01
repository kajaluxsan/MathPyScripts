import scipy
import numpy as np

matrix_a = np.array([[2, 3, 4], [0.8, 2.2, 3.6], [1.2, 2, 5.8]])

print(scipy.linalg.lu(matrix_a, True))
