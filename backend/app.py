from flask import Flask, request, jsonify
from cricket_score_predictor import predict_score
import psycopg2
import os

app = Flask(__name__)

# Database connection settings
DATABASE_URL = os.getenv('DATABASE_URL', 'dbname=predictions_db user=user password=password host=database')

def init_db():
    """Initialize the database and create a table if it doesn't exist."""
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Create table for storing predictions
    cur.execute('''
    CREATE TABLE IF NOT EXISTS predictions (
        id SERIAL PRIMARY KEY,
        input_data TEXT NOT NULL,
        predicted_score FLOAT NOT NULL
    )
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = data.get('inputData', '')

    # Call the prediction function
    predicted_score = predict_score(input_data)

    # Save the result to the database
    save_prediction_to_db(input_data, predicted_score)

    return jsonify({'prediction': predicted_score})

def save_prediction_to_db(input_data, predicted_score):
    """Save the prediction result to the database."""
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    # Insert the prediction result into the predictions table
    cur.execute('''
    INSERT INTO predictions (input_data, predicted_score)
    VALUES (%s, %s)
    ''', (input_data, predicted_score))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    # Initialize the database and create table if not exists
    init_db()

    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
