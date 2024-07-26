import matplotlib.pyplot as plt
import pandas as pd

# Configurar Matplotlib para usar texto en formato SVG
plt.rcParams["svg.fonttype"] = "none"

# Cargar los datos de los archivos CSV
files = [
    "lc1_vel.csv",
    "lc2_vel.csv",
    "lc3_vel.csv",
    "lc4_vel.csv",
    "lc5_vel.csv",
    "lc6_vel.csv",
    "lc7_vel.csv",
    "lc8_vel.csv",
]

# Leer los archivos y almacenar los DataFrames en una lista
dataframes = [pd.read_csv(file) for file in files]

# Convertir tamaño de cm a pulgadas
width_inch = 7.5 / 2.54
height_inch = 6.0 / 2.54

# Crear el gráfico de línea para los datos ordenados
plt.figure(figsize=(width_inch, height_inch))

# Graficar la columna 'p' para cada archivo
for i, df in enumerate(dataframes):
    plt.plot(df["Points:1"], df["U:2"], label=f"v{i+1}")

# Configuraciones del gráfico
plt.xlabel("Distancia y (m)", fontsize=12)
plt.ylabel("Velocidad (m/s)", fontsize=12)
plt.title("Comparación de Velocidad  vs Distancia en y", fontsize=12)

# Añadir una cuadrícula más suave
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Añadir leyenda
plt.legend(loc="best", fontsize=12)

# Ajustar el diseño para evitar recortes
plt.tight_layout()

# Guardar la figura en formato SVG
plt.savefig("figura.svg", format="svg")

# Mostrar el gráfico
plt.show()
