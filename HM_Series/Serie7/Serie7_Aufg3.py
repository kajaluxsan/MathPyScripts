import numpy as np
import matplotlib.pyplot as plt
import IT22ta_ZH07_S6_Aufg2 as a2

# Daten vorbereiten
# x-Werte (Jahre): 0, 2, 9, 13
# y-Werte (Anzahl der Tage): 150, 104, 172, 152
x_values = np.array([0, 2, 9, 13])
y_values = np.array([150, 104, 172, 152])

matrix_A = np.vander(x_values, 4)
matrix_b = y_values.reshape(4, 1)
#coefficients = a2.gauss_procedure(matrix_A, matrix_b)
coefficients = np.linalg.solve(matrix_A, matrix_b)
print("coefficients: {}".format(coefficients))

# b)
# schätzung_für_2003
value_2003 = np.polyval(coefficients, 6)
print("value von 2003: {}".format(value_2003))
# schätzung_für_2004
value_2004 = np.polyval(coefficients, 7)
print("value von 2004: {}".format(value_2004))

# c)
koeffizienten = np.polyfit(x_values, y_values, 3)
print("koeffizienten mit polyfit() berechnet: {}".format(koeffizienten))

# schätzung_polyfit_für_2003
wert_2003 = np.polyval(koeffizienten, 6)
print("werte von 2003 mit polyfit() berechnet: {}".format(wert_2003))
# schätzung_polyfit_für_2004
wert_2004 = np.polyval(koeffizienten, 7)
print("werte von 2004 mit polyfit() berechnet: {}".format(wert_2004))

# plot aufgabe a
coefficients = np.array([coefficients]).flatten()
polynomial_function = np.poly1d(coefficients)

# Zeitachse erstellen 1997 - 2010 (13 jahren)
years_since_1997 = np.arange(0, 13, 0.1)

values_since_1997 = polynomial_function(years_since_1997)

plt.plot(years_since_1997 + 1997 , values_since_1997, label='Polynom')

plt.scatter(x_values + 1997, y_values, color='red', label='Original-Datenpunkte')  # Originaldatenpunkte
plt.title('Polynom-Interpolation der Daten')
plt.xlabel('Jahr')
plt.ylabel('Wert')
plt.legend()
plt.grid(True)
plt.show()


#plot aufgabe c
polynomial_funktion = np.poly1d(koeffizienten)

werte_von_1997 = polynomial_funktion(years_since_1997)

plt.plot(years_since_1997 + 1997 , werte_von_1997, label='Polynom')
plt.plot(years_since_1997 + 1997 , values_since_1997, label='Polynom mit gaus')

plt.scatter(x_values + 1997, y_values, color='red', label='Original-Datenpunkte')  # Originaldatenpunkte
plt.title('Polynom-Interpolation der Daten')
plt.xlabel('Jahr')
plt.ylabel('Wert')
plt.legend()
plt.grid(True)
plt.show()

