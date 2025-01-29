import os
import sys
import traceback
from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import time
from datetime import datetime
from pycaret.classification import load_model, predict_model

app = Flask(__name__)
CORS(app)

# Cargar el modelo y los datos
def load_model_and_data():
    try:
        # Ruta al modelo de PyCaret
        model_path = 'C:\\Users\\jose-\\Desktop\\T\\CODIGO_FINAL\\equipo-s20-08-data\\MODEL ML\\model'
        
        # Cargar el modelo usando load_model de PyCaret
        model = load_model(model_path)
        
        # Cargar los datos de prueba
        data = pd.read_csv('C:\\Users\\jose-\\Desktop\\T\\CODIGO_FINAL\\equipo-s20-08-data\\DATA\\test.csv')
        

        
        # Imprimir información útil de depuración
        print("Modelo cargado exitosamente")
        print("Columnas del dataset:", list(data.columns))
        print("Número de transacciones:", len(data))
        
        return model, data
    
    except Exception as e:
        print(f"Error al cargar el modelo o datos: {e}")
        traceback.print_exc()
        return None, None
# Cargar diccionario de latitudes y longitudes, ciudades y estados y comercios
diccionario = pd.read_csv('C:\\Users\\jose-\\Desktop\\T\\CODIGO_FINAL\\equipo-s20-08-data\\DATA\\lat_log_dict.csv')
# Preparar características para predicción
def prepare_features(transaction):
    # Excluir la columna de fraude y cualquier otra no relevante para la predicción
    features_to_drop = ['is_fraud']
    prediction_features = transaction.drop(features_to_drop)
    return prediction_features

model, test_data = load_model_and_data()
current_index = 0

mu_dict = {'latitud': 37.477951556863495,
 'longitud': -92.15232327648042,
 'población de la ciudad': 289689.81822353014,
 'edad': 49.51685019935447,
 'monto': 304.6946011328398,
 'latitud del comercio': 37.47792923643546,
 'longitud del comercio': -92.15224454220724,
 'número de transacciones del cliente en 1 día': 3.0046041389785456,
 'número de transacciones del cliente en 7 días': 5.499520072569247,
 'número de transacciones del cliente en 30 días': 12.99957281184735,
 'horas de la hora de transacción': 11.49479463325106,
 'la transacción es nocturna': 0.29229690104001854,
 'día de la transacción': 3.374823323418349,
 'la transacción es en fin de semana': 0.35986119022002827,
 'promedio de monto del cliente en 1 día': 45.47115477923338,
 'promedio de monto del cliente en 7 días': 45.56409536316267,
 'promedio de monto del cliente en 30 días': 35.53581772250702,
 'número de transacciones del comercio en 1 día': 2551.7406600320655,
 'número de transacciones del comercio en 7 días': 50432.5217840643,
 'número de transacciones del comercio en 30 días': 555199.1554249203,
 'riesgo del comercio en 1 día': 3.497916798514862,
 'riesgo del comercio en 7 días': 9.250912389511212,
 'riesgo del comercio en 30 días': 16.13766006370905,
 'merchant_risk_90_day': 29.640196822985885}  # diccionario de medias
sigma_dict = {'latitud': 5.2272113688829,
 'longitud': 16.569934035170252,
 'población de la ciudad': 557962.831076326,
 'edad': 18.719298664733376,
 'monto': 381.522447005141,
 'latitud del comercio': 5.259804491321999,
 'longitud del comercio': 16.57971972170049,
 'número de transacciones del cliente en 1 día': 1.9976477377979904,
 'número de transacciones del cliente en 7 días': 2.6287160100631977,
 'número de transacciones del cliente en 30 días': 3.1233045231999834,
 'horas de la hora de transacción': 6.922034501739091,
 'la transacción es nocturna': 0.4548180105079615,
 'día de la transacción': 1.9760473300918984,
 'la transacción es en fin de semana': 0.47995949203391414,
 'promedio de monto del cliente en 1 día': 25.64128442002452,
 'promedio de monto del cliente en 7 días': 25.710857306767856,
 'promedio de monto del cliente en 30 días': 19.902356626744083,
 'número de transacciones del comercio en 1 día': 1414.0102027222517,
 'número de transacciones del comercio en 7 días': 28585.414328346127,
 'número de transacciones del comercio en 30 días': 314511.98280193435,
 'riesgo del comercio en 1 día': 2.2928722451969294,
 'riesgo del comercio en 7 días': 3.8326230704319806,
 'riesgo del comercio en 30 días': 4.793449441491533,
 'merchant_risk_90_day': 12.24559481043392}  #diccionario de desviaciones estándar


