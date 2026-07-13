import pandas as pd

# Leer archivo
df = pd.read_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\especies_amenzadas.csv", sep=",", encoding="utf-8")

# Conteo por reino
reinos = (
    df.groupby("REINO")["NOMBRE CIENTIFICO"]
      .nunique()
      .reset_index(name="NUM_ESPECIES")
      .sort_values("NUM_ESPECIES", ascending=False)
)

print("\n=== ESPECIES POR REINO ===")
print(reinos)

# Conteo por familia
familias = (
    df.groupby("FAMILIA")["NOMBRE CIENTIFICO"]
      .nunique()
      .reset_index(name="NUM_ESPECIES")
      .sort_values("NUM_ESPECIES", ascending=False)
)

print("\n=== TOP 50 FAMILIAS ===")
print(familias.head(50))

# Guardar resultados
reinos.to_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\especies_por_reino.csv", index=False)
familias.to_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\especies_por_familia.csv", index=False)

# Especies por estado de amenaza
amenaza = (
    df.groupby("ESTADO DE AMENAZA")["NOMBRE CIENTIFICO"]
      .nunique()
      .reset_index(name="NUM_ESPECIES")
      .sort_values("NUM_ESPECIES", ascending=False)
)

print(amenaza)

# Cruce reino x amenaza
tabla = pd.crosstab(
    df["REINO"],
    df["ESTADO DE AMENAZA"]
)

print(tabla)

# Guardar resultados
amenaza.to_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\amenaza.csv", index=False)
tabla.to_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\tabla_cruce.csv", index=False)