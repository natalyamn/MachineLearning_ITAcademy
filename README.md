# Predicción de Suscripción de Clientes a Depósitos a Plazo

Este proyecto fue desarrollado como parte del curso de Machine Learning aplicado a Negocios de IT Academy, con el objetivo de automatizar la identificación de clientes más propensos a suscribirse a depósitos a plazo. A partir de características demográficas y financieras, se espera predecir la probabilidad de suscripción y analizar qué variables influyen más en la decisión.  

Con este enfoque, se podría aumentar la eficiencia de las campañas de marketing de depósitos a plazo, focalizando esfuerzos en los clientes con mayor probabilidad de conversión y optimizando los recursos del equipo de marketing.  

## Contenidos del Repositorio  

Además de los archivos del proyecto principal, este repositorio incluye otros ejercicios realizados durante el curso:  

- `Ejercicios extra/`: Contiene ejercicios adicionales como extracción de datos de una API y Web Scraping.
  
- `Proyecto Conceptual Tienda de Ropa/`: Incluye la descripción de otro proyecto conceptual con modelos de Machine Learning para cumplir objetivos específicos.  

### Archivos del proyecto de predicción de suscripción:  
- `1.- Descripción del proyecto.pdf`: Contiene más detalles sobre el proyecto.
- `2.- Proceso de Recolección de Datos.ipynb`: Incluye un esquema de cómo podría haber sido el proceso de obtención de datos.  
- `3.- EDA.ipynb`: Análisis exploratorio de datos, tratamiento de valores nulos y outliers, e identificación de variables relevantes.  
- `4.- Procesamiento de Datos.ipynb`: Tratamiento de datos, división del conjunto, codificación de variables y estandarización.  
- `5.- Resultados del proyecto.ipynb`: Entrenamiento, evaluación y comparación de modelos.  
- `app.py`: Archivo para el despliegue del modelo Random Forest con Streamlit.  
- `forest_model.pkl`: Modelo Random Forest entrenado.  
- `scaler.pkl`: Escalador utilizado para la normalización de los datos.  
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.  


## Modelos Utilizados  

1. **Clustering:** Identificación de subgrupos de clientes según características relevantes para segmentar campañas.
   
2. **Regresión Logística:** Modelo utilizado como línea base para el análisis comparativo.
  
3. **Random Forest:** Modelo principal que permitió analizar la importancia de las características y realizar predicciones.  


## Resultados del Proyecto  

### Principales Hallazgos  
- Las variables más relevantes para predecir la suscripción a depósitos a plazo fueron **saldo** y **edad**.  
- Focalizar campañas en clientes con **mayor saldo** y **menos deudas** podría incrementar las tasas de conversión.  
- La segmentación inicial mediante *clustering* sirve como herramienta complementaria para mejorar la eficiencia de las campañas.  

### Limitaciones y Áreas de Mejora  
- El *clustering* no logró subgrupos bien definidos.  
- El modelo Random Forest obtuvo un recall moderado, por lo que no identifica correctamente a todos los clientes interesados.  
- Sería necesario mejorar los modelos mediante la optimización de hiperparámetros y la eliminación de variables poco relevantes.  


## Despliegue del Modelo  

El modelo Random Forest se ha desplegado utilizando **Streamlit**. Esto permite a los usuarios interactuar con el modelo de manera sencilla, proporcionando las características de un cliente y obteniendo como resultado la probabilidad de que contrate un depósito a plazo. 

Link de la aplicación: [deposit-subscription](https://deposit-subscription.streamlit.app/)

[![image](https://github.com/user-attachments/assets/1a50861c-c9f7-4b35-995e-426b3e036357)](https://deposit-subscription.streamlit.app/)
