# 📊 Customer Churn Prediction (Telco) — End‑to‑End

Proyecto de **predicción de churn** (cancelación) en telecomunicaciones con un flujo completo:

- **ETL / limpieza** y one‑hot encoding
- **Entrenamiento** de un `Pipeline` de scikit‑learn (escalado + regresión logística)
- **API** de predicción con FastAPI (`/predict`)
- **Interfaz** visual con Streamlit (para probar el modelo sin escribir JSON)

---

## 🎯 Objetivo

Predecir la probabilidad de churn de un cliente y devolver:

- `prediction`: 0 (no churn) / 1 (churn)
- `probability`: probabilidad estimada de churn \([0, 1]\)

---

## 📦 Dataset

Dataset base: **Telco Customer Churn** (Kaggle).

- **Archivo original**: `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`
- El pipeline limpia y transforma (dummies) para alimentar el modelo.

> Nota: el entrenamiento usa `pd.get_dummies(..., drop_first=True)`, por lo que las columnas finales son dummies con nombres como `Contract_Two year`, `OnlineSecurity_No internet service`, etc.

---

## 🧱 Stack / Tecnologías

- **Python** (recomendado 3.10+)
- **Pandas / NumPy**
- **scikit‑learn**
- **FastAPI + Uvicorn**
- **Streamlit**

---

## 🗂️ Estructura del proyecto (carpetas clave)

```
customer-churn-prediction/
├── api/
│   ├── api.py               # FastAPI app + endpoint /predict
│   └── schemas.py           # Esquemas Pydantic (entrada/salida)
├── pipeline/
│   └── data_pipeline.py     # load_data / clean_data / split_features_target
├── service/
│   └── service.py           # load_model / predict_from_features
├── training/
│   └── train.py             # entrenamiento + guardado pipeline.joblib
├── model/
│   └── pipeline.joblib      # artefacto entrenado (se genera al entrenar)
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── telco_churn_clean.csv (opcional/derivado)
└── app.py                   # Streamlit UI
```

---

## 🚀 Puesta en marcha

### 1) Crear entorno e instalar dependencias

```bash
python -m venv .venv
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Instalar:

```bash
pip install -U pip
pip install pandas scikit-learn joblib fastapi uvicorn streamlit pydantic
```

---

## 🏋️ Entrenar el modelo

Entrena y guarda el pipeline en `model/pipeline.joblib`:

```bash
python -m training.train
```

Al terminar verás métricas (classification report, matriz de confusión y ROC‑AUC).

---

## 🔌 Ejecutar la API (FastAPI)

Desde la raíz del proyecto:

```bash
uvicorn api.api:app --reload
```

Endpoints útiles:

- **Health check**: `GET /health`
- **Predicción**: `POST /predict`
- **Swagger**: `GET /docs`

---

## 🧪 Ejemplo de request a `/predict`

El `POST /predict` espera un JSON con **las mismas columnas del CSV limpio/dummies** (los `alias` están alineados con esas columnas).

Ejemplo (perfil de churn alto):

```json
{
  "SeniorCitizen": 1,
  "tenure": 1,
  "MonthlyCharges": 110.0,
  "TotalCharges": 110.0,
  "gender_Male": 1,
  "Partner_Yes": 0,
  "Dependents_Yes": 0,
  "PhoneService_Yes": 1,
  "MultipleLines_No phone service": 0,
  "MultipleLines_Yes": 1,
  "InternetService_Fiber optic": 1,
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
  "StreamingTV_Yes": 1,
  "StreamingMovies_No internet service": 0,
  "StreamingMovies_Yes": 1,
  "Contract_One year": 0,
  "Contract_Two year": 0,
  "PaperlessBilling_Yes": 1,
  "PaymentMethod_Credit card (automatic)": 0,
  "PaymentMethod_Electronic check": 1,
  "PaymentMethod_Mailed check": 0
}
```

Respuesta:

```json
{
  "prediction": 1,
  "probability": 0.89
}
```

---

## 🖥️ Ejecutar la interfaz (Streamlit)

La UI permite probar el modelo sin escribir JSON:

```bash
streamlit run app.py
```

---

## ⚙️ Notas sobre `threshold`

El proyecto usa un umbral (threshold) para convertir probabilidad en clase:

- `probability >= threshold` ⇒ `prediction = 1` (churn)
- `probability < threshold` ⇒ `prediction = 0` (no churn)

Actualmente el threshold usado en el servicio/API es **0.4** (ver `service/service.py` y `api/api.py`).

---


