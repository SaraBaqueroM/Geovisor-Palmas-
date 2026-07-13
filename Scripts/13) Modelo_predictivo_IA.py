import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# =====================================================
# RUTAS
# =====================================================

OUTPUT = Path(r"C:\Users\User\Documents\Datos IA al ecosistema\Output_analisis")

palmas = pd.read_csv(
    OUTPUT / "Variables_palmas_por_municipio.csv"
)

ideam = pd.read_csv(
    OUTPUT / "Alertas_IDEAM_por_municipio_2017_2025.csv"
)

# =====================================================
# UNIR
# =====================================================

ideam = ideam.rename(columns={"LEVEL_3":"municipio"})

dataset = palmas.merge(
    ideam,
    on="municipio",
    how="inner"
)

dataset.to_csv(
    OUTPUT/"Dataset_IA_Municipios.csv",
    index=False,
    encoding="utf-8-sig"
)

print(dataset.head())

# =====================================================
# VARIABLES
# =====================================================

X = dataset[[
    "riqueza_palmas",
    "bosque_pct",
    "agro_pct",
    "alertas_2017",
    "alertas_2018",
    "alertas_2019",
    "alertas_2020",
    "alertas_2021",
    "alertas_2022",
    "alertas_2023",
    "alertas_2024"
]]

y = dataset["alertas_2025"]

# =====================================================
# ENTRENAMIENTO
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

modelo = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)

modelo.fit(X_train,y_train)

# =====================================================
# EVALUACIÓN
# =====================================================

pred = modelo.predict(X_test)

print("\n========== MÉTRICAS ==========")

print("MAE :", mean_absolute_error(y_test,pred))

rmse = mean_squared_error(y_test,pred)**0.5
print("RMSE:", rmse)

print("R2  :", r2_score(y_test,pred))

# =====================================================
# IMPORTANCIA
# =====================================================

imp = pd.Series(
    modelo.feature_importances_,
    index=X.columns
).sort_values()

plt.figure(figsize=(8,6))
imp.plot.barh()

plt.tight_layout()

plt.savefig(
    OUTPUT/"Importancia_variables.png",
    dpi=300
)

# =====================================================
# PREDICCIÓN 2026
# =====================================================

X2026 = dataset[[
    "riqueza_palmas",
    "bosque_pct",
    "agro_pct",
    "alertas_2018",
    "alertas_2019",
    "alertas_2020",
    "alertas_2021",
    "alertas_2022",
    "alertas_2023",
    "alertas_2024",
    "alertas_2025"
]].copy()

X2026.columns = X.columns

dataset["pred_alertas_2026"] = modelo.predict(X2026)

dataset = dataset.sort_values(
    "pred_alertas_2026",
    ascending=False
)

dataset.to_csv(
    OUTPUT/"Prediccion_alertas_2026.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nTOP 20 MUNICIPIOS CON MAYOR RIESGO 2026\n")

print(
    dataset[
        ["municipio","pred_alertas_2026"]
    ].head(20)
)

print("\nProceso finalizado.")