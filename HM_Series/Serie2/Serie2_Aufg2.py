import numpy as np
import matplotlib.pyplot as plt

# a)
def f1(x):
    return x ** 7 - 14 * x ** 6 + 84 * x ** 5 - 280 * x ** 4 + 560 * x ** 3 - 672 * x ** 2 + 448 * x - 128

def f2(x):
    return (x - 2) ** 7

x_values_a = np.linspace(1.99, 2.01, 501)
plt.figure(figsize=(10, 5))
plt.plot(x_values_a, f1(x_values_a), label="f1(x)")
plt.plot(x_values_a, f2(x_values_a), label="f2(x)", linestyle="--")
plt.legend()
plt.title("Vergleich von f1(x) und f2(x)")
plt.grid(True)
plt.show()

# Es ist bekannt, dass diese beiden Funktionen analytisch identisch sind,
# aber aufgrund von numerischen Ungenauigkeiten bei der Berechnung
# können Unterschiede bei der Darstellung auftreten.

# b)
def g(x):
    return x / (np.sin(1 + x) - np.sin(1))

x_values_b = np.arange(-10 ** -14, 10 ** -14, 10 ** -17)
plt.figure(figsize=(10, 5))
plt.plot(x_values_b, g(x_values_b), label="g(x)")
plt.title("Darstellung von g(x)")
plt.grid(True)
plt.legend()
plt.show()

# Das Plotten der Funktion g(x) in der Nähe von x = 0 könnte zu Instabilitäten führen,
# da der Nenner nahe 0 ist und numerische Ungenauigkeiten verstärkt werden könnten.

# c)

def g_new(x):
    return x / (2 * np.cos(1 + x / 2) * np.sin(x / 2))

x_values = np.arange(-10 ** -14, 10 ** -14, 10 ** -17)

plt.figure(figsize=(10, 5))

plt.plot(x_values, g_new(x_values), label="g_new(x)", linestyle="-")

plt.legend()
plt.title("g_new(x)")
plt.grid(True)
plt.ylim([-1e11, 1e11])  # Sie können den y-Bereich ändern, um die Graphen besser zu sehen
plt.show()

# Durch die Umformung des Nenners mithilfe des Additionstheorems wird
# die Funktion g(x) in der Nähe von x = 0 stabiler und weniger anfällig
# für numerische Ungenauigkeiten. Der Grenzwert von g(x) für x -> 0 ist 0,
# da sowohl Zähler als auch Nenner gegen 0 streben.

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