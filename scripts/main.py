

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os
from logging_setup import setup_logging

# Set up logging
logger = setup_logging()

def load_data(filepath):
    logger.info(f"Loading data from {filepath}...")
    return pd.read_csv(filepath)

def preprocess_data(data):
    logger.info("Preprocessing data...")
    encoders = {}
    for column in data.columns:
        if data[column].dtype == object:
            logger.info(f"Encoding column: {column}")
            encoder = LabelEncoder()
            data[column] = encoder.fit_transform(data[column])
            encoders[column] = encoder
    logger.info("Data preprocessing completed.")
    return data, encoders

# Create models directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Load and preprocess data
data = load_data('data/mushrooms.csv')
data, encoders = preprocess_data(data)

# Split data into features and target
X = data.drop('class', axis=1)
y = data['class']

# Split data into training and testing sets
logger.info("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
logger.info("Training the model...")
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
logger.info("Evaluating the model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
logger.info(f'Accuracy: {accuracy}')
logger.info(f'\nClassification Report:\n{report}')

# Save model and encoders
logger.info("Saving model and encoders...")
joblib.dump(model, 'models/mushroom_classifier.pkl')
joblib.dump(encoders, 'models/encoders.pkl')

# Save the predictions and actual labels for analysis
results = pd.DataFrame({'actual': y_test, 'predicted': y_pred})
results.to_csv('data/predictions.csv', index=False)

logger.info("Script execution completed.")


# Save model and encoders
logger.info("Saving model and encoders...")
joblib.dump(model, 'models/mushroom_classifier.pkl')
joblib.dump(encoders, 'models/encoders.pkl')

logger.info("Script execution completed.")
