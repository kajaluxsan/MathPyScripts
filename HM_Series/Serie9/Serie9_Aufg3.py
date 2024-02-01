import numpy as np
import matplotlib.pyplot as plt

def berechne_fehler(A, b, A_tilde, b_tilde):
    x = np.linalg.solve(A, b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)

    cond_A = np.linalg.cond(A, np.inf)
    relative_A_diff = np.linalg.norm(A - A_tilde, np.inf) / np.linalg.norm(A, np.inf)
    relative_b_diff = np.linalg.norm(b - b_tilde, np.inf) / np.linalg.norm(b, np.inf)

    if cond_A * relative_A_diff < 1:
        dx_max = (cond_A / (1 - cond_A * relative_A_diff)) * (relative_A_diff + relative_b_diff)
    else:
        dx_max = np.nan

    dx_obs = np.linalg.norm(x - x_tilde, np.inf) / np.linalg.norm(x, np.inf)

    return x, x_tilde, dx_max, dx_obs

dx_max_vals = []
dx_obs_vals = []
ratios = []

for _ in range(1000):
    A = np.random.rand(100, 100)
    b = np.random.rand(100, 1)
    A_tilde = A + np.random.rand(100, 100) / 1e5
    b_tilde = b + np.random.rand(100, 1) / 1e5

    _, _, dx_max, dx_obs = berechne_fehler(A, b, A_tilde, b_tilde)

    dx_max_vals.append(dx_max)
    dx_obs_vals.append(dx_obs)
    ratios.append(dx_max / dx_obs if dx_obs != 0 else np.nan)

# Grafische Darstellung
plt.semilogy(dx_max_vals, label='dx_max', color='blue')
plt.semilogy(dx_obs_vals, label='dx_obs', color='red')
plt.semilogy(ratios, label='dx_max/dx_obs', color='green')
plt.legend()
plt.xlabel('Iteration')
plt.ylabel('Werte')
plt.title('Vergleich von dx_max und dx_obs')
plt.show()


"""
Die Grafik zeigt, dass dx_max immer eine realistische Obergrenze für dx_obs darstellt, da alle Werte > 1 sind und  
somit als konservative Schätzung für den maximalen relativen Fehler dienen kann. 
Das ist eine positive Bestätigung für die Zuverlässigkeit des Modells oder der Methode, die verwendet wurde, um dx_max  
zu berechnen.
"""



