import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo
clf = joblib.load('model/salary_model2.pkl')

# Mapeo de opciones para el título
job_titles = ['Principal Data Scientist', 'ML Engineer', 'Data Scientist', 'Applied Scientist', 'Data Analyst', 'Data Modeler', 'Research Engineer', 'Analytics Engineer', 'Business Intelligence Engineer', 'Machine Learning Engineer', 'Data Strategist', 'Data Engineer', 'Computer Vision Engineer', 'Data Quality Analyst', 'Compliance Data Analyst', 'Data Architect', 'Applied Machine Learning Engineer', 'AI Developer', 'Research Scientist', 'Data Analytics Manager', 'Business Data Analyst', 'Applied Data Scientist', 'Staff Data Analyst', 'ETL Engineer', 'Data DevOps Engineer', 'Head of Data', 'Data Science Manager', 'Data Manager', 'Machine Learning Researcher', 'Big Data Engineer', 'Data Specialist', 'Lead Data Analyst', 'BI Data Engineer', 'Director of Data Science', 'Machine Learning Scientist', 'MLOps Engineer', 'AI Scientist', 'Autonomous Vehicle Technician', 'Applied Machine Learning Scientist', 'Lead Data Scientist', 'Cloud Database Engineer', 'Financial Data Analyst', 'Data Infrastructure Engineer', 'Software Data Engineer', 'AI Programmer', 'Data Operations Engineer', 'BI Developer', 'Data Science Lead', 'Deep Learning Researcher', 'BI Analyst', 'Data Science Consultant', 'Data Analytics Specialist', 'Machine Learning Infrastructure Engineer', 'BI Data Analyst', 'Head of Data Science', 'Insight Analyst', 'Deep Learning Engineer', 'Machine Learning Software Engineer', 'Big Data Architect', 'Product Data Analyst', 'Computer Vision Software Engineer', 'Azure Data Engineer', 'Marketing Data Engineer', 'Data Analytics Lead', 'Data Lead', 'Data Science Engineer', 'Machine Learning Research Engineer', 'NLP Engineer', 'Manager Data Management', 'Machine Learning Developer', '3D Computer Vision Researcher', 'Principal Machine Learning Engineer', 'Data Analytics Engineer', 'Data Analytics Consultant', 'Data Management Specialist', 'Data Science Tech Lead', 'Data Scientist Lead', 'Cloud Data Engineer', 'Data Operations Analyst', 'Marketing Data Analyst', 'Power BI Developer', 'Product Data Scientist', 'Principal Data Architect', 'Machine Learning Manager', 'Lead Machine Learning Engineer', 'ETL Developer', 'Cloud Data Architect', 'Lead Data Engineer', 'Head of Machine Learning', 'Principal Data Analyst', 'Principal Data Engineer', 'Staff Data Scientist', 'Finance Data Analyst']

# Mapeo de opciones para la experiencia
experience_levels = ['SE', 'MI', 'EN', 'EX']

# Mapeo de opciones para la ubicación de la empresa
company_locations = ['ES', 'US', 'CA', 'DE', 'GB', 'NG', 'IN', 'HK', 'NL', 'CH', 'CF', 'FR', 'FI', 'UA', 'IE', 'IL', 'GH', 'CO', 'SG', 'AU', 'SE', 'SI', 'MX', 'BR', 'PT', 'RU', 'TH', 'HR', 'VN', 'EE', 'AM', 'BA', 'KE', 'GR', 'MK', 'LV', 'RO', 'PK', 'IT', 'MA', 'PL', 'AL', 'AR', 'LT', 'AS', 'CR', 'IR', 'BS', 'HU', 'AT', 'SK', 'CZ', 'TR', 'PR', 'DK', 'BO', 'PH', 'BE', 'ID', 'EG', 'AE', 'LU', 'MY', 'HN', 'JP', 'DZ', 'IQ', 'CN', 'NZ', 'CL', 'MD', 'MT']

# Mapeo de opciones para el tamaño de la empresa
company_sizes = ['L', 'S', 'M']

st.title('Calcula el salario!')

# Widget para seleccionar el título
job_title = st.selectbox('Seleccione su título:', job_titles)

# Widget para seleccionar la experiencia
experience_level = st.selectbox('Seleccione su nivel de experiencia:', experience_levels)

# Widget para seleccionar la ubicación de la empresa
company_location = st.selectbox('Seleccione la ubicación de su empresa:', company_locations)

# Widget para seleccionar el tamaño de la empresa
company_size = st.selectbox('Seleccione el tamaño de su empresa:', company_sizes)

if st.button('Calcular salario'):
    # Mapeo inverso para obtener los valores numéricos
    job_title_numeric = job_titles.index(job_title)
    experience_level_numeric = experience_levels.index(experience_level)
    company_location_numeric = company_locations.index(company_location)
    company_size_numeric = company_sizes.index(company_size)

    # Realizar la predicción
    X = [[job_title_numeric, experience_level_numeric, company_location_numeric, company_size_numeric]]
    prediction = clf.predict(X)
    
    st.text(f"El salario predicho es: {prediction}")




