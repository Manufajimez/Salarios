FROM python:3.8
RUN pip install pandas scikit-learn streamlit 
RUN pip install joblib==1.1.0
COPY src/app.py /app/
COPY model/salary_model2.pkl /app/model/salary_model2.pkl 
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py"]
