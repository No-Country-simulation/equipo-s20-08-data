
###  Informe sobre el Modelo de Machine Learning para Detección de Transacciones Fraudulentas
##  1. Introducción
El presente documento describe el contenido y análisis del notebook Jupyter titulado <strong>"MODELO DE ML PARA DETECTAR TRANSACCIONES FRAUDULENTAS"</strong>. El objetivo principal de este notebook es desarrollar un modelo de machine learning capaz de identificar transacciones fraudulentas a partir del conjunto de datos de kaggle (credit card transaction dataset (fraud detection)).
## 2. Descripción del Dataset
El dataset utilizado contiene información sobre transacciones, clientes y comercios. A continuación, se describen las principales variables:<br>
<b>Total de Columnas:</b> 43<br>
<b>Total de Filas:</b> 8 580 255 <br>
<b>Descripción de Columnas<br><br></b>
<br><b>Información del Cliente:<br></b>
•	<b>ssn: </b>Número de Seguro Social sintético que identifica a los individuos (anonimizado).<br>
•	<b>cc_num:</b> Número de tarjeta de crédito utilizada en las transacciones (anonimizado).<br>
•	<b>first, last:</b> Nombres y apellidos de los clientes (anonimizados).<br>
•	<b>gender:</b> Género del cliente (M, F, etc.).<br>
•	<b>street, city, state, zip:</b> Información de la dirección del cliente.<br>
•	<b>lat, long:</b> Latitud y longitud geográfica de la ubicación del cliente.<br>
•	<b>city_pop:</b> Población de la ciudad donde reside el cliente.<br>
•	<b>job:</b> Ocupación del cliente.<br>
•<b>	dob:</b> Fecha de nacimiento del cliente<br>
•	<b>acct_num:</b> Número de cuenta bancaria vinculada a las transacciones (anonimizado).<br>
•	<b>profile:</b> Identificador único del perfil de los clientes.<br>
<br><b>Detalles de la Transacción:</b><br>
•	<b>trans_num:</b> Identificador único de cada transacción.<br>
•	<b>trans_date:</b> Fecha de la transacción.<br>
•	<b>trans_time:</b> Hora de la transacción.<br>
•	<b>unix_time:</b> Representación en timestamp de la hora de la transacción.<br>
•	<b>category:</b> Categoría de la transacción (ej. comida, viajes, compras).<br>
•	<b>amt: </b>Monto involucrado en la transacción.<br>
•	<b>is_fraud:</b> Indica si la transacción es fraudulenta (1 para fraude, 0 en caso contrario).<br>
<br><b>Información del Comerciante:</b><br>
•	<b>merchant: </b>Nombre del comerciante donde se realizó la transacción (anonimizado).<br>
•	<b>merch_lat, merch_long: </b>Latitud y longitud de la ubicación del comerciante.<br>
<b>Métricas de Comportamiento y Riesgo:</b><br>
•	<b>customer_num_trans_1_day, customer_num_trans_7_day, customer_num_trans_30_day:</b> Número de transacciones realizadas por el cliente en los últimos 1, 7 y 30 días.<br>
•	<b>customer_avg_amout_1_day, customer_avg_amount_7_day, customer_avg_amount_30_day:</b> Promedio del monto de transacciones del cliente en los últimos 1, 7 y 30 días.<br>
•	<b>merchant_num_trans_1_day, merchant_num_trans_7_day, merchant_num_trans_30_day: </b>Número de transacciones procesadas por el comerciante en los últimos 1, 7 y 30 días.<br>
•	<b>merchant_risk_1_day, merchant_risk_7_day, merchant_risk_30_day, merchant_risk_90_day:</b> Puntajes de riesgo asociados con el comerciante en distintos períodos de tiempo.<br>
<br><b>Características Temporales:</b><br>
•	<b>trans_time_secs, trans_time_hrs:</b> Tiempo de la transacción convertido a segundos y horas para análisis.<br>
•<b>	trans_time_is_night:</b> Indica si la transacción ocurrió en horario nocturno (1 para noche, 0 en caso contrario).<br>
•	<b>trans_time_day: </b>Día del mes en que ocurrió la transacción.<br>
•	<b>trans_date_is_weekend: </b>Indica si la transacción ocurrió en un fin de semana (1 para fin de semana, 0 en caso contrario).<br>

## 3. Preprocesamiento de Datos<br>
<b>El preprocesamiento incluye las siguientes etapas:</b><br>
1.	<b>Conversión de Fecha de Nacimiento a Edad:</b> Se transforma la columna dob a age para obtener la edad del cliente.<br>
 <p align=center><img src=../SRC/ml/unoml.png width=300px heigth=200px><p>
