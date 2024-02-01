import numpy as np
import time
import matplotlib.pyplot as plt
from Serie6.IT22ta_ZH07_S6_Aufg2 import gauss_procedure
from Serie10.IT22ta_ZH07_S10_Aufg3a import IT22ta_ZH07_S10_Aufg3a

# Daten
dim = 3000
A = np.diag(np.diag(np.ones((dim, dim)) * 4000)) + np.ones((dim, dim))
dum1 = np.arange(1, int(dim / 2 + 1), dtype=np.float64).reshape((int(dim / 2), 1))
dum2 = np.arange(int(dim / 2), 0, -1, dtype=np.float64).reshape((int(dim / 2), 1))
x_exact = np.append(dum1, dum2, axis=0)
b = A @ x_exact
x0 = np.zeros((dim, 1))
tol = 1e-4

# Laufzeitmessung
# Gauss-Seidel
start_time = time.time()
x_gauss_seidel, _, _ = IT22ta_ZH07_S10_Aufg3a(A, b, x0, tol, 'Gauss-Seidel')
gauss_seidel_time = time.time() - start_time
print(f"Gauss-Seidel Laufzeit: {gauss_seidel_time} Sekunden")

# jacobi
start_time = time.time()
x_jacobi, _, _ = IT22ta_ZH07_S10_Aufg3a(A, b, x0, tol, 'Jacobi')
linalg_time = time.time() - start_time
print(f"Jacobi Laufzeit: {linalg_time} Sekunden")

# Gauss-Prozedur
A_copy = A.copy()
b_copy = b.copy()
start_time = time.time()
x_gauss = gauss_procedure(A_copy, b_copy)
gauss_procedure_time = time.time() - start_time
print(f"Gauss-Prozedur Laufzeit: {gauss_procedure_time} Sekunden")

# Fehleranalyse
error_gauss_seidel = np.abs(x_exact - x_gauss_seidel.reshape(x_exact.shape))
error_gauss = np.abs(x_exact - x_gauss.reshape(x_exact.shape))
error_jacobi = np.abs(x_exact - x_jacobi.reshape(x_exact.shape))

# Fehler plotten
plt.figure(figsize=(12, 8))
plt.plot(error_gauss_seidel, label='Gauss-Seidel Fehler', marker='o')
plt.plot(error_gauss, label='Gauss Fehler', marker='x')
plt.plot(error_jacobi, label='Jacobi Fehler', marker='^')
plt.yscale('log')
plt.xlabel('Index des Vektorelements')
plt.ylabel('Absoluter Fehler')
plt.title('Vergleich der Fehler der Lösungsmethoden')
plt.legend()
plt.show()

"""
Das Gauss-Verfahren bietet eine perfekte Lösung mit null absolutem Fehler, ideal für Präzisionsanwendungen, bei denen 
die Laufzeit weniger wichtig ist. Die Gauss-Seidel-Methode ist ein guter Kompromiss zwischen Genauigkeit und Effizienz, 
geeignet für Situationen, in denen eine perfekte Lösung nicht zwingend erforderlich ist. Das Jacobi-Verfahren, obwohl 
weniger effizient als Gauss-Seidel und mit dem höchsten Fehler, besticht durch seine Parallelisierbarkeit, was es für 
bestimmte Anwendungsfälle trotz längerer Laufzeit vorteilhaft macht.
"""
