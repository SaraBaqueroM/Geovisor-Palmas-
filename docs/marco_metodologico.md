\# Marco metodológico



\## Introducción



El desarrollo del proyecto se basó en la integración de datos abiertos de biodiversidad y monitoreo ambiental mediante herramientas de análisis espacial y aprendizaje automático. La metodología adoptada toma como referencia el ciclo CRISP-ML (Cross Industry Standard Process for Machine Learning), adaptándolo a las necesidades específicas del proyecto y a las características de las fuentes de información utilizadas.



Todo el procesamiento, integración de datos, generación de variables, entrenamiento del modelo y producción de resultados fue desarrollado mediante scripts reproducibles en Python.



\---



\# Enfoque metodológico



El proyecto siguió un flujo iterativo compuesto por seis etapas principales:



1\. Comprensión del problema.

2\. Comprensión de los datos.

3\. Preparación de los datos.

4\. Ingeniería de variables.

5\. Modelado mediante aprendizaje automático.

6\. Generación y comunicación de resultados.



Aunque el proceso se presenta de forma secuencial, durante el desarrollo fue necesario realizar múltiples iteraciones entre las diferentes etapas para mejorar la calidad de los datos y optimizar el desempeño del modelo.



\---



\# 1. Comprensión del problema



El objetivo del proyecto fue identificar municipios colombianos donde convergen dos condiciones de interés para la conservación:



\- presencia registrada de especies de palmas amenazadas;

\- alta probabilidad de generación de nuevas alertas de deforestación.



En lugar de modelar directamente la distribución potencial de las especies, el enfoque consistió en utilizar la dinámica histórica de las alertas tempranas de deforestación como variable objetivo y emplear la información sobre biodiversidad como un criterio adicional para priorizar territorios.



\---



\# 2. Comprensión de los datos



Para el desarrollo del modelo se integraron diferentes fuentes de información.



\## 2.1 Listado oficial de especies amenazadas



Se utilizó el listado oficial de especies silvestres amenazadas de Colombia (Resolución 0126 de 2024) para identificar las especies de palmas incluidas en el análisis.



Este listado permitió seleccionar exclusivamente las especies pertenecientes a la familia Arecaceae clasificadas bajo alguna categoría oficial de amenaza.



\---



\## 2.2 Registros de biodiversidad



Los registros de ocurrencia fueron descargados desde GBIF con Python para cada una de las especies seleccionadas.



Posteriormente se realizó un proceso de control de calidad que incluyó:



\- eliminación de registros duplicados;

\- revisión de coordenadas;

\- estandarización de nombres;

\- integración de información taxonómica.



\---



\## 2.3 Alertas tempranas de deforestación



Se recopilaron las Alertas Tempranas de Deforestación del IDEAM correspondientes al período 2017–2025.



Los archivos fueron organizados por año y trimestre para facilitar su procesamiento automático mediante Python.



Posteriormente se realizó un conteo municipal de alertas utilizando análisis espacial.



\---



\## 2.4 Cobertura del suelo



Cada registro biológico fue enriquecido espacialmente con información sobre cobertura del suelo.



A partir de esta información se calcularon indicadores relacionados con la proporción de registros ubicados sobre:



\- Bosque natural.

\- Uso productivo.



\---



\## 2.5 División político-administrativa



Toda la información fue agregada utilizando la división municipal de Colombia como unidad espacial de análisis.



Cada registro biológico y cada alerta de deforestación fueron asignados al municipio correspondiente mediante operaciones de unión espacial (Spatial Join).



\---



\# 3. Preparación de los datos



La preparación de los datos constituyó una de las etapas más importantes del proyecto.



Los principales procesos desarrollados fueron:



\## Descarga automática



Se implementaron scripts en Python para automatizar la descarga y organización de los diferentes conjuntos de datos.



\---



\## Limpieza de registros



Los registros de ocurrencia fueron sometidos a procesos de depuración para eliminar inconsistencias y mejorar la calidad de la información.



Entre ellos:



\- eliminación de duplicados;

\- normalización de nombres de municipios;

\- verificación de geometrías;

\- manejo de valores faltantes.



\---



\## Integración espacial



Mediante GeoPandas se realizaron diferentes operaciones espaciales para:



\- asignar municipios;

\- incorporar coberturas del suelo;

\- calcular distancias a alertas;

\- enriquecer cada registro biológico.



\---



\## Obtención de imágenes



Como parte del desarrollo del geovisor se implementó un proceso automático para consultar la API pública de iNaturalist.



