import numpy as np
import matplotlib.pyplot as plt

start_ki_value = 0.1
days_in_year = 365


def ki(alpha):
    ki_values = [start_ki_value]
    for _ in np.arange(days_in_year):
        current_ki = alpha * ki_values[-1] * (1 - ki_values[-1])
        ki_values.append(current_ki)
    return ki_values


def plot(nums):
    for i in np.arange(nums):
        alpha = i
        list_i = ki(alpha)

        plt.plot(list_i)
        plt.title(f'alpha = {alpha}')
        plt.ylabel('proportion of sick children')
        plt.xlabel('days')
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def check_convergence(ki_values):
    tolerance = 1e-6
    for i in range(1, len(ki_values)):
        differance = abs(ki_values[i] - ki_values[i - 1])

        if (differance < tolerance):
            return True

    return False


def plot_convergence(nums):
    convergence = []
    for i in np.arange(nums):
        alpha = i
        ki_values = ki(alpha)
        if (check_convergence(ki_values)):
            convergence.append(1)
        else:
            convergence.append(0)

    plt.plot(convergence, marker='o')
    plt.title('convergence')
    plt.xlabel('alpha_value')
    plt.ylabel('1 = convergence 0 = divergence')
    plt.grid(True)
    plt.show()


# Erzeugt fünf separate Plots, die die Dynamik der Krankheitsausbreitung für fünf unterschiedliche Alpha-Werte (0 bis 4) darstellen.
# Jeder Plot zeigt, wie sich die Krankheit über die Zeit entwickelt, basierend auf dem jeweiligen Alpha-Wert.
plot(5)

# Führt eine Analyse durch, um zu bestimmen, ob die Sequenz der Krankheitsausbreitung für die verschiedenen Alpha-Werte konvergiert oder divergiert.
# Erzeugt einen Plot, der die Ergebnisse visualisiert: '1' bedeutet, dass die Sequenz für diesen Alpha-Wert konvergiert (stabilisiert),
# während '0' eine Divergenz anzeigt (keine Stabilisierung).
plot_convergence(5)

"""
Basierend auf den Simulationen über 100 Tage (tolerance = 1e-6) 

a) Die Funktion `plot` zeigt, dass bei einigen Werten von α die Anzahl der kranken Kinder stabil bleibt (α = 0 & α = 2 konvergiert)(anziehend), während sie bei anderen stark schwankt (α =  1, α = 3 & α = 4 divergiert)(abstossend). 

b) Ein Fixpunkt ist der Zustand, in dem sich die Anzahl der kranken Kinder stabilisiert und nicht weiter ändert, was auf eine Kontrolle der Krankheitsausbreitung hindeutet.

c) Die Gleichung a = 1 / 1 - k  bestimmt den erforderlichen Wert von α, um eine Konvergenzrate von k zu erreichen. Sie identifiziert einen Fixpunkt, wobei das tatsächliche System, abhängig von α, verschiedene Dynamiken einschliesslich mehrerer Fixpunkte oder Oszillationen aufweisen kann.
"""
