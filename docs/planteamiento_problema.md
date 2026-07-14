\# Planteamiento del problema



\## Contexto



Colombia es reconocido como uno de los países con mayor diversidad biológica del planeta, albergando una gran variedad de ecosistemas y especies vegetales. Dentro de esta diversidad, las palmas representan un grupo de gran importancia ecológica, cultural y económica, debido a su papel en la estructura de los ecosistemas, sus interacciones con la fauna y sus múltiples usos por comunidades humanas.



A pesar de esta riqueza biológica, diferentes especies de palmas enfrentan amenazas asociadas principalmente a la transformación del hábitat, expansión de actividades productivas, fragmentación de ecosistemas y pérdida de cobertura vegetal. La identificación de áreas donde coinciden especies vulnerables con zonas sometidas a presiones de transformación es fundamental para orientar acciones de conservación.



Paralelamente, Colombia cuenta con sistemas de monitoreo de pérdida de cobertura vegetal que generan información espacial sobre procesos de deforestación y degradación de ecosistemas. Estas fuentes permiten analizar patrones históricos de cambio y explorar escenarios de riesgo futuro.



La disponibilidad simultánea de datos abiertos sobre biodiversidad y monitoreo ambiental representa una oportunidad para desarrollar herramientas de inteligencia artificial capaces de integrar ambas fuentes y generar insumos para apoyar la toma de decisiones en conservación.



\## Problema identificado



Aunque existen múltiples fuentes de datos abiertos sobre biodiversidad y monitoreo ambiental, estas fuentes generalmente se encuentran separadas y requieren procesos de integración para generar análisis más completos.



Por un lado, los registros de ocurrencia de especies disponibles en plataformas como GBIF permiten conocer localidades donde han sido observadas especies de interés, pero presentan limitaciones relacionadas con sesgos de muestreo, distribución desigual de observaciones y diferencias en la calidad espacial de los registros.



Por otro lado, los sistemas de alertas tempranas de deforestación, como los generados por el IDEAM entre 2017 y 2025, permiten identificar patrones temporales y espaciales de pérdida de cobertura vegetal, pero estos datos normalmente son utilizados para seguimiento de cambios y no necesariamente integrados con información de biodiversidad para evaluar posibles impactos sobre especies amenazadas.



Esta separación limita la capacidad de identificar territorios donde coinciden:

\- presencia registrada de especies de palmas amenazadas,

\- antecedentes de pérdida de cobertura vegetal,

\- y condiciones asociadas a un mayor riesgo futuro de transformación.



\## Pregunta de investigación



¿Cómo pueden integrarse registros abiertos de biodiversidad, alertas históricas de deforestación del IDEAM y técnicas de aprendizaje automático para identificar municipios con mayor riesgo de generación de alertas de deforestación y priorizar territorios donde existen registros de palmas amenazadas en Colombia?



\## Objetivo general



Desarrollar un modelo basado en inteligencia artificial que integre registros de ocurrencia de palmas amenazadas y la serie histórica de alertas tempranas de deforestación del IDEAM (2017–2025) para predecir el riesgo municipal de generación de nuevas alertas de deforestación y apoyar la priorización de territorios para la conservación.



\## Objetivos específicos



* Consolidar y depurar registros de ocurrencia de especies de palmas amenazadas provenientes de fuentes abiertas de biodiversidad.
* Procesar e integrar las alertas tempranas de deforestación del IDEAM correspondientes al periodo 2017–2025 para construir una serie histórica de alertas por municipio.
* Generar variables espaciales derivadas relacionadas con riqueza de especies y características del territorio.
* Entrenar un modelo de aprendizaje automático que permita estimar el riesgo de generación de alertas de deforestación durante 2026 a partir del comportamiento histórico observado.
* Integrar los resultados en productos cartográficos y un geovisor interactivo que faciliten la exploración y comunicación de los territorios priorizados.



\## Justificación del uso de inteligencia artificial



La dinámica de la deforestación responde a procesos espaciales y temporales complejos que involucran múltiples variables y relaciones no lineales. Los métodos tradicionales de análisis permiten describir patrones históricos, pero presentan limitaciones para identificar tendencias futuras cuando intervienen simultáneamente diferentes fuentes de información.



En este proyecto se emplea un modelo de aprendizaje automático basado en Random Forest para analizar la relación entre el comportamiento histórico de las alertas tempranas de deforestación, variables territoriales y la presencia registrada de palmas amenazadas. El modelo estima el riesgo de generación de nuevas alertas de deforestación a nivel municipal, mientras que la información biológica permite priorizar aquellos territorios donde dicho riesgo coincide con la presencia de especies de interés para la conservación.



De esta manera, la inteligencia artificial actúa como una herramienta de apoyo para integrar grandes volúmenes de datos abiertos y generar información útil para procesos de planificación, monitoreo ambiental y conservación de la biodiversidad.



\## Alcance y limitaciones



El proyecto desarrolla un modelo predictivo a escala municipal utilizando la serie histórica de alertas tempranas de deforestación del IDEAM entre 2017 y 2025, complementada con registros abiertos de palmas amenazadas y variables espaciales derivadas.



Como resultado se generan mapas de riesgo, una base de datos integrada y un geovisor interactivo que permiten identificar municipios donde coinciden antecedentes de deforestación y presencia de especies amenazadas.



Los resultados corresponden a una aproximación predictiva basada en datos históricos y no constituyen una predicción determinística del comportamiento futuro de la deforestación. Su desempeño depende de la calidad, cobertura y representatividad de las fuentes de información utilizadas.



Entre las principales limitaciones se encuentran los sesgos inherentes a los registros biológicos, la disponibilidad desigual de observaciones entre regiones, la resolución espacial de las fuentes de datos y la naturaleza dinámica de los procesos de transformación del territorio.



En consecuencia, los resultados deben interpretarse como una herramienta de apoyo para la priorización territorial y la toma de decisiones, y no como un reemplazo de las evaluaciones ecológicas o de campo.