2.	<b>Balanceo de clases:</b> Se toman en su totalidad los casos positivos de fraude y una muestra aleatoria del mismo tamaño de los casos negativos de fraude.<br>
<p align=center><img src=../SRC/ml/dosml.png width=300px heigth=200px><p>
 
3.	<b>Selección de Variables Relevantes:</b> Se eliminan columnas irrelevantes y se renombran algunas variables para mayor claridad.<br>
 <p align=center><img src=../SRC/ml/tresml.png width=300px heigth=200px><p>
4.	<b>división de variables categóricas y numéricas:</b> Se separan las variables de texto y numericas.<br>
 <p align=center><img src=../SRC/ml/cuatroml.png width=300px heigth=200px><p>
5.	<b>Codificación de Variables Categóricas:</b> Se convierte la variable gender y category en formato numérico usando OneHotEncoder.<br>
 <p align=center><img src=../SRC/ml/cincoml.png width=300px heigth=200px><p>
6.	<b>Estandarización de las variables Numéricas:</b> Se ponen todas la varibales numéricas en la misma escala usando StandardScaler.<br>
 <p align=center><img src=../SRC/ml/seisml.png width=300px heigth=200px><p>
<b>Dataset para entrenamiento:</b> <br>
•	<b>Datos del Cliente:</b><br>
	gender, lat, long, city_pop, dob(convertida en edad age).<br>
•	<b>Datos de la Transacción:</b><br>
category, amt, trans_time_hrs, trans_time_is_night, trans_time_day, trans_date_is_weekend <br>
•	<b>Historial de Transacciones del Cliente:</b><br>
customer_num_trans_1_day, customer_num_trans_7_day, customer_num_trans_30_day<br>
customer_avg_amout_1_day, customer_avg_amount_7_day, customer_avg_amount_30_day<br>
•	<b>Datos del Comercio:</b><br>
merch_lat, merch_long, merchant_num_trans_1_day, merchant_num_trans_7_day, merchant_num_trans_30_day, merchant_risk_1_day, merchant_risk_7_day, merchant_risk_30_day, merchant_risk_90_day<br>
•<b>	Variable Objetivo:</b><br>
<b>is_fraud:</b> Variable binaria que indica si la transacción es fraudulenta (1) o no (0).<br>
## 4. División del Conjunto de Datos<br>
Se divide el dataset en conjunto de entrenamiento y prueba para evaluar el modelo, 80% para entrenamiento y 20% para prueba.<br>
 <p align=center><img src=../SRC/ml/sieteml.png width=300px heigth=200px><p>
## 5. Construcción del Modelo<br>
Primero se construyó un modelo básico de regresión logística para determinar si las variables nos dan suficiente información: 
<p align=center><img src=../SRC/ml/ochoml.png width=300px heigth=200px><p>
Teniendo como resultado un:<br>
<b>Accuracy:</b> 0.83<br>
<b>Precision:</b> 0.89<br>
<b>Recall:</b> 0.75<br><br>
Con estos resultados se procedió a usar la librería pycaret para determinar el mejor modelo:
 <p align=center><img src=../SRC/ml/nueveml.png width=300px heigth=200px><p>
 <br>
 <p align=center><img src=../SRC/ml/diezml.png width=600px heigth=600px><p>
 En este caso fue <b>lightgbm </b>(Light Gradient Boosting Machine) con:<br>
<b>Accuracy: 0.93<br></b>
<b>Precision: 0.93<br></b>
<b>Recall: 0.93<br></b>
 <p align=center><img src=../SRC/ml/onceml.png width=600px heigth=600px><p>
## <b>6. Evaluación del Modelo<br></b>
Se analizan métricas de rendimiento:<br>
<b>Accuracy</b> (0.9328)<br>
Indica que el 93.28% de las predicciones fueron correctas.Buena métrica por las clases que están balanceadas.<br>
<b>AUC </b>(0.9842)<br>
Muestra que el modelo discrimina bien entre clases. Un valor cercano a 1 sugiere un excelente rendimiento en términos de separación de clases.
Recall (0.9328)<br>
Indica que el modelo identifica el 93.28% de los casos positivos correctamente. Es una buena métrica si el costo de los falsos negativos es alto.<br>
<b>Precisión (0.9328)<br></b>
Significa que el 93.28% de los casos clasificados como positivos realmente son positivos. Buen resultado si se quiere minimizar falsos positivos.<br>
Importancia de las características para el modelo<br>
 <p align=center><img src=../SRC/ml/doceml.png width=600px heigth=600px><p>
