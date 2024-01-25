import streamlit as st
import pandas as pd 
import joblib

# Asegúrate de que 'clf' sea realmente tu modelo y no un DataFrame
#clf = joblib.load('model/salary_model2.pkl')


# Cargar datos desde el CSV
data = pd.read_csv('/data/salarios_nuevo.csv')

st.title('Calcula el salario!')

# Mapeo para 'job_title'
job_title_mapping = dict(zip(data['job_title'].unique(), data['job_title_label'].unique()))

# Mapeo para 'experience_level'
experience_level_mapping = dict(zip(data['experience_level'].unique(), data['experience_level_label'].unique()))

# Mapeo para 'company_location'
company_location_mapping = dict(zip(data['company_location'].unique(), data['company_location_label'].unique()))

# Mapeo para 'company_size'
company_size_mapping = dict(zip(data['company_size'].unique(), data['company_size_label'].unique()))


st.title('Calcula el salario!')

job_title = st.selectbox('Job Title:', list(job_title_mapping.keys()))
experience_level = st.selectbox('Experience Level:', list(experience_level_mapping.keys()))
company_location = st.selectbox('Company Location:', list(company_location_mapping.keys()))
company_size = st.selectbox('Company Size:', list(company_size_mapping.keys()))


job_title_int = next(key for key, value in job_title_mapping.items() if value == job_title)
experience_level_int = next(key for key, value in experience_level_mapping.items() if value == experience_level)
company_location_int = next(key for key, value in company_location_mapping.items() if value == company_location)
company_size_int = next(key for key, value in company_size_mapping.items() if value == company_size)

# Realizar la predicción
# X = [[job_title_int, experience_level_int, company_location_int, company_size_int]]
# prediction = clf.predict(X)
# st.text(f"El salario predicho es: {prediction}")



