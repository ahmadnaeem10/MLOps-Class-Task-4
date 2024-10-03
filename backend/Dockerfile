FROM python:3.9-slim

WORKDIR /app

COPY app.py /app/
COPY cricket_score_predictor.py /app/
COPY cricket_dataset.csv /app/

RUN pip install flask pandas scikit-learn psycopg2-binary  # Added psycopg2-binary for PostgreSQL

CMD ["python", "app.py"]
