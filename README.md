# 📡 Predicción de Churn en Telecomunicaciones

> **Proyecto real:** Análisis y predicción de cancelación de clientes en una empresa de telecomunicaciones. Enfoque profesional: desde el entendimiento del negocio hasta el modelado, siguiendo el flujo real de un Data Scientist.

---

## 🎯 Contexto del negocio

Una empresa de telecomunicaciones está **perdiendo clientes cada mes**. La gerencia necesita respuestas accionables:

| Pregunta de negocio | Objetivo |
|--------------------|----------|
| ¿Qué tipo de clientes se están yendo? | Segmentación y perfiles de riesgo |
| ¿Qué variables influyen más en la cancelación? | Drivers del churn |
| ¿Podemos predecir qué cliente está en riesgo? | Modelo predictivo |
| ¿Qué estrategia podríamos recomendar? | Acciones y recomendaciones |

Este no es un ejercicio académico: es un **problema real de negocio** abordado con criterio profesional.

---

## 📦 Dataset

- **Nombre:** [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (Kaggle)
- **Por qué este dataset:** variables numéricas y categóricas, valores faltantes, features de negocio (contrato, internet, facturación, antigüedad) y espacio para un EDA profundo antes de ML.

**Ubicación en el repo:** `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`

---

## 🗂 Estructura del proyecto

El trabajo se organiza en **6 fases**. El modelado (ML) llega solo después de dominar exploración, análisis y preparación de datos.

```
customer-churn-prediction/
├── data/                    # Dataset Telco Customer Churn
├── EDA/                     # Exploración y análisis
│   ├── EDA_churn.ipynb      # EDA inicial y exploración
│   └── univariate_bivariate_analysis.ipynb  # Análisis univariado y bivariado
└── README.md
```

---

## 🔎 Fase 1 — Entendimiento del problema

Antes de abrir Python, se responde con criterio:

- ¿Qué es **churn** y por qué es grave para la empresa?
- ¿Qué tipo de variable es *Churn*? (binaria)
- ¿Es un problema de **clasificación** o **regresión**?
- ¿Cuál sería el **costo de equivocarnos** (falsos positivos vs falsos negativos)?

Aquí se desarrolla **pensamiento crítico** y alineación con el negocio.

---

## 📊 Fase 2 — Exploración inicial (EDA nivel 1)

**Objetivo:** entender qué datos tenemos.

- Cargar dataset, `shape`, tipos de datos
- Identificar variables **numéricas** y **categóricas**
- Valores nulos e inconsistencias
- Preguntas clave: ¿columnas mal tipadas? ¿irrelevantes? ¿duplicados? ¿qué % de churn hay?

**Herramientas:** estadística descriptiva, distribuciones, medidas de tendencia central y dispersión.

---

## 📈 Fase 3 — Análisis univariado y bivariado

### Univariado
- Histogramas (numéricas), barplots (categóricas), boxplots
- Mediana vs media, detección de outliers
- Preguntas: ¿*tenure* está sesgada? ¿mayoría con contrato mensual? ¿target balanceado?

### Bivariado (pensar como analista)
- Cruzar variables con **Churn**: contrato, antigüedad, método de pago, cargo mensual, etc.
- Identificar patrones, variables más influyentes, correlaciones y multicolinealidad
- Herramientas: tablas cruzadas, heatmaps, correlaciones, análisis visual

---

## 🧹 Fase 4 — Limpieza y ETL

Enfoque tipo **Data Engineer**:

- Corregir tipos de datos
- Manejo de valores nulos
- Encoding de variables categóricas
- Escalado (y criterio: ¿antes o después del train/test split?)
- Train/test split y balanceo de clases si aplica

---

## 📊 Fase 5 — Feature engineering

Los datos no se usan “tal cual”:

- Ejemplos: `cliente_nuevo` (tenure &lt; 12), ratio `cargo_mensual / total_cargos`, agrupación de tipos de contrato, flag de alto gasto.
- Objetivo: crear señales que el modelo pueda aprovechar.

---

## 🤖 Fase 6 — Modelado

Solo cuando el problema y los datos están claros.

- **Modelos:** Regresión logística, Árbol de decisión, Random Forest, XGBoost (opcional).
- **Evaluación:** Accuracy, Precision, Recall, F1, matriz de confusión, curva ROC.
- **Pregunta de negocio:** ¿Es más grave un falso positivo o un falso negativo? La respuesta guía la métrica y el umbral.

---

## 🧠 Qué se aprende con este proyecto

| Área | Contenido |
|------|-----------|
| Fundamentos | Estadística descriptiva, probabilidad aplicada, inferencia básica |
| Datos | EDA profesional, limpieza real, visualización estratégica |
| Modelado | Supervisado (clasificación), evaluación de modelos |
| Negocio | Pensamiento crítico, storytelling con datos |

Cuando llegues al ML, sabrás **por qué** lo usas, **cuándo** aplicarlo y **qué significa** el resultado. No solo “`.fit()` y listo”.

---

## 📌 Flujo real de un Data Scientist

Este proyecto replica el flujo típico en la industria:

1. Entender el problema de negocio  
2. Explorar y entender los datos  
3. Limpiar y preparar datos  
4. Analizar patrones  
5. Construir features  
6. Modelar  
7. Evaluar  
8. Comunicar resultados  

No es una ruta solo académica; es una **ruta profesional**.

---

## 🚀 Cómo usar este repositorio

1. Clona el repo y crea un entorno virtual (recomendado).
2. Instala dependencias (p. ej. `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`).
3. Descarga el dataset [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) y colócalo en `data/` si no está incluido.
4. Sigue los notebooks en `EDA/` en orden para reproducir el análisis.
5. Avanza por las fases 4–6 según tu plan (limpieza, feature engineering, modelado).

---

*Proyecto alineado con la práctica real de Data Science en negocio.*
