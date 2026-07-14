\# Resultados



\## Introducción



Como resultado del proceso de integración de datos abiertos, análisis espacial y modelado mediante aprendizaje automático, se generó un conjunto de productos orientados a identificar municipios con mayor riesgo de generación de alertas de deforestación y analizar su relación con la presencia de especies de palmas amenazadas en Colombia.



Los resultados obtenidos incluyen bases de datos integradas, variables derivadas, modelos predictivos, productos cartográficos y un geovisor web para la consulta interactiva de la información.



\---



\# 1. Integración de datos



Se consolidó una base de datos municipal integrando información proveniente de diferentes fuentes:



\- listado oficial de especies amenazadas de Colombia;

\- registros de ocurrencia descargados desde GBIF;

\- alertas tempranas de deforestación del IDEAM para el período 2017–2025;

\- variables derivadas de cobertura del suelo;

\- división político-administrativa municipal.



La integración permitió construir un conjunto de datos único para el entrenamiento del modelo de inteligencia artificial.



\---



\# 2. Variables generadas



Como parte del procesamiento se generaron diferentes variables municipales, entre ellas:



\## Variables biológicas



\- riqueza de especies de palmas amenazadas;

\- porcentaje de registros localizados sobre bosque natural;

\- porcentaje de registros localizados sobre uso productivo.



\## Variables históricas



Para cada municipio se calculó el número de alertas tempranas de deforestación registradas durante los años:



\- 2017

\- 2018

\- 2019

\- 2020

\- 2021

\- 2022

\- 2023

\- 2024

\- 2025



Adicionalmente se calculó el total histórico de alertas por municipio.



\---



\# 3. Modelo de aprendizaje automático



Se entrenó un modelo Random Forest Regressor utilizando las variables espaciales e históricas generadas durante el procesamiento.



El objetivo del modelo fue estimar el número esperado de alertas tempranas de deforestación para el año 2026 a nivel municipal.



La evaluación del modelo mostró un desempeño satisfactorio, evidenciando una alta capacidad para reproducir los patrones históricos observados.



Las métricas obtenidas fueron:



\- Error Absoluto Medio (MAE).

\- Raíz del Error Cuadrático Medio (RMSE).

\- Coeficiente de determinación (R²).



Asimismo, se obtuvo la importancia relativa de las variables predictoras, permitiendo identificar cuáles contribuyen en mayor medida a las predicciones realizadas por el modelo.



\---



\# 4. Predicción municipal para 2026



El modelo permitió estimar el riesgo relativo de generación de alertas tempranas de deforestación para los municipios colombianos utilizando la información histórica disponible hasta 2025.



Como resultado se obtuvo una predicción continua del número esperado de alertas para cada municipio, la cual posteriormente fue clasificada en categorías cualitativas de riesgo:



\- Muy bajo.

\- Bajo.

\- Medio.

\- Alto.

\- Muy alto.



Estas categorías facilitan la interpretación de los resultados y su representación cartográfica.



\---



\# 5. Productos cartográficos



Se generaron productos espaciales en formato GeoPackage que contienen:



\- predicción municipal de alertas para 2026;

\- clasificación del nivel de riesgo;

\- variables asociadas a biodiversidad;

\- información histórica de alertas de deforestación.



Estos productos pueden ser utilizados directamente en sistemas de información geográfica como QGIS.



\---



\# 6. Geovisor interactivo



Como mecanismo de divulgación y consulta pública de los resultados, se desarrolló un geovisor web interactivo.



El geovisor permite explorar espacialmente:



\- municipios con presencia de palmas amenazadas;

\- registros de ocurrencia;

\- fichas técnicas con fotografías de las especies obtenidas desde iNaturalist;

\- niveles históricos de alertas de deforestación;

\- predicción municipal de alertas para 2026.



La aplicación fue publicada mediante \*\*GitHub Pages\*\*, facilitando el acceso libre a los resultados del proyecto desde cualquier navegador web.



\---



\# 7. Repositorio reproducible



Todos los procesos desarrollados durante el proyecto fueron documentados mediante un repositorio público en GitHub.



El repositorio incluye:



\- scripts de procesamiento;

\- documentación metodológica;

\- archivos de configuración del entorno;

\- productos derivados;

\- geovisor web.



Esta organización facilita la reproducción del flujo de trabajo, la reutilización de los scripts y la adaptación de la metodología a otros grupos biológicos o regiones de estudio.



\---



\# Conclusiones de los resultados



La integración de datos abiertos de biodiversidad, monitoreo forestal y análisis espacial permitió construir un modelo capaz de identificar municipios con mayor riesgo de generación de alertas de deforestación.



Además de producir una estimación predictiva para el año 2026, el proyecto generó productos cartográficos y herramientas de visualización que facilitan la identificación de territorios donde convergen procesos históricos de transformación del paisaje y la presencia de especies de palmas amenazadas, aportando información útil para procesos de monitoreo, planificación y conservación de la biodiversidad.

