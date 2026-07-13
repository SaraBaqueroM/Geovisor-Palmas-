from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# ============================================================
# Rutas
# ============================================================

INPUT = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\municipios_dataset_modelo.csv"

# ============================================================
# Leer datos
# ============================================================

print("Leyendo dataset...")

df = pd.read_csv(INPUT)

# ============================================================
# Variables del modelo
# ============================================================

variables = [

    "riqueza_especies",

    "indice_amenaza",

    "pct_bosque",

    "pct_palma",

    "pct_agro",

    "glad_presion"

]

# ============================================================
# Escalar
# ============================================================

scaler = StandardScaler()

X = scaler.fit_transform(df[variables])

# ============================================================
# Evaluación
# ============================================================

ks = range(2,11)

inercias = []

silhouettes = []

print()

print("========================================")
print("Evaluación de K")
print("========================================")

for k in ks:

    modelo = KMeans(

        n_clusters=k,

        random_state=42,

        n_init=20

    )

    etiquetas = modelo.fit_predict(X)

    inercias.append(modelo.inertia_)

    sil = silhouette_score(X, etiquetas)

    silhouettes.append(sil)

    print(f"K = {k:2d}   Inercia = {modelo.inertia_:10.2f}   Silhouette = {sil:.4f}")

# ============================================================
# Método del codo
# ============================================================

plt.figure(figsize=(7,5))

plt.plot(

    ks,

    inercias,

    marker="o"

)

plt.xlabel("Número de clusters (K)")

plt.ylabel("Inercia")

plt.title("Método del Codo")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\elbow.png",
    dpi=300
)

# ============================================================
# Silhouette
# ============================================================

plt.figure(figsize=(7,5))

plt.plot(

    ks,

    silhouettes,

    marker="o"

)

plt.xlabel("Número de clusters (K)")

plt.ylabel("Silhouette Score")

plt.title("Silhouette Score")

plt.grid(True)

plt.tight_layout()

plt.savefig(

    r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\silhouette.png",

    dpi=300

)

print()

print("Gráficos guardados en Output_analisis")

print(" - elbow.png")

print(" - silhouette.png")

print()

print(f"Mejor Silhouette: K = {ks[silhouettes.index(max(silhouettes))]}")