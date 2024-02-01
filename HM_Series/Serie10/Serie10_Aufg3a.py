import numpy as np

def IT22ta_ZH07_S10_Aufg3a(A, b, x0, tol, opt):
    x = x0.copy()
    x_prev = x0.copy()
    iteration = 0
    max_iterations = 1000

    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)

    while iteration < max_iterations:
        if opt == 'Jacobi':
            x = np.linalg.inv(D) @ (b - (L + U) @ x_prev)
        elif opt == 'Gauss-Seidel':
            x = np.linalg.inv(D + L) @ (b - U @ x_prev)
        else:
            raise ValueError("Unbekanntes Verfahren: Wählen Sie 'Jacobi' oder 'Gauss-Seidel'")

        if np.linalg.norm(x - x_prev, np.inf) < tol:
            break

        x_prev = x.copy()
        iteration += 1

    n2 = np.log(tol / np.linalg.norm(x - x0, np.inf)) / np.log(np.linalg.norm(D - A, np.inf))

    return x, iteration, n2

