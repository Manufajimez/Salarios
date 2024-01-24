FROM python:3.8
RUN pip install pandas scikit-learn streamlit
COPY src/app.py /app/
COPY model/Salary_model.pkl /app/model/Salary_model.pkl 
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py"]
