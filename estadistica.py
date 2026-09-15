import numpy as np

# Actividad 2
datos = [10, 20, 30, 40, 50]

print("Análisis estadístico de datos")
print("Datos:", datos)

# Cálculos de la Actividad 2 - Persona A
suma = sum(datos)
promedio = suma / len(datos)
cantidad = len(datos)

print("\n--- Resultados del análisis ---")
print("Suma:", suma)
print("Promedio:", promedio)
print("Cantidad de datos:", cantidad)

# Cálculos de la Actividad 2 - Persona B
print("Máximo:", max(datos))
print("Mínimo:", min(datos))
print("Rango:", max(datos) - min(datos))

# Análisis que ya existía en GitHub
datos_csv = np.loadtxt("datos.csv", delimiter=",", skiprows=1)

edad = datos_csv[:, 0]
ingreso = datos_csv[:, 1]

media_edad = np.mean(edad)
media_ingreso = np.mean(ingreso)

mediana_edad = np.median(edad)
mediana_ingreso = np.median(ingreso)

desviacion_edad = np.std(edad)
desviacion_ingreso = np.std(ingreso)

print("Media de edad:", media_edad)
print("Media de ingreso:", media_ingreso)
print("Mediana de edad:", mediana_edad)
print("Mediana de ingreso:", mediana_ingreso)
print("Desviación estándar de edad:", desviacion_edad)
print("Desviación estándar de ingreso:", desviacion_ingreso)