FROM python:3.8.13
WORKDIR /app
RUN pip install pyodbc==4.0.34

COPY Dev/sqlManagerLib/SqlReader.py .

CMD python SqlReader.py