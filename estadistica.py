import numpy as np

# Cargar los datos
datos = np.loadtxt("datos.csv", delimiter=",", skiprows=1)

edad = datos[:, 0]
ingreso = datos[:, 1]

# Calcular media
media_edad = np.mean(edad)
media_ingreso = np.mean(ingreso)

# Calcular mediana
mediana_edad = np.median(edad)
mediana_ingreso = np.median(ingreso)

# Calcular desviación estándar
desviacion_edad = np.std(edad)
desviacion_ingreso = np.std(ingreso)

print("Media de edad:", media_edad)
print("Media de ingreso:", media_ingreso)
print("Mediana de edad:", mediana_edad)
print("Mediana de ingreso:", mediana_ingreso)
print("Desviación estándar de edad:", desviacion_edad)
print("Desviación estándar de ingreso:", desviacion_ingreso)
