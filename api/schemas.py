# api/schemas.py
# Esquemas Pydantic para la API de churn

from pydantic import BaseModel, Field


class ChurnFeatures(BaseModel):
    """
    Esquema de entrada para el modelo de churn.
    Los alias de los campos coinciden EXACTAMENTE con las columnas del CSV limpio.
    """

    # Variables numéricas (mismo nombre que en el CSV)
    senior_citizen: float = Field(..., ge=0, alias="SeniorCitizen")
    tenure: float = Field(..., ge=0, alias="tenure")
    monthly_charges: float = Field(..., ge=0, alias="MonthlyCharges")
    total_charges: float = Field(..., ge=0, alias="TotalCharges")

    # Dummies binarias (0/1) con alias iguales a las columnas del CSV
    gender_male: int = Field(..., ge=0, le=1, alias="gender_Male")
    partner_yes: int = Field(..., ge=0, le=1, alias="Partner_Yes")
    dependents_yes: int = Field(..., ge=0, le=1, alias="Dependents_Yes")
    phone_service_yes: int = Field(..., ge=0, le=1, alias="PhoneService_Yes")

    multiple_lines_no_phone_service: int = Field(
        ..., ge=0, le=1, alias="MultipleLines_No phone service"
    )
    multiple_lines_yes: int = Field(..., ge=0, le=1, alias="MultipleLines_Yes")

    internet_service_fiber_optic: int = Field(
        ..., ge=0, le=1, alias="InternetService_Fiber optic"
    )
    internet_service_no: int = Field(..., ge=0, le=1, alias="InternetService_No")

    online_security_no_internet_service: int = Field(
        ..., ge=0, le=1, alias="OnlineSecurity_No internet service"
    )
    online_security_yes: int = Field(..., ge=0, le=1, alias="OnlineSecurity_Yes")

    online_backup_no_internet_service: int = Field(
        ..., ge=0, le=1, alias="OnlineBackup_No internet service"
    )
    online_backup_yes: int = Field(..., ge=0, le=1, alias="OnlineBackup_Yes")

    device_protection_no_internet_service: int = Field(
        ..., ge=0, le=1, alias="DeviceProtection_No internet service"
    )
    device_protection_yes: int = Field(..., ge=0, le=1, alias="DeviceProtection_Yes")

    tech_support_no_internet_service: int = Field(
        ..., ge=0, le=1, alias="TechSupport_No internet service"
    )
    tech_support_yes: int = Field(..., ge=0, le=1, alias="TechSupport_Yes")

    streaming_tv_no_internet_service: int = Field(
        ..., ge=0, le=1, alias="StreamingTV_No internet service"
    )
    streaming_tv_yes: int = Field(..., ge=0, le=1, alias="StreamingTV_Yes")

    streaming_movies_no_internet_service: int = Field(
        ..., ge=0, le=1, alias="StreamingMovies_No internet service"
    )
    streaming_movies_yes: int = Field(..., ge=0, le=1, alias="StreamingMovies_Yes")

    contract_one_year: int = Field(..., ge=0, le=1, alias="Contract_One year")
    contract_two_year: int = Field(..., ge=0, le=1, alias="Contract_Two year")

    paperless_billing_yes: int = Field(..., ge=0, le=1, alias="PaperlessBilling_Yes")

    payment_method_credit_card_automatic: int = Field(
        ..., ge=0, le=1, alias="PaymentMethod_Credit card (automatic)"
    )
    payment_method_electronic_check: int = Field(
        ..., ge=0, le=1, alias="PaymentMethod_Electronic check"
    )
    payment_method_mailed_check: int = Field(
        ..., ge=0, le=1, alias="PaymentMethod_Mailed check"
    )


class PredictResponse(BaseModel):
    """
    Esquema de respuesta del endpoint /predict.
    """
    prediction: int               # 0 = no churn, 1 = churn
    probability: float            # probabilidad de churn (0–1)