## <b>7. Conclusiones<br></b>
El modelo de machine learning desarrollado para la detección de transacciones fraudulentas ha demostrado un rendimiento excepcional, alcanzando métricas consistentes de 93.28% en accuracy, precisión y recall, junto con un AUC de 0.9842, lo que representa una mejora significativa respecto al modelo base de regresión logística. Este éxito se debe a la combinación de un preprocesamiento efectivo que incluye el balanceo de clases, la incorporación de variables categóricas transformadas, y la selección del algoritmo LightGBM mediante PyCaret. El modelo presenta un equilibrio óptimo entre la detección de fraudes y la minimización de falsos positivos, lo que lo hace altamente viable para su implementación en un entorno de producción


<br><br><br><br><br>















### Detección de Fraude en Transacciones Financieras: Un Enfoque Basado en Análiis de Datos y Machine Learning
### Análisis Financiero - Sistema de Deteccion de Fraudes 
<p align=center><img src=SRC/img/sup.jpg width=900px heigth=100px><p>



## 📌 Integrantes

<div align="letf">

<table>
  <thead>
    <tr>
      <th>Integrante</th>
      <th>Rol</th>
      </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Luciana Melisa Rabozzi Orelo</b></td>
      <td>Data Analist</td>
     </tr>
      <td><b>Diego Borges</b></td>
      <td>Data Analist</td>
      </tr>    
      <td><b>José Manuel Ardiles Ugaz</b></td>
      <td>Data Scientist</td>
      </tr>    
      <td><b>Mariano Ledezma</b></td>
      <td>PM</td>
      </tr>    
  </tbody>
</table>

</div>

## Metodologia 📖

