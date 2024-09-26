import matplotlib.pyplot as plt
import pandas as pd

# Configurar Matplotlib para usar texto en formato SVG
plt.rcParams["svg.fonttype"] = "none"

# Cargar los datos de los archivos CSV
files = [
    "p1_lc1.csv",
    "p1_lc2.csv",
    "p1_lc3.csv",
    "p1_lc4.csv",
    "p1_lc5.csv",
    "p1_lc6.csv",
    "p1_lc7.csv",
    "p1_lc8.csv",
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
    plt.plot(df["Points:1"], df["p"] / 9.81, label=f"v{i+1}")

# Configuraciones del gráfico
plt.xlabel("Distancia y (m)", fontsize=12)
plt.ylabel("Perdidad de Carga (m)", fontsize=12)
plt.title("Comparación de Perdida de Carga vs distancia y ", fontsize=12)

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
