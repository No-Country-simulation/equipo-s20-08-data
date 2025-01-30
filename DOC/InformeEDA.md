## Informe de la exploración de datos EDA
##  Resumen de hallazgos
Patrones:<br>
Se identificaron patrones de transacciones fraudulentas en ciertas categorías y horarios específicos.<br>
Los fraudes tienden a ocurrir más frecuentemente durante la noche y los fines de semana.<br>
<b>Relaciones:</b><br>
Existe una correlación significativa entre el número de transacciones y la probabilidad de fraude.<br>
Los comerciantes con un alto número de transacciones diarias presentan un mayor riesgo de fraude.<br>
<b>Anomalías:</b><br>
Se detectaron valores atípicos en las columnas amt y merchant_risk_30_day, algunos de los cuales están asociados con fraudes.<br>
Se encontraron duplicados en la columna trans_num, que deben ser revisados y eliminados si es necesario.<br>
### Columnas del DataFrame
<b>trans_date<br>
trans_time<br>
unix_time<br>
amt<br>
customer_num_trans_1_day<br>
customer_num_trans_7_day<br>
customer_num_trans_30_day<br>
customer_avg_amout_1_day<br>
customer_avg_amount_7_day<br>
customer_avg_amount_30_day<br>
merchant_num_trans_1_day<br>
merchant_num_trans_7_day<br>
merchant_num_trans_30_day<br>
merchant_risk_1_day<br>
merchant_risk_7_day<br>
merchant_risk_30_day<br>
merchant_risk_90_day<br>
is_fraud<br>
trans_num<br>
category<br>
merchant<br>
gender<br>
city<br>
state<br>
city_pop<br>
job<br>
dob<br>
age<br>
profile<br>
lat<br>
long<br>
merch_lat<br>
merch_long<br>
trans_time_is_night<br>
trans_time_day<br>
trans_date_is_weekend<br>

</b>


## Visualizaciones
Para mejorar la comprensión de los datos y los hallazgos, se pueden incluir las siguientes visualizaciones:<br>
<b>Gráficos de barras:<br></b>
<b>Distribución de transacciones fraudulentas por categoría:</b>
<br><br>--imagen--<br><br>
<p align=center><img src=SRC/EDA/unoEDA.png width=300px heigth=300px><p>

<b>Número de transacciones fraudulentas por hora del día:</b>
<br><br>--imagen--<br><br>
<p align=center><img src=SRC/EDA/dosEDA.png width=300px heigth=300px><p>
<b>Gráficos de dispersión:</b>
<br><br>--imagen--<br><br>
<p align=center><img src=SRC/EDA/tresEDA.png width=300px heigth=300px><p>
<b>Relación entre el monto de la transacción (amt) y la probabilidad de fraude:</b>
<br><br>--imagen--<br><br>
<p align=center><img src=SRC/EDA/cuatroEDA.png width=300px heigth=300px><p>
<b>Relación entre el riesgo del comerciante (merchant_risk_30_day) y la probabilidad de fraude:</b>
<br><br>--imagen--<br><br>
<p align=center><img src=../SRC/EDA/cincoEDA.png width=300px heigth=300px><p>
<b>Mapas de calor:</b>

Correlación entre diferentes variables numéricas:</b>

### Pasos para seguir
<b>Normalizacion:<br></b>
<b>Normalización y estandarización:</b> Asegurarse de que las variables numéricas estén en una escala comparable.<br>
<b>Análisis posterior:<br></b>
<b>Modelización de datos: </b>Utilizar técnicas de modelización como regresión logística, árboles de decisión o redes neuronales para predecir la variable is_fraud.<br>
<b>Validación cruzada:</b> Implementar técnicas de validación cruzada para evaluar la robustez de los modelos.<br>
<b>Optimización de hiperparámetros:</b> Ajustar los hiperparámetros de los modelos para mejorar su rendimiento.<br>
<b>Evaluación de modelos: </b>Utilizar métricas de evaluación como precisión, recall, F1-score, y AUC-ROC para medir el desempeño de los modelos.<br>
## Conclusiones<br>
La identificación de patrones y relaciones en los datos puede ayudar a desarrollar modelos predictivos más precisos.<br>
La limpieza y preparación de los datos son pasos cruciales para garantizar la calidad del análisis.<br>
Las visualizaciones pueden proporcionar una comprensión más clara de los hallazgos y facilitar la comunicación de los resultados.<br>
