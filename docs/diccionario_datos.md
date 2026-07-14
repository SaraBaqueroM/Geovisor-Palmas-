\# Diccionario de datos



\## Descripción general



Este documento describe las variables utilizadas en el conjunto de datos consolidado y en la capa geográfica generada por el proyecto.



Las variables integran información de biodiversidad, monitoreo de deforestación e inteligencia artificial para caracterizar el riesgo de generación de alertas de deforestación a nivel municipal en Colombia.



\---



\# Variables geográficas



| Variable | Tipo | Descripción |

|----------|------|-------------|

| LEVEL\_2 | Texto | Departamento o unidad administrativa de segundo nivel. |

| LEVEL\_3 | Texto | Municipio o unidad administrativa de tercer nivel utilizada como unidad de análisis. |

| geometry | Geometría | Polígono correspondiente al límite municipal. |



\---



\# Variables de biodiversidad



| Variable | Tipo | Descripción |

|----------|------|-------------|

| riqueza\_palmas | Entero | Número de especies de palmas amenazadas registradas en el municipio según datos de GBIF. |

| bosque\_pct | Decimal (%) | Porcentaje de registros de ocurrencia localizados sobre coberturas clasificadas como Bosque natural. |

| agro\_pct | Decimal (%) | Porcentaje de registros de ocurrencia localizados sobre coberturas clasificadas como Uso productivo. |



\---



\# Variables históricas de deforestación



Las siguientes variables corresponden al número de alertas tempranas de deforestación registradas por el IDEAM para cada municipio.



| Variable | Tipo | Descripción |

|----------|------|-------------|

| alertas\_2020 | Entero | Número de alertas registradas durante 2020. |

| alertas\_2021 | Entero | Número de alertas registradas durante 2021. |

| alertas\_2022 | Entero | Número de alertas registradas durante 2022. |

| alertas\_2023 | Entero | Número de alertas registradas durante 2023. |

| alertas\_2024 | Entero | Número de alertas registradas durante 2024. |

| alertas\_2025 | Entero | Número de alertas registradas durante 2025. |



\---



\# Variables generadas por el modelo



| Variable | Tipo | Descripción |

|----------|------|-------------|

| pred\_alertas\_2026 | Decimal | Número estimado de alertas de deforestación que podrían generarse durante 2026 según el modelo Random Forest. |

| riesgo | Categórica | Clasificación cualitativa del riesgo de generación de alertas a partir de la predicción del modelo. |



Las categorías utilizadas son:



| Categoría | Rango de alertas predichas |

|-----------|---------------------------:|

| Muy bajo | ≤ 50 |

| Bajo | 51 – 200 |

| Medio | 201 – 500 |

| Alto | 501 – 1000 |

| Muy alto | > 1000 |



\---



\# Valores nulos



Algunos municipios pueden presentar valores nulos en las variables relacionadas con biodiversidad o predicción.



Esto ocurre principalmente en:



\- Áreas en litigio u otras unidades administrativas especiales.

\- Municipios sin registros de ocurrencia de palmas amenazadas.

\- Municipios excluidos del proceso de modelado por ausencia de información suficiente.



\---



\# Fuente de las variables



| Grupo de variables | Fuente |

|--------------------|--------|

| Límites municipales | Nivel político administrativo de Colombia |

| Registros de palmas | GBIF |

| Fotografías de especies | iNaturalist |

| Especies amenazadas | Resolución 0126 de 2024 (MinAmbiente) |

| Alertas históricas | IDEAM - Monitoreo de Bosques |

| Variables derivadas | Procesamiento propio mediante Python |

| Predicción 2026 | Modelo Random Forest desarrollado en Scikit-learn |



\---



\# Observaciones



Todas las variables fueron generadas mediante un flujo de trabajo reproducible implementado en Python. Los productos finales corresponden a la versión utilizada para el desarrollo del geovisor y del modelo de inteligencia artificial presentado en este proyecto.

