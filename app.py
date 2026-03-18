#Importamos Streamlit
import streamlit as st
import joblib #Para cargar el modelo
from pathlib import Path #Para acceder a rutas
import pandas as pd

st.set_page_config(
    page_title="Churn Predictor",
    page_icon="🔥",
    layout="wide", #Uso de toda la pantalla
    initial_sidebar_state="expanded" #Barra lateral expanmdidad
)

st.markdown("""
<style>
/* Fondo general */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e3a8a 100%);
}

.card {
    background: rgba(15, 23, 42, 0.72);
    backdrop-filter: blur(10px);
    padding: 1.25rem;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.35);
    margin-bottom: 1rem;
}

/* Barra superior */
[data-testid="stHeader"] {
    background: transparent;
}

/* Títulos */
h1, h2, h3, h4, p, label {
    color: #e5e7eb !important;
}

/* Título principal con sombra suave */
h1 {
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.35);
    font-weight: 800;
}

/* Botón principal */
.stButton > button {
    background: linear-gradient(90deg, #2563eb 0%, #3b82f6 100%);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    box-shadow: 0 6px 18px rgba(37, 99, 235, 0.35);
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1d4ed8 0%, #2563eb 100%);
    color: white;
}
</style>
""", unsafe_allow_html=True)

#Ruta del modelo
MODEL_PATH = Path(__file__).resolve().parent /"model/pipeline.joblib"

#Cargamos el modelo
model = joblib.load(MODEL_PATH)

st.title("📊Predictor de Churn")
st.write("Aplicación para estimar si un cliente de telecomunicaciones va a cancelar el servicio.")

col1, col2 = st.columns([2, 1])
with col1:
    # Formulario para clientes
    st.markdown("""
    <div class="card">
        <h3 style="margin-top: 0;">Datos del cliente</h3>
    </div>
    """, unsafe_allow_html=True)

    #Crear desplegables para elegir y poder ingresar valores
    senior_citizen = st.selectbox("¿Eres un adulto mayor? (NO(0), SI(1))", [0,1])
    tenure = st.number_input("Tiempo como cliente (meses)", min_value=0, max_value=100, value=12)
    monthly_charges = st.number_input("Cargo mensual", min_value=0.0, max_value=200.0, value=70.0)
    total_charges = st.number_input("Cargo total", min_value=0.0, max_value=10000.0, value=800.0)

with col2:
    st.subheader("Resumen")
    st.info("Completa los datos del cliente y presiona el botón para predecir churn.")

# Información personal
st.markdown("""
<div class="card">
    <h3 style="margin-top: 0;">Información personal</h3>
</div>
""", unsafe_allow_html=True)

# Servicios contratados
info_col1, info_col2, info_col3 = st.columns(3)
with info_col1:
    gender = st.selectbox("Género", ["Femenino", "Masculino"])
with info_col2:
    partner = st.selectbox("¿Tiene pareja?", ["NO", "SI"])
with info_col3:
    dependents = st.selectbox("¿Tiene personas dependientes?", ["NO", "SI"])

st.markdown("""
<div class="card">
    <h3 style="margin-top: 0;">Servicios contratados</h3>
</div>
""", unsafe_allow_html=True)

# Servicios contratados: tipo de teléfono e internet
service_col1, service_col2 = st.columns(2)
with service_col1:
    phone_service = st.selectbox("¿Tiene servicio de teléfono?", ["NO", "SI"])
    if phone_service == "SI":
        multiple_lines = st.selectbox("¿Tiene multiples lineas?", ["NO", "SI"])
    else:
        multiple_lines = "No phone service"
with service_col2:
    internet_service = st.selectbox(
        "Tipo de internet",
        ["DSL", "Fibra óptica", "Sin internet"]
    )

st.markdown("""
<div class="card">
    <h3 style="margin-top: 0;">Servicios adicionales</h3>
</div>
""", unsafe_allow_html=True)

# Servicios adicionales según internet
if internet_service == "Sin internet":
    online_security = "No internet service"
    online_backup = "No internet service"
    device_protection = "No internet service"
    tech_support = "No internet service"
    streaming_tv = "No internet service"
    streaming_movies = "No internet service"
    st.info("Como el cliente no tiene internet, los servicios adicionales no aplican.")
else:
    add_col1, add_col2 = st.columns(2)
    with add_col1:
        online_security = st.selectbox("Seguridad online", ["NO", "SI"])
        online_backup = st.selectbox("Backup online", ["NO", "SI"])
        device_protection = st.selectbox("Protección de dispositivos", ["NO", "SI"])
    with add_col2:
        tech_support = st.selectbox("Soporte técnico", ["NO", "SI"])
        streaming_tv = st.selectbox("Streaming TV", ["NO", "SI"])
        streaming_movies = st.selectbox("Streaming de peliculas", ["NO", "SI"])

