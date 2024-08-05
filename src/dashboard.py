import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import requests

# Load the data
data = pd.read_csv('data/mushrooms.csv')

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Generate insights
class_distribution = data['class'].value_counts().reset_index()
class_distribution.columns = ['Class', 'Count']

summary_stats = data.describe(include='all')

features = ['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor']
feature_counts = []
for feature in features:
    feature_counts.append(data[feature].value_counts().reset_index())
    feature_counts[-1].columns = [feature, 'count']

# Layout of the dashboard
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Mushroom Classification Dashboard"), className="mb-2")
    ]),
    dbc.Row([
        dbc.Col(html.H3("Summary Statistics"), className="mb-2")
    ]),
    dbc.Row([
        dbc.Col(html.Div([
            html.H5("Summary Statistics"),
            html.Pre(summary_stats.to_string())
        ]), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.H3("Make a Prediction"), className="mb-2")
    ]),
    dbc.Row([
        dbc.Col(dbc.Input(id='input-data', placeholder='Enter feature values as JSON', type='text'), width=9),
        dbc.Col(dbc.Button('Predict', id='predict-button', color='primary'), width=3)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='prediction-result', style={'font-weight': 'bold', 'font-size': '24px'}), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='prediction-explanation'), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.H3("Mushroom Class Distribution and Counts"), className="mb-2")
    ], id='class-distribution-row', style={'display': 'none'}),
    dbc.Row([
        dbc.Col(dcc.Graph(id='mushroom-class-distribution'), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.H4("Count of Poisonous Mushrooms"), width=6),
        dbc.Col(html.H4("Count of Edible Mushrooms"), width=6)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='poisonous-mushrooms-count'), width=6),
        dbc.Col(html.Div(id='edible-mushrooms-count'), width=6)
    ]),
    dbc.Row([
        dbc.Col(html.H3("Lists of Mushrooms"), className="mb-2")
    ]),
    dbc.Row([
        dbc.Col(html.H5("Here is list according to it's Row Numbers"), className="mb-2")
    ]),
    dbc.Row([
        dbc.Col(html.H4("Poisonous Mushrooms"), width=6),
        dbc.Col(html.H4("Edible Mushrooms"), width=6)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='poisonous-mushrooms'), width=6),
        dbc.Col(html.Div(id='edible-mushrooms'), width=6)
    ]),
])

# Add a callback for predictions
@app.callback(
    [dash.dependencies.Output('prediction-result', 'children'),
     dash.dependencies.Output('prediction-explanation', 'children'),
     dash.dependencies.Output('class-distribution-row', 'style')],
    [dash.dependencies.Input('predict-button', 'n_clicks')],
    [dash.dependencies.State('input-data', 'value')]
)
def update_prediction(n_clicks, input_data):
    if n_clicks is None:
        return "", "", {'display': 'none'}

    # Assume `input_data` is a JSON string containing the input features
    url = 'http://127.0.0.1:5000/predict'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=input_data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        prediction = result['prediction']
        explanation = result.get('explanation', 'No explanation provided.')

        prediction_text = f"The mushroom is {prediction}."
        return prediction_text, explanation, {'display': 'block'}
    else:
        return "Error in prediction.", "", {'display': 'none'}

# Add a callback to fetch and display the lists and counts
@app.callback(
    [dash.dependencies.Output('poisonous-mushrooms', 'children'),
     dash.dependencies.Output('edible-mushrooms', 'children'),
     dash.dependencies.Output('poisonous-mushrooms-count', 'children'),
     dash.dependencies.Output('edible-mushrooms-count', 'children'),
     dash.dependencies.Output('mushroom-class-distribution', 'figure')],
    [dash.dependencies.Input('predict-button', 'n_clicks')]
)
def update_mushroom_lists(n_clicks):
    if n_clicks is None:
        return "", "", "", "", {}

    url = 'http://127.0.0.1:5000/get_mushrooms'
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        poisonous_mushrooms = result['poisonous_mushrooms']
        edible_mushrooms = result['edible_mushrooms']

        poisonous_list = html.Ul([html.Li(mushroom) for mushroom in poisonous_mushrooms])
        edible_list = html.Ul([html.Li(mushroom) for mushroom in edible_mushrooms])

        poisonous_count = f"Count: {len(poisonous_mushrooms)}"
        edible_count = f"Count: {len(edible_mushrooms)}"

        # Create the class distribution pie chart
        fig = px.pie(
            values=[len(poisonous_mushrooms), len(edible_mushrooms)],
            names=['Poisonous', 'Edible'],
            title='Mushroom Class Distribution'
        )

        return poisonous_list, edible_list, poisonous_count, edible_count, fig
    else:
        return "Error in fetching mushroom lists.", "Error in fetching mushroom lists.", "", "", {}

if __name__ == '__main__':
    app.run_server(debug=True)
