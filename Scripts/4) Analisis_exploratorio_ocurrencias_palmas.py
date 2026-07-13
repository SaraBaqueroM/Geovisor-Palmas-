"""
03_eda_ocurrencias.py

Análisis Exploratorio de Datos (EDA) para las ocurrencias
de palmas amenazadas en Colombia obtenidas desde GBIF.

Autor: Equipo Datos al Ecosistema 2026
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# CONFIGURACIÓN
# =====================================================

INPUT_CSV = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\ocurrencias_palmas.csv"
OUTPUT_FOLDER = r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\Analisis exploratorio ocurrencias palmas"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

plt.style.use("ggplot")

# =====================================================
# CARGAR DATOS
# =====================================================

df = pd.read_csv(INPUT_CSV)

print("\n====================================")
print("ANÁLISIS EXPLORATORIO DE DATOS")
print("====================================\n")

# =====================================================
# RESUMEN GENERAL
# =====================================================

resumen = []

resumen.append(f"Registros: {len(df):,}")
resumen.append(f"Especies: {df['species'].nunique()}")
resumen.append(f"Géneros: {df['GENERO'].nunique()}")
resumen.append(f"Familias: {df['FAMILIA'].nunique()}")
resumen.append(f"Instituciones: {df['institutionCode'].nunique()}")
resumen.append(f"Datasets: {df['datasetName'].nunique()}")
resumen.append(f"Año mínimo: {int(df['year'].min())}")
resumen.append(f"Año máximo: {int(df['year'].max())}")

for linea in resumen:
    print(linea)

with open(f"{OUTPUT_FOLDER}/resumen_general.txt", "w", encoding="utf8") as f:
    f.write("\n".join(resumen))

# =====================================================
# CALIDAD DEL DATASET
# =====================================================

faltantes = pd.DataFrame({
    "Valores faltantes": df.isnull().sum(),
    "Porcentaje": round(df.isnull().sum()/len(df)*100,2)
})

faltantes.to_csv(
    f"{OUTPUT_FOLDER}/valores_faltantes.csv",
    encoding="utf-8-sig"
)

# =====================================================
# DUPLICADOS
# =====================================================

duplicados_exactos = df.duplicated().sum()

duplicados_gbif = df["gbifID"].duplicated().sum()

duplicados_coord = df.duplicated(
    subset=[
        "species",
        "decimalLatitude",
        "decimalLongitude"
    ]
).sum()

print("\nDuplicados exactos:", duplicados_exactos)
print("Duplicados gbifID:", duplicados_gbif)
print("Duplicados especie+coordenadas:", duplicados_coord)

# =====================================================
# ESTADOS DE AMENAZA
# =====================================================

amenaza = (
    df["ESTADO DE AMENAZA"]
    .value_counts()
    .sort_index()
)

amenaza.to_csv(
    f"{OUTPUT_FOLDER}/estado_amenaza.csv",
    encoding="utf-8-sig"
)

plt.figure(figsize=(7,5))

amenaza.plot(kind="bar")

plt.title("Registros por categoría de amenaza")
plt.xlabel("")
plt.ylabel("Número de registros")

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/estado_amenaza.png",
    dpi=300
)

plt.close()

# =====================================================
# TOP ESPECIES
# =====================================================

top_especies = (
    df["species"]
    .value_counts()
    .head(10)
)

top_especies.to_csv(
    f"{OUTPUT_FOLDER}/top10_especies.csv",
    encoding="utf-8-sig"
)

plt.figure(figsize=(10,6))

top_especies.sort_values().plot(kind="barh")

plt.title("Top 10 especies con más ocurrencias")
plt.xlabel("Número de registros")

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/top10_especies.png",
    dpi=300
)

plt.close()

# =====================================================
# DISTRIBUCIÓN TEMPORAL
# =====================================================

anios = (
    df["year"]
    .value_counts()
    .sort_index()
)

anios.to_csv(
    f"{OUTPUT_FOLDER}/registros_por_anio.csv",
    encoding="utf-8-sig"
)

plt.figure(figsize=(10,5))

anios.plot()

plt.title("Ocurrencias por año")

plt.xlabel("Año")

plt.ylabel("Número de registros")

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/registros_por_anio.png",
    dpi=300
)

plt.close()

# =====================================================
# DEPARTAMENTOS
# =====================================================

departamentos = (
    df["stateProvince"]
    .fillna("Sin dato")
    .value_counts()
)

departamentos.to_csv(
    f"{OUTPUT_FOLDER}/departamentos.csv",
    encoding="utf-8-sig"
)

plt.figure(figsize=(8,8))

departamentos.head(15).sort_values().plot(kind="barh")

plt.title("Departamentos con mayor número de registros")

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/departamentos.png",
    dpi=300
)

plt.close()

# =====================================================
# INSTITUCIONES
# =====================================================

instituciones = (
    df["institutionCode"]
    .fillna("Sin dato")
    .value_counts()
)

instituciones.to_csv(
    f"{OUTPUT_FOLDER}/instituciones.csv",
    encoding="utf-8-sig"
)

plt.figure(figsize=(9,7))

instituciones.head(15).sort_values().plot(kind="barh")

plt.title("Instituciones con mayor aporte de registros")

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/instituciones.png",
    dpi=300
)

plt.close()

# =====================================================
# TIPO DE REGISTRO
# =====================================================

tipo = (
    df["basisOfRecord"]
    .value_counts()
)

tipo.to_csv(
    f"{OUTPUT_FOLDER}/tipo_registro.csv",
    encoding="utf-8-sig"
)

plt.figure(figsize=(7,5))

tipo.plot(kind="bar")

plt.title("Tipo de registro")

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/tipo_registro.png",
    dpi=300
)

plt.close()

# =====================================================
# MUNICIPIOS VACÍOS
# =====================================================

municipios_vacios = df["municipality"].isna().sum()

print(f"\nMunicipios vacíos: {municipios_vacios:,}")

# =====================================================
# ESPECIES POR CATEGORÍA DE AMENAZA
# =====================================================

tabla = pd.crosstab(
    df["species"],
    df["ESTADO DE AMENAZA"]
)

tabla.to_csv(
    f"{OUTPUT_FOLDER}/especies_vs_amenaza.csv",
    encoding="utf-8-sig"
)

print("\nEDA finalizado correctamente.")
print(f"Resultados guardados en: {OUTPUT_FOLDER}")