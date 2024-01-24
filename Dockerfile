FROM python:3.8
RUN pip install pandas scikit-learn streamlit
COPY src/app.py /app/
COPY model/salary_model.pkl /app/model/salary_model.pkl 
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py"]
