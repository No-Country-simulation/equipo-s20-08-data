import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from pycaret.classification import load_model as pyc_load_model
from pycaret.classification import predict_model

# Configuración de la página
st.set_page_config(
    page_title="Fraud Detection Demo",
    page_icon="🔍",
    layout="wide"
)

# Cargar el modelo
@st.cache_resource
def load_model():
    try:
        model = pyc_load_model(r'C:\Users\jose-\Desktop\T\CODIGO_FINAL\equipo-s20-08-data\MODEL ML\model')
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Cargar los datos de test
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(r'C:\Users\jose-\Desktop\T\CODIGO_FINAL\equipo-s20-08-data\DATA\test.csv')
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

# Inicializar el estado de la sesión si no existe
if 'transaction_history' not in st.session_state:
    st.session_state.transaction_history = []
if 'total_transactions' not in st.session_state:
    st.session_state.total_transactions = 0
if 'total_fraud' not in st.session_state:
    st.session_state.total_fraud = 0
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Cargar modelo y datos
with st.spinner('Loading model and data...'):
    model = load_model()
    test_data = load_data()

if model is None or test_data is None:
    st.error("Could not load model or data. Please check the file paths and dependencies.")
    st.stop()

# Título principal
st.title("🔍 Fraud Detection System Demo")

# Crear columnas para las métricas
col1, col2, col3, col4 = st.columns(4)

# Métricas en tiempo real
with col1:
    st.metric("Total Transactions", st.session_state.total_transactions)
with col2:
    st.metric("Fraud Detected", st.session_state.total_fraud)
with col3:
    fraud_rate = (st.session_state.total_fraud / st.session_state.total_transactions * 100) if st.session_state.total_transactions > 0 else 0
    st.metric("Fraud Rate", f"{fraud_rate:.2f}%")
with col4:
    elapsed_time = int(time.time() - st.session_state.start_time)
    st.metric("Time Elapsed", f"{elapsed_time}s")

# Crear dos columnas para la visualización principal
left_col, right_col = st.columns([2, 1])

with left_col:
    # Gráfico de línea temporal de transacciones
    st.subheader("Transaction Timeline")
    if st.session_state.transaction_history:
        df_history = pd.DataFrame(st.session_state.transaction_history)
        fig = px.line(df_history, x='timestamp', y='amount', 
                     color='is_fraud',
                     color_discrete_map={True: 'red', False: 'green'},
                     title='Transaction Amount Over Time')
        st.plotly_chart(fig, use_container_width=True)

with right_col:
    # Última transacción
    st.subheader("Latest Transaction")
    if st.session_state.transaction_history:
        last_transaction = st.session_state.transaction_history[-1]
        
        # Crear un contenedor con estilo para la última transacción
        with st.container():
            st.markdown(
                f"""
                <div style="padding: 20px; border-radius: 10px; border: 2px solid {'red' if last_transaction['is_fraud'] else 'green'};">
                    <h3 style="color: {'red' if last_transaction['is_fraud'] else 'green'}">
                        {'⚠️ FRAUD DETECTED' if last_transaction['is_fraud'] else '✅ LEGITIMATE'}
                    </h3>
                    <p><strong>Amount:</strong> ${last_transaction['amount']:.2f}</p>
                    <p><strong>Time:</strong> {last_transaction['timestamp']}</p>
                    <p><strong>Risk Score:</strong> {last_transaction['risk_score']:.3f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

# Historial de transacciones
st.subheader("Recent Transactions")
if st.session_state.transaction_history:
    # Convertir el historial a DataFrame
    history_df = pd.DataFrame(st.session_state.transaction_history)
    # Mostrar las últimas 5 transacciones
    st.dataframe(
        history_df.tail(5)[['timestamp', 'amount', 'is_fraud', 'risk_score']],
        use_container_width=True
    )

# Control de velocidad de simulación
simulation_speed = st.slider("Simulation Speed (seconds)", 
                           min_value=1, 
                           max_value=10, 
                           value=2)

# Botón para generar nueva transacción
if st.button("Process Next Transaction"):
    # Tomar una muestra aleatoria del conjunto de test
    random_idx = np.random.randint(0, len(test_data))
    transaction = test_data.iloc[random_idx]
    
    # Hacer la predicción
    prediction = model.predict_proba(transaction.values.reshape(1, -1))[0]
    is_fraud = prediction[1] > 0.5
    
    # Crear registro de la transacción
    transaction_record = {
        'timestamp': datetime.now().strftime('%H:%M:%S'),
        'amount': float(transaction['amt']),
        'is_fraud': bool(is_fraud),
        'risk_score': float(prediction[1])
    }
    
    # Actualizar el estado
    st.session_state.transaction_history.append(transaction_record)
    st.session_state.total_transactions += 1
    if is_fraud:
        st.session_state.total_fraud += 1
    
    # Recargar la página para actualizar las visualizaciones
    time.sleep(simulation_speed)
    st.rerun()

# Botón para reiniciar la simulación
if st.button("Reset Simulation"):
    st.session_state.transaction_history = []
    st.session_state.total_transactions = 0
    st.session_state.total_fraud = 0
    st.session_state.start_time = time.time()
    st.rerun()