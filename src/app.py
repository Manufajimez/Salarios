import streamlit as st
import pandas as pd 
import joblib

clf = joblib.load('model/salary_model.pkl')
st.title('Calcula el salario!')

job_title = st.number_input('job_title:', value=0, step=1)  # Asegurando que sea un número entero
experience_level = st.number_input('experience_level:', value=0, step=1)  # Asegurando que sea un número entero
company_location = st.number_input('company_location:', value=0, step=1)  # Asegurando que sea un número entero
company_size = st.number_input('company_size:', value=0, step=1)  # Asegurando que sea un número entero


if st.button('Calcular'):

   X=[[job_title, experience_level, company_location, company_size]]
   prediction = clf.predict(X)
   st.text(f"El salario predicho es: {prediction}")
