import numpy as np
import matplotlib.pyplot as plt

# a)

def h(x):
    inside_value = 100 * x ** 2 - 200 * x + 99
    if inside_value < 0:
        return np.nan
    return np.sqrt(inside_value)

x_values = [i for i in np.arange(1.09, 1.12, 0.001)]

y_values = [h(x) for x in x_values]

plt.plot(x_values,y_values, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("h(x)")
plt.grid(True)
plt.xlim(1.09, 1.15)
plt.show()
print(y_values)

"""
Der Ausdruck unter der Wurzel nähert sich einem Wert von Null, wenn x sich dem Wert 1.10 annähert.
Wenn der Wert unter der Wurzel sehr nahe an 0 liegt, kann in einer Coputerarithmetik aufgrund von Rundungsfehlern als 0 betrachtet werden.
Die Fliesskomma-Arithmetik von der Maschine kann dazu führen, dass der Ausdruck unter der Wuzel leicht negative wird, selbst wenn der Wert leicht positive sein sollte.
"""

# b)

def h_der(x) :
 return (200 * x - 200) / (2 * h(x))


def con(x) :
    return np.abs(x) * (h_der(x) / h(x))

x_con_values = [i for i in np.arange(1.11, 1.13, 1e-7)]

y_con_values = [con(x) for x in x_con_values]

plt.semilogy(x_con_values, y_con_values, label='Kondition von h(x) 1.11 - 1.13')

plt.title("Halblogarithmischer Plot der Kondition von h(x)")

plt.xlabel("X-Values")

plt.ylabel("Y-Values")

plt.grid(True)

plt.show()

print(y_con_values)


# c)
"""
Die Konditionzahlen liegen zwischen 6 * 10^1 und 3 * 10 ^ 1 die zahlen sind weder sehr gross noch sehr klein.
Das deutet darauf hin, dass die Funktion h(x) eine mittlere Empfindlichkeit gegenüber Eingabeänderung aufweist.
Deshalb könnte man möglicherweise die Auslösung durch einen algorithmus verhindern.
"""