#Api para la prediccion de CHURN

from typing import Dict, Any
from fastapi import FastAPI


#Cargar metodos del service
from service.service import load_model, predict_from_features
from api.schemas import ChurnFeatures, PredictResponse

#Crear instancia de FastAPI
#Variable app es la que se usa en uvicorn para correr el servidor
app = FastAPI(
    title="Customer Churn Prediction API",
    description="API para predecir churn de clientes Teclo usando modelo entrenado",
    version="1.0.0",
)

#Cargar el modelo

model = load_model()

#Endpoint de salud
@app.get("/health")
def health_check():
    """
    Endpoint simple para comprobar que la API está viva.
    Útil para pruebas rápidas o para sistemas de monitorización.
    """
    return {"status": "ok"}

#Endpoint de prediccion

@app.post("/predict", response_model=PredictResponse)
def predict(features: ChurnFeatures):
    
    # Convertir el modelo Pydantic a dict (lo que espera predict_from_features)
    # Usamos los alias para que las columnas coincidan con las del CSV/modelo
    features_dict = features.model_dump(by_alias=True)
    
    pred, proba = predict_from_features(
        model=model,
        features=features_dict,
        threshold=0.4,
    )
    
    #Construimos una respuesta
    response= {
        "prediction": int(pred),
        "probability": float(proba)
    }
    
    return response