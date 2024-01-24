import streamlit as st
import pandas as pd 
import joblib

clf = joblib.load('data/Salary_model.pkl')
st.title('Calcula el salario!')

experience_level = st.number_input('Height:')
job_title = st.number_input('job_title:')
company_location = st.number_input('company_location:')
company_size = st.number_input('company_size:')

salary = st.selectbox(
    'Predice tu salario',  
)

if st.button('Submit'):
    X = pd.DataFrame([[experience_level, job_title, experience_level, company_location, company_size]], columns=["Experience level", "job title", "experience level", "company location", "company size"])
    prediction = clf.predict(X)[0]
    st.text(f"This pet is a {prediction}")
