import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Load dataset
df = pd.read_csv('cricket_dataset.csv')

# Data preprocessing: convert categorical data using dummy encoding
df_encoded = pd.get_dummies(df, columns=['batting_team', 'bowling_team', 'city'])

# Prepare the dataset
X = df_encoded.drop('runs_x', axis=1)  # features
y = df_encoded['runs_x']  # target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Decision Tree model
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train, y_train)

# Evaluate the model
dt_score = dt_model.score(X_test, y_test)
print(f'Decision Tree Score: {dt_score}')

# Function to make predictions based on input data
def predict_score(input_data):
    # Assuming input_data is in the correct format that matches the model features
    prediction = dt_model.predict([input_data])  # Modify to accept the correct input format
    return prediction[0]  # Return the predicted score
