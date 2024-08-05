

from flask import Flask, request, jsonify
from model_loading import load_model_and_encoders
import pandas as pd

app = Flask(__name__)

# Load the model and encoders
model, encoders = load_model_and_encoders()

# Get the list of feature names excluding the target variable 'class'
feature_names = [feature for feature in encoders.keys() if feature != 'class']

@app.route('/')
def home():
    return "Mushroom Classification API is running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if not isinstance(data, dict):
        return jsonify({'error': 'Invalid input format. Expected a JSON object.'}), 400

    features = []

    # Transform categorical features using the encoders
    for feature in feature_names:
        if feature in data:
            encoded_feature = encoders[feature].transform([data[feature]])[0]
            features.append(encoded_feature)
        else:
            return jsonify({'error': f'Missing feature: {feature}'}), 400

    # Predict
    prediction = model.predict([features])[0]
    result = 'poisonous' if prediction == 1 else 'edible'


    if prediction == 1:
        explanation = "The mushroom is poisonous because it has a foul odor and bruises easily."
    else:
        explanation = "The mushroom is edible."

    return jsonify({'prediction': result, 'explanation': explanation})

@app.route('/get_mushrooms', methods=['GET'])
def get_mushrooms():
    # Load the predictions
    predictions = pd.read_csv('data/predictions.csv')

    # Get indices of edible and poisonous mushrooms
    poisonous_mushrooms = predictions[predictions['predicted'] == 1].index.tolist()
    edible_mushrooms = predictions[predictions['predicted'] == 0].index.tolist()

    return jsonify({
        'poisonous_mushrooms': poisonous_mushrooms,
        'edible_mushrooms': edible_mushrooms
    })


if __name__ == '__main__':
    app.run(debug=True)
