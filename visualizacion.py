import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos
datos = np.loadtxt("datos.csv", delimiter=",", skiprows=1)

edad = datos[:, 0]
ingreso = datos[:, 1]

# Crear gráfico
plt.scatter(edad, ingreso)

plt.xlabel("Edad")
plt.ylabel("Ingreso")
plt.title("Relación entre edad e ingreso")

plt.show()