Puedes encontrar mucho más sobre la gestión de este proyecto en la sección [Metodología](https://github.com/No-Country-simulation/equipo-s20-08-data/blob/main/DOC/metodologia.md)

## Esquema General de Trabajo 
Puedes encontrar mucho más sobre la gestión de este proyecto en la sección [Esquema General de Trabajo](https://github.com/No-Country-simulation/equipo-s20-08-data/blob/main/DOC/Esquema_General_de_Trabajo.md)

<br> 

## 📖 Descripción del Proyecto
Introducción
Este proyecto tiene como objetivo desarrollar un sistema de detección de fraudes en transacciones financieras utilizando técnicas de machine learning. El sistema se basa en un conjunto de datos históricos de transacciones y emplea algoritmos de clasificación para identificar patrones asociados con actividades fraudulentas y cuenta con un tablero interactivo desarrollado en Power BI para visualizar los resultados y un modelo de clasificación desplegado en una aplicación web.

## 🎯 Objetivos
•	Desarrollar un modelo de machine learning preciso para detectar transacciones fraudulentas.
•	Crear un tablero interactivo en Power BI para visualizar los datos y los resultados del modelo.
•	Desplegar el modelo en una aplicación web que permita realizar un análisis en tiempo real de una transacción.

## Tecnologías✔🛠️


### Tecnologías empleadas en el proyecto:
 ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?logo=power-bi&logoColor=white)
 ![Python](https://img.shields.io/badge/Python-0a6c9b?logo=Python&logoColor=white)
 ![Anaconda](https://img.shields.io/badge/Anaconda-06c318?logo=Anaconda&logoColor=white)

 - Bibliotecas para análisis de datos:
   * ![Numpy](https://img.shields.io/badge/Numpy-33d4ff?logo=numpy&logoColor=fff)
   * ![Pandas](https://img.shields.io/badge/Pandas-063cf4?logo=pandas&logoColor=fff)
 - Bibliotecas para visualización de datos:
   * ![Seaborn](https://img.shields.io/badge/Seaborn-005377?logo=Seaborn&logoColor=fff) 
   * ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?logo=matplotlib&logoColor=f0f)
  -	Bibliotecas para aprendizaje automático:
     * ![scikit-learn](https://img.shields.io/badge/scikit-learn-11557C?logo=scikit-learn&logoColor=f0f)
  - Despliegue:
     * ![streamlite](https://img.shields.io/badge/streamlite-11557C?logo=streamlite&logoColor=f0f)



### Herramienta para gestión del proyecto:
 - Tablero: ![Trello](https://img.shields.io/badge/Trello-0079BF?logo=trello&logoColor=white)
- Bitacora: ![Notion](https://img.shields.io/badge/Notion-000000?logo=Notion&logoColor=white)

- Repositorio:![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)
- Chats:![Slack](https://img.shields.io/badge/Slack-4A154B?logo=slack&logoColor=white)
![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?logo=whatsapp&logoColor=white)
- Reuniones: ![Google Meet](https://img.shields.io/badge/Google%20Meet-00897B?logo=google-meet&logoColor=white)
- Recursos Compartidos:![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?logo=google-drive&logoColor=white)

 **Power BI:** Visualización de Datos. 
- **Streamlit:**  Plataforma para la creación de aplicaciones web interactivas a partir de scripts de Python. 
- **Trello:** Herramienta de Gestión de Proyectos 
- **GitHub y Colab:** Desarrollo Colaborativo y Control de Versiones. 
- **Slack:** Comunicación diaria del equipo y colaboración en tiempo real.
- **Google Meet:** Reuniones diarias, planificación de sprint y coordinación de trabajo.
- **WhatsApp:** Comunicación instantánea para cuestiones urgentes.
- **Google Drive:** Almacenamiento y sincronización de documentación.





### ➡️ Estructura del Proyecto
La estructura de directorios se plantea: 

    /
    │
    ├── data/                          # Directorio principal de los datos
    │   ├── datos iniciales/           # Referencias a distintos archivos en formato csv 
    │
    ├── directorio/                    # preprocesado de datos xlsm
    │
    ├── codigo/                        # Cuadernos Jupyter 
        ├── EDA.ipynb                  # Análisis exploratorio de los datos (EDA)
        ├── visualizacion.pbix         # Visualización interactiva de los resultados (Power BI)
        └── ml.ipynb                   # Modelado predictivo usando Machine Learning


Metodología
1.	Recopilación de datos: Se recopilaron datos históricos de transacciones financieras de diversas fuentes.
2.	Preprocesamiento de datos: Los datos fueron limpiados, transformados y preparados para el entrenamiento del modelo.
3.	Exploración de datos (EDA): Se realizó un análisis exploratorio de los datos para identificar patrones y características relevantes.
4.	Modelado: Se entrenó un modelo de clasificación utilizando algoritmos como: ##Agregar--- Random Forest, XGBoost o redes neuronales.
5.	Evaluación del modelo: Se evaluó el rendimiento del modelo utilizando métricas como precisión, recall, F1-score y matriz de confusión.
6.	Despliegue: El modelo se desplegó en una aplicación web utilizando Streamlit y se integró con un tablero en Power BI para visualizar los resultados.
Resultados



## ➡️Resultados Esperados - Power Bi- Looker

El análisis de los datos en Power Bi, se implementa mediante un dashboard interactivo que permite visualizar:

- agregar.
- agregar.
- agregars.
- agregar.

## ➡️Resultados Esperados - Python

El análisis de los datos EDA, se implementa mediante un script en lenguaje python que permite visualizar:

- Valores descriptivos de las variables (media, mediana, desviación estandar,etc)
- Análisis Univariado
- Análisis Bivariado
- Análisis de Tendencias
- Correlación de variables

## ➡️Resultados Esperados - Machine Learning

El análisis de los datos en Power Bi, se implementa mediante un dashboard interactivo que permite visualizar:

- agregar
- agregar

## 📈Futuros Desarrollos

El presente proyecto constituye un punto de partida en la implementación de Técnicas de análisis de Ciencia de Datos e Intelegencia Artificial y hace posible a futuro ampliar y mejorar sus funcionalidades, además de incorporar nuevas caracteristicas que permitan incrementar continuamente su calidad, entre estas podemos mencionar: 

-   Permitir el ingreso de datos en tiempo real de distintas fuentes y formatos.
-   Mejorar el sistema de monitoreo para emitir alarmas.
-   Mejorar la ubicación en tiempo real.
-   Realizar procesamientos en parelelo para detectar semejanzas en los datos en tiempo real.

## 📌Referencias
El estado del proyecto esta en una fase ......


## 📌Presentación de los resultados del proyecto 🚀

</head>
<body>
    <div class="container">
        <p><h2>Link a la presentación final</h2></p>
        <h2><a class="button" href="https:......................" target="_blank">Ver Presentación</a></h2>
      <p><h2>Link al Dashboard</h2></p>
        <h2><a class="button" href="--------link al tablero------- " target="_blank">Ver Tablero</a></h2>
  </body>

  
![Proyecto No Country - Detecciòn de Fraude](https://github.com/No-Country-simulation/equipo-s20-08-data/tree/main)
</html>