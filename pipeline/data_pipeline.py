from pathlib import Path
from typing import Tuple
import pandas as pd

#Ruta al CSV original

DATA_PATH = (
    Path(__file__)
    .resolve()
    .parents[1]
    /"data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.copy()
    
    #Convertir TotalCharges a numero y relleanr nulos
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(0)
    
    #Ahora debemos convertir Churn a numerico, 0 y 1 
    # porque nuestro modelo no entenderá valores numericos
    df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})
    
    #Eliminar custormerID si existe
    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)
    
    #Convertir todas las variables categoricas a numericas
    #numéricas mediante one-hot encoding.
    df = pd.get_dummies(df, drop_first=True)
    
    return df
    
def split_features_target(
    df: pd.DataFrame, target: str = "Churn"
    ) -> Tuple[pd.DataFrame, pd.Series]:
    X = df.drop(columns=[target])
    y = df[target]
    return X, y
