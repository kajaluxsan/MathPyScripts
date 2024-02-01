# 3) b)

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 5 / (2 * x ** 2) ** (1 / 3)

def g(x):
    return (10 ** 5) * 2 * np.e ** (-x/100)

def h(x):
    return (10 ** (2 * x) / 2 ** (5 * x)) ** 2

def plot(function, hasLogX):
    plt.plot(x, function)
    if (hasLogX):
        plt.semilogx()
    plt.semilogy()
    plt.grid(True)
    plt.show()


x = np.arange(0.1, 100 + 1, 0.1)

plot(f(x), True)
plot(g(x), False)
plot(h(x), False)