Mediante Python se descargaron imágenes representativas de las especies de palmas amenazadas, las cuales fueron incorporadas posteriormente al geovisor para complementar la información biológica presentada.



\---



\## Construcción del dataset municipal



Finalmente se consolidó un conjunto de datos a escala municipal que integró variables provenientes de todas las fuentes de información.



\---



\# 4. Ingeniería de variables



A partir de los datos originales se generaron variables derivadas utilizadas como entrada del modelo.



Entre ellas:



\## Variables biológicas



\- riqueza de especies de palmas amenazadas por municipio;

\- porcentaje de registros sobre bosque natural;

\- porcentaje de registros sobre uso productivo.



\---



\## Variables históricas



Número de alertas tempranas de deforestación por municipio para cada uno de los años:



\- 2017

\- 2018

\- 2019

\- 2020

\- 2021

\- 2022

\- 2023

\- 2024

\- 2025



Además se calculó:



\- total histórico de alertas por municipio.



\---



\# 5. Modelado



Se utilizó un algoritmo Random Forest Regressor implementado mediante la biblioteca Scikit-learn.



Este algoritmo fue seleccionado debido a:



\- su capacidad para modelar relaciones no lineales;

\- su buen desempeño con variables heterogéneas;

\- su robustez frente a valores atípicos;

\- la posibilidad de interpretar la importancia relativa de las variables.



\---



\## Variables predictoras



El modelo utilizó como variables independientes:



\- riqueza de palmas;

\- porcentaje de bosque natural;

\- porcentaje de uso productivo;

\- historial anual de alertas entre 2017 y 2024.



\---



\## Variable objetivo



La variable objetivo utilizada durante el entrenamiento fue el número de alertas tempranas registradas durante 2025.



Posteriormente el modelo fue utilizado para estimar el riesgo de generación de alertas durante 2026 utilizando como entrada la información histórica disponible hasta 2025.



\---



\## Entrenamiento



El conjunto de datos fue dividido en subconjuntos de entrenamiento y validación mediante una partición aleatoria.



Posteriormente se entrenó un modelo Random Forest con múltiples árboles de decisión para minimizar el error de predicción.



\---



\# 6. Evaluación del modelo



El desempeño del modelo fue evaluado utilizando tres métricas ampliamente utilizadas en problemas de regresión:



\- Error Absoluto Medio (MAE).

\- Raíz del Error Cuadrático Medio (RMSE).

\- Coeficiente de Determinación (R²).



Adicionalmente se calculó la importancia relativa de cada variable predictora para facilitar la interpretación del modelo.



\---



\# 7. Productos generados



Como resultado del flujo metodológico se generaron los siguientes productos:



\- Base de datos consolidada de registros de ocurrencia de palmas amenazadas.

\- Base de datos histórica de alertas tempranas de deforestación del IDEAM (2017–2025) agregadas a nivel municipal.

\- Variables derivadas para el modelado, incluyendo riqueza de especies de palmas y proporción de registros asociados a coberturas de bosque natural y uso productivo.

\- Modelo de aprendizaje automático basado en Random Forest para estimar el riesgo de generación de alertas de deforestación a nivel municipal.

\- Cartografía temática en formato GeoPackage con la predicción de alertas para el año 2026 y la clasificación de niveles de riesgo.

\- Geovisor web interactivo para la exploración espacial de los resultados, desplegado mediante \*\*GitHub Pages\*\*, permitiendo el acceso público a las capas geográficas y la visualización de los municipios priorizados.

\- Repositorio público en GitHub que documenta el código fuente, los scripts de procesamiento, la metodología implementada y los productos derivados del proyecto, favoreciendo la transparencia, la reproducibilidad y la reutilización del trabajo desarrollado.

\---



\# 8. Reproducibilidad



Todo el flujo de trabajo fue desarrollado mediante scripts independientes escritos en Python.



El repositorio organiza de forma estructurada:



\- datos de entrada;

\- scripts de procesamiento;

\- documentación metodológica;

\- productos derivados.



Esta organización permite reproducir completamente el procesamiento realizado, desde la preparación de los datos hasta la generación de los productos cartográficos y el entrenamiento del modelo de inteligencia artificial.



La documentación incluida en el repositorio facilita además la reutilización de la metodología en otros grupos taxonómicos o regiones de estudio, promoviendo el uso de datos abiertos y herramientas de código abierto para el análisis espacial y la conservación de la biodiversidad.

