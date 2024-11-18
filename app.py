import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo y el escalador desde archivos
with open('forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)


# Título de la aplicación
st.title('Predicción de Suscripción a Depósito de los Clientes')


# Entrada de datos demográficos del usuario
st.header('Datos Demográficos')

age = st.number_input('Edad:', min_value=0, max_value=125)

job = st.selectbox('Trabajo:', 
                   ('management', 'blue-collar', 'technician', 'admin.', 
                    'services', 'housemaid', 'self-employed', 'entrepreneur',
                    'unemployed', 'retired', 'student'),
                  index=None, placeholder='Selecciona un trabajo...',)
st.write('Has seleccionado: ', job)

marital = st.radio('Estado civil:', ['single', 'married', 'divorced'])

education = st.radio('Educación:', ['primary', 'secondary', 'tertiary'])


# Entrada de datos financieros del usuario
st.header('Datos Financieros')

balance = st.number_input('Saldo:')

default = st.radio('Incumplimiento de Crédito:', ['no', 'yes'])

housing = st.radio('Hipoteca:', ['no', 'yes'])

loan = st.radio('Préstamo personal:', ['no', 'yes'])


# Crear un DataFrame con las entradas
user_data = pd.DataFrame({
    'age': [age],
    'job': [job],
    'marital': [marital], 
    'education': [education],
    'default': [default],
    'balance': [balance],
    'housing': [housing],
    'loan': [loan]
})

# Label Encoding de las características 'default', 'housing', 'loan' y 'education'
user_data['default'] = user_data['default'].map({'no': 0, 'yes': 1}).astype(int)
user_data['housing'] = user_data['housing'].map({'no': 0, 'yes': 1}).astype(int)
user_data['loan'] = user_data['loan'].map({'no': 0, 'yes': 1}).astype(int)
user_data['education'] = user_data['education'].map({'primary': 1, 'secondary': 2, 'tertiary': 3}).astype(int)

# One-Hot Encoding de las características 'job' y 'marital'
grouped_jobs = {'management': 'management',
                'blue-collar': 'blue-collar',
                'technician': 'technician',
                'admin.': 'admin.',  
                'services': 'services_group',
                'housemaid': 'services_group',
                'self-employed': 'independent_group',
                'entrepreneur': 'independent_group',
                'unemployed': 'inactive_group',
                'retired': 'inactive_group',
                'student': 'inactive_group'}
user_data['job'] = user_data['job'].map(grouped_jobs)

user_encoded_data = pd.get_dummies(user_data, columns=['job', 'marital'])

# Asegurar que las columnas están en el orden correcto
required_columns = [
    'age', 'education', 'default', 'balance', 'housing', 'loan',
    'job_admin.', 'job_blue-collar', 'job_inactive_group', 'job_independent_group', 
    'job_management', 'job_services_group', 'job_technician',
    'marital_divorced', 'marital_married', 'marital_single'
]

# Agregar columnas faltantes con valor 0
for col in required_columns:
    if col not in user_encoded_data.columns:
        user_encoded_data[col] = 0

# Reordenar las columnas
user_encoded_data = user_encoded_data[required_columns]

# Estandarizar las entradas
user_encoded_standardized_data = scaler.transform(user_encoded_data[['age', 'balance']])

# Realizar la predicción
prediction = model.predict(user_encoded_standardized_data)


# Mostrar la predicción
st.header('Resultado de la Predicción')
if prediction == 1: 
    st.success('El cliente probablemente SÍ contratará un depósito a plazo.')
else:
    st.error('El cliente probablemente NO contratará un depósito a plazo.')