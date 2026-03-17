from pathlib import Path
import joblib
import pandas as pd

MODEL_PATH = (
    Path(__file__)
    .resolve()
    .parents[1]
    /"model/pipeline.joblib"
)

def load_model():
    return joblib.load(MODEL_PATH)

def predict_from_features(
    model, #modelo ya cargado
    features: dict, #diccionario con las 30 columnas de entrada
    threshold: float = 0.4
):
    
    #Convetir el dic a DataFrame
    df = pd.DataFrame([features])
    
    #Obtener la probabilidad de la clase 1
    #columna 0 → probabilidad de clase 0 (no churn),
    #columna 1 → probabilidad de clase 1 (churn).
    proba = model.predict_proba(df)[:, 1][0]
    
    #Aplicar trheshol para decidir la clase
    pred = int(proba >= threshold)
    
    return pred, proba
    
    
    