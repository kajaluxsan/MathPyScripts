# Task 4
# a)
eps = float(1)

while eps + 1 > 1:
    eps /= 2

eps *= 2

print("eps: ", eps)


# 2.22e-16 ist gleich 2^-52, was der Mantissenlänge eines Floats im Dualsystem entspricht.


# b)

q_max = float(1)

while q_max != q_max + 1:
    q_max *= 2

q_max /= 2

print("qmax: ", q_max)
print("eps: ", 1 / q_max)


# Der Kehrwert von q_max ergibt eps.
