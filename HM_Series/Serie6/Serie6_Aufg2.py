import numpy as np


def gauss_procedure(A, b):
    n_A = A.shape[0]
    m_A = A.shape[1]
    m_b = b.shape[1]
    print("Matrix dimension: " + str(n_A) + " x " + str(m_A))
    i = 0
    j = 0
    x = []
    reference_index = 0

    while j < m_A - 1:
        reference_index_has_been_set = False
        while i < n_A:
            current_number = A[i][j]
            # Element has 0 --> go to next line
            if current_number == 0:
                i += 1
                continue
            elif not reference_index_has_been_set:
                reference_index_has_been_set = True
                reference_index = i
            else:
                k = -1 * current_number / A[reference_index][j]
                calculate_next_number(A, i, k, m_A, reference_index)
                calculate_next_number(b, i, k, m_b, reference_index)

            i += 1
        i = reference_index + 1
        j += 1

    i_index = n_A - 1
    j_index = m_A - 1

    det = -1

    while j_index >= 0:

        current_element = A[i_index][j_index]
        result_element = b[i_index]
        for id_element, element in enumerate(x):
            result_element = result_element - (A[i_index][j_index + id_element + 1] * x[-1 - id_element])
        # x.append(round(float(result_element / current_element)))
        x.append(float(result_element / current_element))

        j_index -= 1
        i_index -= 1
        det *= current_element

    print("Matrix row level form:")
    print("A: " + str(A))
    print("b: " + str(b))
    for i in range(len(x)):
        print("x" + str(i + 1) + ": " + str(x[len(x) - i - 1]))

    print("Determinant: " + str(round(det)))
    return x


def calculate_next_number(M, i, k, m, reference_index):
    for index_column in np.arange(m):
        M[i][index_column] += k * M[reference_index][index_column]

# Test data
# Sample #1
# sample_A = np.array([[-1, 1, 1], [1, -3, -2], [5, 1, 4]])
# sample_b = np.array([[0], [5], [3]])
# gauss_procedure(sample_A, sample_b)
#
# # Sample #2
# sample_A1 = np.array([[1, 5, 6], [7, 9, 6], [2, 3, 4]]).astype(np.float64)
# sample_b1 = np.array([[29], [43], [20]]).astype(np.float64)
# gauss_procedure(sample_A1, sample_b1)
#
# # Sample #A1 from 4.3
# sample_43A1 = np.array([[4, -1, -5], [-12, 4, 17], [32, -10, -41]]).astype(np.float64)
# sample_43B1 = np.array([[-5], [19], [-39]]).astype(np.float64)
# gauss_procedure(sample_43A1, sample_43B1)
