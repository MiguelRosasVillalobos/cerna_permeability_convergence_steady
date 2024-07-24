import matplotlib.pyplot as plt
import pandas as pd

# Cargar los datos de los archivos CSV
files = [
    "lc1.csv",
    "lc2.csv",
    "lc3.csv",
    "lc4.csv",
    "lc5.csv",
    "lc6.csv",
    "lc7.csv",
]

# Leer los archivos y almacenar los DataFrames en una lista
dataframes = [pd.read_csv(file) for file in files]

# Configurar la figura para el gráfico
plt.figure(figsize=(14, 8))

# Graficar la columna 'p' para cada archivo
for i, df in enumerate(dataframes):
    plt.plot(df["Points:2"], df["p"] / 9.81, label=f"lc{i+1}")

# Configuraciones del gráfico
plt.xlabel("Points:2")
plt.ylabel("Velocidad (m/s)")
plt.title("Comparación de Velocidad vs Points:2 en diferentes archivos")
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
