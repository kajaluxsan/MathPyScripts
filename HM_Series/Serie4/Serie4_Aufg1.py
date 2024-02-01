# 1)
import math

import numpy as np
import matplotlib.pyplot as plt

tolerance = 1e-6
number_digits = 6

x1_range = np.arange(-1, 0 + 0.01, 0.01)
x2_range = np.arange(0, 1 + 0.01, 0.01)


def f(x):
    return 230 * x ** 4 + 18 * x ** 3 + 9 * x ** 2 - 221 * x - 9


def f_derivative(x):
    return 920 * x ** 3 + 54 * x ** 2 + 18 * x - 221


def f_fixpoint(x):
    return (230 * x ** 4 + 18 * x ** 3 + 9 * x ** 2 - 9) / 221


def f_derivative_fixpoint(x):
    return (920 * x ** 3 + 54 * x ** 2 + 18 * x) / 221


def calculate_null_point(x, counter=0):
    new_x = f_fixpoint(x)
    print('Iteration #' + str(counter + 1) + ': fix point: ' + str(x) + ' - next fix point: ' + str(new_x))
    if abs(new_x - x) >= tolerance:
        if abs(new_x) < 1:
            calculate_null_point(new_x, counter + 1)
        else:
            print('Wrongly chosen initial x: ' + str(new_x))
    else:
        print('Null point found: ' + str(round(new_x, number_digits)))


def plot(x, function):
    plt.plot(x, function)
    plt.grid(True)
    plt.show()


# a)

# First null point in interval [-1, 0]
# plot(x1, f(x1))
# calculate_null_point(-1)

# Second null point in interval [0, 1]
# plot(x2, f(x2))
# calculate_null_point(0.9)

# The found null point with an initial x between [0, 1] will be the same as the first null point
# Reason: if you enter a positive number between [0, 1], you'll get a negative number which is your new x
# This means you'll be redirected to the same interval as from the first null point


# b)
initial_x = 0.5
alpha = f_derivative_fixpoint(initial_x)
print(round(alpha, number_digits))
""""The value of α is approximately 0.6222. Since 0 ≤ α < 10 ≤ α < 1, this value satisfies the contraction condition 
of Banach's Fixed Point Theorem."""

# c)
x1 = -1
x2 = f_fixpoint(x1)

desired_accuracy = 10 ** -9

num_iterations = math.log(((1-alpha) / abs(x2 - x1)) * desired_accuracy) / math.log(alpha)

print(abs(math.ceil(num_iterations)))