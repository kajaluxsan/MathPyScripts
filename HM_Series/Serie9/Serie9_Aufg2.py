import numpy as np

def berechne_fehler(A, b, A_tilde, b_tilde):
    x = np.linalg.solve(A,b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)

    cond_A = np.linalg.cond(A, np.inf)

    dx_max = (cond_A / (1 - cond_A * (np.linalg.norm(A - A_tilde, np.inf) / np.linalg.norm(A, np.inf)))) * ((np.linalg.norm(A - A_tilde, np.inf) / np.linalg.norm(A, np.inf)) + (np.linalg.norm(b - b_tilde, np.inf) / np.linalg.norm(b, np.inf)))

    dx_obs = (np.linalg.norm(x-x_tilde, np.inf)/np.linalg.norm(x, np.inf))

    if (cond_A * (np.linalg.norm(A - A_tilde, np.inf) / np.linalg.norm(A, np.inf))) >= 1:
       dx_max = np.nan

    return x, x_tilde, dx_max, dx_obs


A_matrix = np.array([[20000, 30000, 10000], [10000, 17000, 6000], [2000, 3000, 2000]])
A_tilde_matrix = np.array([[19900, 29900, 9900], [9900, 16900, 5900], [1900, 2900, 1900]])
b_vector = np.array([[5720000], [3300000], [836000]])
b_tilde = np.array([[5820000], [3400000], [936000]])

x, x_tilde, dx_max, dx_obs = berechne_fehler(A_matrix, b_vector, A_tilde_matrix, b_tilde)

print(f'Original x:\n{x}\n')
print(f'Gestörtes x_tilde:\n{x_tilde}\n')
print(f'Maximaler relativer Fehler (dx_max): {dx_max:.2e}' if not np.isnan(dx_max) else 'Maximaler relativer Fehler (dx_max): NaN')
print(f'Beobachteter relativer Fehler (dx_obs): {dx_obs:.2e}\n')