st.markdown("""
<div class="card">
    <h3 style="margin-top: 0;">Contrato y pago</h3>
</div>
""", unsafe_allow_html=True)

# Contrato y forma de pago
contract_col1, contract_col2 = st.columns(2)
with contract_col1:
    contract = st.selectbox("Tipo de contrato", ["Mensual", "1 año", "2 años"])
    paperless_billing = st.selectbox("¿Recibe facturación sin papel?", ["NO", "SI"])
with contract_col2:
    payment_method = st.selectbox(
        "Metodo de pago",
        ["Tarjeta de crédito automática", "Cheque electrónico", "Cheque por correo"]
    )

# Convertir los inputs del formulario en el formato que espera el modelo.
def build_feature_dict():
    features = {
        "SeniorCitizen": senior_citizen,
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "gender_Male": 0,
        "Partner_Yes": 0,
        "Dependents_Yes": 0,
        "PhoneService_Yes": 0,
        "MultipleLines_No phone service": 0,
        "MultipleLines_Yes": 0,
        "InternetService_Fiber optic": 0,
        "InternetService_No": 0,
        "OnlineSecurity_No internet service": 0,
        "OnlineSecurity_Yes": 0,
        "OnlineBackup_No internet service": 0,
        "OnlineBackup_Yes": 0,
        "DeviceProtection_No internet service": 0,
        "DeviceProtection_Yes": 0,
        "TechSupport_No internet service": 0,
        "TechSupport_Yes": 0,
        "StreamingTV_No internet service": 0,
        "StreamingTV_Yes": 0,
        "StreamingMovies_No internet service": 0,
        "StreamingMovies_Yes": 0,
        "Contract_One year": 0,
        "Contract_Two year": 0,
        "PaperlessBilling_Yes": 0,
        "PaymentMethod_Credit card (automatic)": 0,
        "PaymentMethod_Electronic check": 0,
        "PaymentMethod_Mailed check": 0,
    }
    
    # Validaciones lógicas
    
    if gender == "Masculino":
        features["gender_Male"] = 1
        
    if partner == "SI":
        features["Partner_Yes"] = 1
        
    if dependents == "SI":
        features["Dependents_Yes"] = 1
        
    if phone_service == "SI":
        features["PhoneService_Yes"] = 1
        if multiple_lines == "SI":
            features["MultipleLines_Yes"] = 1
    else:
        features["MultipleLines_No phone service"] = 1
        
    if internet_service == "Fibra óptica":
        features["InternetService_Fiber optic"] = 1
    elif internet_service == "Sin internet":
        features["InternetService_No"] = 1
        features["OnlineSecurity_No internet service"] = 1
        features["OnlineBackup_No internet service"] = 1
        features["DeviceProtection_No internet service"] = 1
        features["TechSupport_No internet service"] = 1
        features["StreamingTV_No internet service"] = 1
        features["StreamingMovies_No internet service"] = 1
        
    if internet_service != "Sin internet":
        if online_security == "SI":
            features["OnlineSecurity_Yes"] = 1
        if online_backup == "SI":
            features["OnlineBackup_Yes"] = 1
        if device_protection == "SI":
            features["DeviceProtection_Yes"] = 1
        if tech_support == "SI":
            features["TechSupport_Yes"] = 1
        if streaming_tv == "SI":
            features["StreamingTV_Yes"] = 1
        if streaming_movies == "SI":
            features["StreamingMovies_Yes"] = 1
            
    if contract == "1 año":
        features["Contract_One year"] = 1
    elif contract == "2 años":
        features["Contract_Two year"] = 1
        
    if paperless_billing == "SI":
        features["PaperlessBilling_Yes"] = 1
        
    if payment_method == "Tarjeta de crédito automática":
        features["PaymentMethod_Credit card (automatic)"] = 1
        
    elif payment_method == "Cheque electrónico":
        features["PaymentMethod_Electronic check"] = 1
        
    elif payment_method == "Cheque por correo":
        features["PaymentMethod_Mailed check"] = 1
        
    return features


# Convertir el diccionario en DataFrame,
# hacer model.predict_proba(...),
# mostrar el resultado en pantalla.
threshold = 0.4 #Umbral de decision

if st.button("Predecir Churn"):
    #Llama a la función que arma el diccionario con todas las columnas del modelo
    features = build_feature_dict()
    #Convierte el diccionario en un DataFrame de una sola fila
    df_input = pd.DataFrame([features])
    
    proba = model.predict_proba(df_input)[:, 1][0]
    pred = int(proba >= threshold)
    
    st.write("---")
    st.subheader("Resultado")
    
    st.metric("Probabilidad de churn", f"{proba:.2%}")
    
    if pred == 1:
        st.error(f"El modelo predice CHURN, Threshold usado: {threshold}")
    else:
        st.success(f"El modelo predice NO CHURN. Threshold usado: {threshold}")
        
        