# Función para encontrar la ubicación más cercana
def find_closest_location(lat, lon, diccionario):
    # Encontrar la distancia más cercana
    diccionario['distance'] = ((diccionario['latitud'] - lat) ** 2 + (diccionario['longitud'] - lon) ** 2) ** 0.5
    closest_location = diccionario.loc[diccionario['distance'].idxmin()]
    return closest_location

@app.route('/get-transaction')
def get_transaction():
    global current_index
    
    if model is None or test_data is None:
        return jsonify({"error": "Modelo o datos no cargados correctamente"}), 500
    
    if current_index >= len(test_data):
        current_index = 0
    
    # Obtener la transacción actual
    transaction = test_data.iloc[current_index]
    
    # Preparar características para predicción
    prediction_features = prepare_features(transaction)
    
    # Hacer la predicción
    try:
        # Convertir la serie a DataFrame
        prediction_df = pd.DataFrame([prediction_features])
        
        # Realizar predicción usando predict_model de PyCaret
        predictions = predict_model(model, data=prediction_df)
        print(f"Predicciones generadas:\n{predictions}")
        # Encontrar la columna de probabilidad de fraude
        fraud_prob_columns = [col for col in predictions.columns if 'score' in col.lower()]
        print(f"Columnas encontradas con 'score': {fraud_prob_columns}")
        # Encontrar la columna de prediction_label
        prediction_label_columns = [col for col in predictions.columns if 'prediction_label' in col]
        if not prediction_label_columns:
            raise ValueError("No se encontró columna de etiqueta de predicción")

        if not fraud_prob_columns:
            raise ValueError("No se encontró columna de puntuación de fraude")

        # Usar la primera columna de puntuación encontrada
        risk_score_column = fraud_prob_columns[0]
        risk_score = predictions[risk_score_column].values[0]
        print(f"Puntuación de riesgo obtenida: {risk_score}")
        # Usar la primera columna de etiqueta de predicción encontrada
        prediction_label_column = prediction_label_columns[0]
        is_fraud = predictions[prediction_label_column].values[0] == 1 # Manejar el caso donde 'is_fraud' no exista
        #is_fraud = transaction.get('is_fraud', 0) == 1  # Manejar el caso donde 'is_fraud' no exista
        print(f"¿Es fraude?: {is_fraud}")
        
        # Función para desescalar un valor
        def descale_value(column_name, value):
            return (value * sigma_dict[column_name]) + mu_dict[column_name]

        # Obtener las latitudes y longitudes desescaladas
        descaled_lat = descale_value('latitud', transaction.get('latitud', 0))
        descaled_lon = descale_value('longitud', transaction.get('longitud', 0))
        
        # Obtener la información de la ubicación más cercana desde el diccionario
        location_info = find_closest_location(descaled_lat, descaled_lon, diccionario)
        
        # Crear respuesta con los datos desescalados y la ubicación más cercana
        response = {
            'id': int(time.time() * 1000),
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'amount': float(descale_value('monto', transaction.get('monto', 0)).round(2)),
            'merchant': location_info['comercio'],
            'isFraud': bool(is_fraud),
            'risk_score': float(risk_score),
            'ciudad': location_info['ciudad'],
            'estado': location_info['estado'],
            'Monto_promedio_del_cliente_en_30_días': float(descale_value('promedio de monto del cliente en 30 días', transaction.get('promedio de monto del cliente en 30 días', 0)).round(2)),
            'categoría_entertainment': transaction.get('categoría_entertainment', 0),
            'categoría_food_dining': transaction.get('categoría_food_dining', 0),
            'categoría_gas_transport': transaction.get('categoría_gas_transport', 0),
            'categoría_grocery_net': transaction.get('categoría_grocery_net', 0),
            'categoría_grocery_pos': transaction.get('categoría_grocery_pos', 0),
            'categoría_health_fitness': transaction.get('categoría_health_fitness', 0),
            'categoría_home': transaction.get('categoría_home', 0),
            'categoría_kids_pets': transaction.get('categoría_kids_pets', 0),
            'categoría_misc_net': transaction.get('categoría_misc_net', 0),
            'categoría_misc_pos': transaction.get('categoría_misc_pos', 0),
            'categoría_personal_care': transaction.get('categoría_personal_care', 0),
            'categoría_shopping_net': transaction.get('categoría_shopping_net', 0),
            'categoría_shopping_pos': transaction.get('categoría_shopping_pos', 0),
            'categoría_travel': transaction.get('categoría_travel', 0),
            'additional_details': {
                'latitud': descaled_lat,
                'longitud': descaled_lon,
                'ciudad': location_info['ciudad'],
                'estado': location_info['estado'],
                'comercio': location_info['comercio'],
            }
            
        }
        current_index += 1
        return jsonify(response)
    
    except Exception as e:
        print(f"Error en la predicción: {e}")
        traceback.print_exc()
        return jsonify({"error": "Error en la predicción"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)