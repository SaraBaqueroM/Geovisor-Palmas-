\# Guía de validación del proyecto



\## Objetivo



Esta guía describe los pasos necesarios para reproducir el flujo de trabajo desarrollado en el proyecto, desde la preparación de los datos hasta la generación del geovisor y los productos finales.



\---



\# Requisitos



Antes de ejecutar el proyecto es necesario contar con:



\- Python 3.11 o superior

\- Git

\- QGIS (para visualización de resultados geográficos, opcional)

\- Navegador web actualizado



Las dependencias de Python se encuentran definidas en:



\- `requirements.txt`

\- `environment.yml`



\---



\# Estructura del proyecto



El repositorio contiene los siguientes componentes principales:



```

docs/

Scripts/

Geovisor/

Output\_analisis/

RECURSOS/

```



\---



\# Datos de entrada



El proyecto utiliza información proveniente de las siguientes fuentes abiertas:



\- Listado oficial de especies amenazadas de Colombia (Resolución 0126 de 2024).

\- Registros de ocurrencia descargados desde GBIF.

\- Fotografías obtenidas desde iNaturalist.

\- Alertas Tempranas de Deforestación del IDEAM (2017–2025).

\- Límites municipales de Colombia.



Los archivos deben ubicarse en las rutas indicadas dentro de cada script o ajustarse según la organización local del usuario.



\---



\# Flujo de ejecución



Los scripts fueron diseñados para ejecutarse de forma secuencial.



\## Paso 1



Procesamiento del listado de especies amenazadas.



Salida esperada:



\- Listado de especies objetivo.



\---



\## Paso 2



Descarga y depuración de registros de ocurrencia desde GBIF.



Salida esperada:



\- Base de ocurrencias depurada.



\---



\## Paso 3



Descarga automática de fotografías desde iNaturalist mediante Python.



Salida esperada:



\- Carpeta con imágenes de las especies.



\---



\## Paso 4



Integración de variables espaciales.



Se calculan variables como:



\- municipio;

\- riqueza de especies;

\- porcentaje de registros sobre bosque natural;

\- porcentaje de registros sobre uso productivo.



Salida esperada:



\- Variables municipales.



\---



\## Paso 5



Procesamiento de las Alertas Tempranas de Deforestación del IDEAM.



El script:



\- lee todos los archivos KML;

\- integra los cuatro trimestres de cada año;

\- realiza la unión espacial con los municipios;

\- calcula el número anual de alertas.



Salida esperada:



\- Alertas\_IDEAM\_por\_municipio\_2017\_2025.csv



\---



\## Paso 6



Entrenamiento del modelo Random Forest.



El modelo utiliza:



\- variables de biodiversidad;

\- variables espaciales;

\- serie histórica de alertas.



Salida esperada:



\- Predicción municipal de alertas para 2026.

\- Importancia de variables.

\- Dataset consolidado.



\---



\## Paso 7



Generación de la capa geográfica.



El script integra las predicciones con los límites municipales y genera un GeoPackage utilizado por el geovisor.



Salida esperada:



\- Municipios\_Riesgo\_Alertas\_2026.gpkg



\---



\## Paso 8



Actualización del geovisor.



Los archivos generados son incorporados al geovisor web publicado mediante GitHub Pages.



\---



\# Productos esperados



Al finalizar correctamente la ejecución deberán generarse, entre otros, los siguientes archivos:



\- Dataset\_IA\_Municipios.csv

\- Variables\_palmas\_por\_municipio.csv

\- Alertas\_IDEAM\_por\_municipio\_2017\_2025.csv

\- Prediccion\_alertas\_2026.csv

\- Municipios\_Riesgo\_Alertas\_2026.gpkg

\- Importancia\_variables.png



\---



\# Verificación de resultados



La ejecución puede considerarse correcta si:



\- El modelo genera métricas de evaluación (MAE, RMSE y R²).

\- Se crea el archivo `Prediccion\_alertas\_2026.csv`.

\- Se genera correctamente el archivo `Municipios\_Riesgo\_Alertas\_2026.gpkg`.

\- El geovisor carga correctamente la nueva capa geográfica.

\- Las predicciones son consistentes con el comportamiento histórico de las alertas observadas.



\---



\# Consideraciones



Los resultados pueden presentar pequeñas variaciones si se modifican los datos de entrada, los parámetros del modelo o la versión de las bibliotecas utilizadas.



El flujo fue diseñado para ser completamente reproducible utilizando datos abiertos y herramientas de código abierto.

