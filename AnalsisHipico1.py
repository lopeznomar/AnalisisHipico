import pandas as pd

# Cargar los datos de los CSV generados
jockeys_df = pd.read_csv("C:\Python Varios\AnalisisHipico\estadisticas_jockeys_2024.csv")
trainers_df = pd.read_csv("C:\Python Varios\AnalisisHipico\estadisticas_entrenadores_2024.csv")

# Imprimir los nombres de las columnas y las primeras filas para ambos DataFrames
print("Columnas del DataFrame de Jockeys:")
print(jockeys_df.columns)
print(jockeys_df.head())

print("\nColumnas del DataFrame de Entrenadores:")
print(trainers_df.columns)
print(trainers_df.head())

