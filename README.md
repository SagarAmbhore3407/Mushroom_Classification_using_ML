# Mushroom_Classification_using_ML
## Project Overview

The Audubon Society Field Guide to North American Mushrooms contains descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom (1981). Each species is labelled as either definitely edible, definitely poisonous, or maybe edible but not recommended. This last category was merged with the toxic category. The Guide asserts unequivocally that there is no simple rule for judging a mushroom's edibility, such as "leaflets three, leave it be" for Poisonous Oak and Ivy.

The main goal of this project is to predict whether a mushroom is poisonous or edible based on its features using classical machine learning tasks like data exploration, data cleaning, feature engineering, model building, and model testing.


## ML Algorithm used

Logistic Regression: For binary classification of mushrooms as edible or poisonous.
Decision Tree Classifier: To create a decision tree model for classification.
Random Forest Classifier: To improve the accuracy of predictions by using an ensemble method.
Support Vector Machine (SVM): For creating a hyperplane that best separates the classes.
K-Nearest Neighbors (KNN): For instance-based learning by considering the nearest neighbors.

## Project Structure

Mushroom_Classification/
│
├── data/
│   └── mushrooms.csv
│
├── models/
│   ├── mushroom_classifier.pkl
│   ├── encoders.pkl
│
├── notebooks/
│   └── eda.ipynb
│
├── scripts/
│   └── main.py
│
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── data_loading.py
│   ├── model_loading.py
│   ├── dashboard.py
│
└── requirements.txt



## Installation

1. **Clone the repository**

   git clone https://github.com/your-username/Mushroom_Classification.git
   cd Mushroom_Classification

2. Create a virtual environment and activate it:

    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`

3. Install Required Package:
    pip install -r requirements.txt



## Data

The dataset used in this project is located in the data/ directory.

## Notebooks

The notebooks/ directory contains the eda.ipynb notebook, which includes exploratory data analysis and visualization of the dataset.


## Scripts

main.py: This script is used to train the machine learning model and save the trained model and encoders.

logging_setup.py: This module sets up the logging configuration for the project.
                  This will create a log file in root directory of project and That file contains 
                  detailed logs of the script execution.

data_loading.py: This module contains functions to load and pre-process the data.

model_loading.py: This module contains functions to load the trained model and encoders.

app.py: This Flask application provides an API for predicting mushroom edibility based on input features.

dashboard.py: This Dash application provides a dashboard for visualizing the prediction results and insights.


## Running the Project

1. Run the Exploratory Data Analysis (EDA) Notebook:
    Open the notebooks/eda.ipynb file in Jupyter Notebook or Jupyter Lab and run all the cells to perform data exploration and visualization.
    
2. Train the Model:
   python scripts/main.py


3. Start the Flask API:
   python src/app.py

4. Test the API:
   
    curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
    "cap-shape": "x",
    "cap-surface": "s",
    "cap-color": "n",
    "bruises": "t",
    "odor": "p",
    "gill-attachment": "f",
    "gill-spacing": "c",
    "gill-size": "n",
    "gill-color": "k",
    "stalk-shape": "e",
    "stalk-root": "e",
    "stalk-surface-above-ring": "s",
    "stalk-surface-below-ring": "s",
    "stalk-color-above-ring": "w",
    "stalk-color-below-ring": "w",
    "veil-type": "p",
    "veil-color": "w",
    "ring-number": "o",
    "ring-type": "p",
    "spore-print-color": "k",
    "population": "s",
    "habitat": "u"
    }'


    Using Postman:
    Set the URL to http://127.0.0.1:5000/predict
    Set the method to POST
    Set the header Content-Type to application/json
    Add the JSON body:
        {
        "cap-shape": "x",
        "cap-surface": "s",
        "cap-color": "n",
        "bruises": "t",
        "odor": "p",
        "gill-attachment": "f",
        "gill-spacing": "c",
        "gill-size": "n",
        "gill-color": "k",
        "stalk-shape": "e",
        "stalk-root": "e",
        "stalk-surface-above-ring": "s",
        "stalk-surface-below-ring": "s",
        "stalk-color-above-ring": "w",
        "stalk-color-below-ring": "w",
        "veil-type": "p",
        "veil-color": "w",
        "ring-number": "o",
        "ring-type": "p",
        "spore-print-color": "k",
        "population": "s",
        "habitat": "u"
        }

5. Start the Dash Dashboard:
    python src/dashboard.py


6. Check the Prediction:  
    The API will respond with the prediction result, indicating whether the mushroom is "edible" or "poisonous" along with an explanation.

    Results:
    Accuracy: 1.0

    Classification Report:
                        precision    recall  f1-score   support

                0       1.00      1.00      1.00       843
                1       1.00      1.00      1.00       782

         accuracy                           1.00      1625
        macro avg       1.00      1.00      1.00      1625
    weighted avg        1.00      1.00      1.00      1625


## Acknowledgements

    -The Audubon Society Field Guide to North American Mushrooms for the dataset.
    -Scikit-learn for the machine learning library.      


This README file includes all the necessary information for understanding, setting up, running, and testing the project. You can adjust the content as needed to better fit your specific project details.
