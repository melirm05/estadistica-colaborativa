import numpy as np

# Cargar los datos
datos = np.loadtxt("datos.csv", delimiter=",", skiprows=1)

edad = datos[:, 0]
ingreso = datos[:, 1]

# Calcular media
media_edad = np.mean(edad)
media_ingreso = np.mean(ingreso)

print("Media de edad:", media_edad)
print("Media de ingreso:", media_ingreso)