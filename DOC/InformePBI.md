### INFORME BI
### 1 pantalla
<p align=center><img src=../SRC/TABLERO/TABLERO1.png width=600px heigth=600px><p>

### Resultados del Análisis
El presente análisis visualiza los datos de fraudes recopilados, ofreciendo una perspectiva clara sobre la frecuencia, los patrones y las tendencias de estos eventos. A continuación, se detalla la interpretación de cada gráfico:
### Cantidad de Eventos detectados
La proporción de transacciones que son fraudulentas frente a las legítimas se estiman en un 1.17% del total de transacciones analizadas son fraudulentas (23.55 mil fraudes), las cuales equivalen a una pérdida económica de 1.16 mil millones.<BR>
Estos datos cuantifican el impacto financiero de las actividades fraudulentas y subrayan la importancia de implementar medidas preventivas.
 
### Fraudes por años y meses
Este gráfico de líneas muestra la evolución del número de fraudes a lo largo del tiempo, desglosado por meses.<BR>
• Se observa tendencia constante en la cantidad de fraudes por meses,  el en rango de aproximandamente 1.8 mil- 2.10, con valores minimos registrados en el mes de mayo (1.50) y valores máximos para los meses de octubre (2.10 mil) y enero (2.11mil).<BR>
### Dias y Horarios de Fraudes
• Se puede apreciar la mayor actividad de actividades fraudulentas en horas nocturas con repecto a las diurna, con marcados incrementos en horarios de 22:00 hrs - 4:00hrs.<BR>
• Con respecto a los días de semana, se aprecia una mayor cantidad de fraudes los fines de semana.<BR>
Lo anterior sugiere que los delincuentes aprovechan determinados horarios para cometer sus actos.<BR>
### Mapa de Calor
• El mapa de calor permite visualizar geográficamente la concentración de fraudes. La región costera este presenta la mayor concentración, seguida por la región costera oeste y la región sudeste de los EEUU. Esta información es crucial para identificar áreas geográficas que requieren mayor atención y reforzar las medidas de seguridad.<BR>

### A partir de este análisis preliminar, podemos concluir que:<BR>
• Existe una tendencia constante en el tiempo anual.<BR>
• Los fraudes se concentran en determinados días de la semana y horas del día.<BR>
• Hay regiones geográficas con mayor incidencia de fraudes.<BR>
El costo financiero de los fraudes es significativo.<BR>
Para obtener una comprensión más profunda de los patrones de fraude y desarrollar estrategias de prevención más efectivas realizamos un análisis más detallado de los datos, incluyendo:<BR>
• Análisis de las características de las transacciones fraudulentas que permitan identificar las variables que mejor discriminan entre transacciones legítimas y fraudulentas.<BR>
• Análisis de las causas raíz subyacentes en los fraudes para implementar medidas correctivas.<BR>
 

### 2 pantalla
<p align=center><img src=../SRC/TABLERO/TABLERO2.png width=600px heigth=600px><p>

### Riesgo a través del tiempo: 
Este gráfico de línea muestra la evolución del nivel de riesgo de fraude a lo largo del tiempo. Se observa una tendencia creciente de estación en el periodo octubre-enero.<BR>
### Fraude por hora:<BR>
-------ver si el grafico es igual que el otro<BR>
Cual usar?
### Fraude por día de la semana:
. -------ver si el grafico es igual que el otro<BR>
Cual usar?<BR>
 
### Mapa de calor:
---según caracteristicas<BR>
Monto total de fraude y porcentaje:<BR>
---según características<BR>
 
 
### Conclusión General:
<STRONG> "El análisis de los datos de fraude revela patrones claros que pueden ser utilizados para mejorar las estrategias de prevención. La mayor concentración de fraudes durante las horas nocturnas y los fines de semana sugiere la necesidad de reforzar los controles de seguridad durante estos periodos. Además, la identificación de regiones geográficas con alta incidencia de fraudes permite focalizar los esfuerzos de prevención en áreas específicas. Estos hallazgos, junto con los resultados del modelo de machine learning, servirán como base para desarrollar un sistema de detección de fraudes más robusto y eficaz." </STRONG>
 
 
### 3 pantalla

<p align=center><img src=../SRC/TABLERO/TABLERO3.png width=600px heigth=600px><p>

### Análisis de Impacto del Modelo LightGBM en la Detección de Fraudes
El tablero presentado ofrece una comparación visual del impacto del modelo LightGBM en la detección de fraudes antes y después de su implementación. A continuación, se detalla la interpretación de cada gráfico:<BR>
### Comparación de la cantidad de fraudes antes y después del modelo
Este gráfico de líneas muestra una disminución significativa en la cantidad de fraudes detectados después de la implementación del modelo LightGBM. Antes de la implementación, se observaba un número considerable de fraudes, mientras que después se ha logrado reducir significativamente esta cantidad.
### Métricas de desempeño del modelo
Se presentan las métricas de evaluación del modelo LightGBM, incluyendo precisión, recall, F1-score, AUC y los valores de falsos positivos (FP), falsos negativos (FN), verdaderos positivos (TP) y verdaderos negativos (TN) a partir de las cuales se infiere:
1. Los altos valores de precisión, recall y F1-score indican que el modelo es capaz de identificar correctamente tanto las transacciones fraudulentas como las legítimas.
2. El valor de AUC cercano a 1 indica un excelente poder de discriminación del modelo.
### Fraudes por categoría
----detallar---minimos, máximos y tendencias---
### Conclusiones
Los resultados obtenidos demuestran que la implementación del modelo LightGBM ha tenido un impacto positivo en la detección y prevención de fraudes. El modelo ha demostrado ser altamente efectivo en la identificación de transacciones fraudulentas, lo que ha llevado a una reducción significativa en el número de fraudes y en las pérdidas económicas asociadas.<BR>
### Beneficios clave:
• Reducción significativa de fraudes: El modelo ha logrado reducir significativamente el número de transacciones fraudulentas.<br>
• Mayor precisión en la detección: Las métricas de evaluación del modelo demuestran una alta precisión en la identificación de fraudes.<br>
• Reducción de pérdidas económicas: La implementación del modelo ha resultado en una disminución significativa de las pérdidas financieras causadas por los fraudes.<br>
• Mejora de la seguridad: El modelo contribuye a fortalecer la seguridad de las transacciones y a proteger a los clientes.<br>


