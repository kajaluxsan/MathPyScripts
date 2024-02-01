import numpy as np
from IT22ta_ZH07_S6_Aufg2 import gauss_procedure

# Test data
sample_A0 = np.array([[-1, 1, 1], [1, -3, -2], [5, 1, 4]])
sample_b0 = np.array([[0], [5], [3]])

sample_A1 = np.array([[1, 5, 6], [7, 9, 6], [2, 3, 4]])
sample_b1 = np.array([[29], [43], [20]])

sample_43A1 = np.array([[4, -1, -5], [-12, 4, 17], [32, -10, -41]]).astype(np.float64)
sample_43B1 = np.array([[-5], [19], [-39]]).astype(np.float64)
sample_43B12 = np.array([[6], [-12], [48]]).astype(np.float64)


sample_43A2 = np.array([[2, 7, 3], [-4, -10, 0], [12, 34, 9]]).astype(np.float64)
sample_43B2 = np.array([[25], [-24], [107]]).astype(np.float64)
sample_43B22 = np.array([[5], [-22], [42]]).astype(np.float64)


sample_43A3 = np.array([[-2, 5, 4], [-14, 38, 22], [6, -9, -27]]).astype(np.float64)
sample_43B3 = np.array([[1], [40], [75]]).astype(np.float64)
sample_43B32 = np.array([[16], [82], [-120]]).astype(np.float64)

sample_43A4 = np.array([[-1, 2, 3, 2, 5, 4, 3, -1], [3, 4, 2, 1, 0, 2, 3, 8], [2, 7, 5, -1, 2, 1, 3, 5],
                        [3, 1, 2, 6, -3, 7, 2, -2], [5, 2, 0, 8, 7, 6, 1, 3], [-1, 3, 2, 3, 5, 3, 1, 4],
                        [8, 7, 3, 6, 4, 9, 7, -9], [-3, 14, -2, 1, 0, -2, 10, 5]]).astype(np.float64)
sample_43B4 = np.array([[-11], [103], [53], [-20], [95], [78], [131], [-26]]).astype(np.float64)


def test(A, b):
    print(np.linalg.solve(A, b))
    print(gauss_procedure(A, b))


# Test result
test(sample_43A1, sample_43B1)
test(sample_43A2, sample_43B2)
test(sample_43A3, sample_43B3)
test(sample_43A4, sample_43B4)

"""
Sofern es bei den Zwischenrechnungen bzw. bei der Umwandlung in die Zeilstufenform zur Fliesskommazahlen kommmt, muss
zwingend der Datentyp der Matrix auf Float eingestellt werden. Dies führt dazu, dass die End-Resultate zwingend gerundet
sollten. Dieses Problem könnte man umgehen, indem man die jeweiligen Zahlen als Bruch speichern würde (z.B. mit der
Library fractions).
"""
