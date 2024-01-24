import streamlit as st
import pandas as pd 
import joblib

clf = joblib.load('data/Salary_model.pkl')
st.title('Calcula el salario!')

job_title = st.number_input('job_title:')
experience_level = st.number_input('experience_level:')
company_location = st.number_input('company_location:')
company_size = st.number_input('company_size:')

# Quitar esta línea ya que no parece necesaria
# salary = st.selectbox('Predice tu salario', [])

if st.button('Submit'):
    X = pd.DataFrame([[job_title, experience_level, company_location, company_size]], columns=["job title", "experience level", "company location", "company size"])
    prediction = clf.predict(X)[0]
    st.text(f"El salario predicho es: {prediction}")
