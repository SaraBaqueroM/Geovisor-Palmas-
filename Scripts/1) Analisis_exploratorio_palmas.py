import pandas as pd

# Leer archivo
df = pd.read_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\Palmas\palmas.csv", sep=",", encoding="utf-8")

# Conteo por genero
generos = (
    df.groupby("GENERO")["NOMBRE CIENTIFICO"]
      .nunique()
      .reset_index(name="NUM_ESPECIES")
      .sort_values("NUM_ESPECIES", ascending=False)
)

print("\n=== ESPECIES POR Genero ===")
print(generos)

# Conteo por vulnerabilidad
vulnerabilidad = (
    df.groupby("ESTADO DE AMENAZA")["NOMBRE CIENTIFICO"]
      .nunique()
      .reset_index(name="NUM_ESPECIES")
      .sort_values("NUM_ESPECIES", ascending=False)
)

print("\n=== Estados de amenaza ===")
print(vulnerabilidad)

# Guardar resultados
vulnerabilidad.to_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\Palmas\vulnerabilidad_palmas.csv", index=False)
generos.to_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\Palmas\especies_por_genero.csv", index=False)

# # Especies por estado de amenaza
# amenaza = (
#     df.groupby("ESTADO DE AMENAZA")["NOMBRE CIENTIFICO"]
#       .nunique()
#       .reset_index(name="NUM_ESPECIES")
#       .sort_values("NUM_ESPECIES", ascending=False)
# )

# print(amenaza)

# # Cruce reino x amenaza
# tabla = pd.crosstab(
#     df["REINO"],
#     df["ESTADO DE AMENAZA"]
# )

# print(tabla)

# # Guardar resultados
# amenaza.to_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\amenaza.csv", index=False)
# tabla.to_csv(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis\tabla_cruce.csv", index=False)