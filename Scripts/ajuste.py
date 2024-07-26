import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

# Listas de nombres de archivos
archivos_vel_csv = [f"v{i}_vel.csv" for i in range(1, 9)]
archivos_p_csv = [f"v{i}.csv" for i in range(1, 9)]

# Inicializar listas para almacenar las velocidades máximas y los valores máximos de p
velocidades_maximas = []
p_maximos = []

# Leer cada archivo de velocidades y extraer la velocidad máxima de la columna 'U:2'
for archivo in archivos_vel_csv:
    df = pd.read_csv(archivo)
    if "U:2" in df.columns:
        velocidad_maxima = df["U:2"].max()
        velocidades_maximas.append(velocidad_maxima)
    else:
        raise ValueError(f"El archivo {archivo} no contiene una columna llamada 'U:2'.")

# Leer cada archivo de p y extraer el valor máximo de la columna 'p'
for archivo in archivos_p_csv:
    df = pd.read_csv(archivo)
    if "p" in df.columns:
        p_maximo = df["p"].max()
        p_maximos.append(p_maximo)
    else:
        raise ValueError(f"El archivo {archivo} no contiene una columna llamada 'p'.")

# Crear los vectores V e I con los valores máximos obtenidos y agregar el punto (0,0)
V = np.array([0] + velocidades_maximas)
I = np.array([0] + p_maximos) / (9.81 * 0.01)


# Definimos la función parabólica con término lineal y cuadrático
def parabola(x, a, b):
    return a * x + b * x**2


# Ajuste de los datos a la parábola
popt, pcov = curve_fit(parabola, V, I)
a, b = popt

# Coeficiente de correlación de Pearson
r, _ = pearsonr(I, parabola(V, a, b))

# Imprimir los coeficientes de ajuste y el coeficiente de correlación
print(f"Coeficiente a: {a}")
print(f"Coeficiente b: {b}")
print(f"Coeficiente de correlación de Pearson: {r}")

# Discretización fina para la curva ajustada
V_fine = np.linspace(min(V), max(V), 1000)
I_fine = parabola(V_fine, a, b)

# Graficar los datos y el ajuste con estilo mejorado
plt.figure(figsize=(10, 6))
plt.scatter(V, I, label="Datos", color="blue", marker="o")
plt.plot(
    V_fine,
    I_fine,
    label=f"Ajuste: $I = {a:.2f}V + {b:.2f}V^2$",
    color="red",
    linestyle="-",
    linewidth=2,
)
plt.xlabel("V (m/s)", fontsize=14)
plt.ylabel("I (m/m)", fontsize=14)
plt.title("Ajuste Parabólico de Datos", fontsize=16)
plt.legend(fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tick_params(axis="both", which="major", labelsize=12)
plt.text(
    0.1,
    0.9,
    f"$r^2 = {r:.7f}$",
    transform=plt.gca().transAxes,
    fontsize=14,
    verticalalignment="top",
)
plt.tight_layout()

# Guardar el gráfico como un archivo PNG de alta resolución
# plt.savefig("ajuste_parabolico.png", dpi=300)
print(I)
# Mostrar el gráfico
plt.show()
