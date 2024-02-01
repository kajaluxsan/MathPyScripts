import numpy as np
import matplotlib.pyplot as plt


def compute_a(two_times_n):
    if two_times_n == 6:
        return 1
    n = two_times_n / 2
    return np.sqrt(2 - 2 * np.sqrt(1 - (compute_a(n) ** 2 / 4)))


def u_a(n):
    return n * compute_a(n)


def compute_b(two_times_n):
    if two_times_n == 6:
        return 1
    n = two_times_n / 2
    sn = compute_b(n)
    return np.sqrt(sn ** 2 / (2 * (1 + np.sqrt(1 - (sn ** 2 / 4)))))


def u_b(n):
    return n * compute_b(n)


def x_values(iterations):
    return 2 ** (np.array(range(1, iterations + 1)) - 1) * 6


n_vals = x_values(13)

a_vals = [u_a(n) for n in n_vals]

b_vals = [u_b(n) for n in n_vals]

plt.plot(n_vals, a_vals, label='Method A', marker='o')
plt.plot(n_vals, b_vals, label='Method B', marker='x')
plt.xlabel('n')
plt.ylabel('values')
plt.legend()
plt.grid(True)
plt.show()
