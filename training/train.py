from pathlib import Path
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from pipeline.data_pipeline import load_data, clean_data, split_features_target

#Ruta para guardar el pipeline entrenado
MODEL_PATH = (
    Path(__file__)
    .resolve()
    .parents[1]
    /"model/pipeline.joblib"
)

def build_pipeline() -> Pipeline:
    #Pipeline de prepocesamiento
    clf = LogisticRegression(
        max_iter=1000,
        class_weight="balanced", #balancea para hacer peso a la variable
        random_state=42
    )
    
    pipeline = Pipeline(
        steps = [
            ("scaler", StandardScaler()),
            ("model", clf)
        ]
    )
    return pipeline

def train(threshold: float = 0.40) -> None: #0.35 como umbral de probabilidad
    #Entrenar modelo, evaluar y guardar
    
    #Cargar y limpiar datos
    df_raw = load_data()
    df_clean = clean_data(df_raw)
    X, y = split_features_target(df_clean)
    
    #Division train / test
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y #Mantener proporcion de churn
    )

    #Construir y entrenar el pipeline
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)
    
    #Evalauación implementando el threshold
    y_prob = pipeline.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= threshold).astype(int)
    
    print(f" Resultados con threshold = {threshold}")
    print(classification_report(y_test, y_pred))
    print("Matriz de confusión: ")
    print(confusion_matrix(y_test, y_pred))
    
    roc_auc = roc_auc_score(y_test, y_prob)
    print(f"ROC-AUC: {roc_auc:.3f}")
    
    #Ahora vamos a guardar el modelo entrenado
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Modelo guardado en: {MODEL_PATH}")


if __name__ == "__main__":
    train()
    
    