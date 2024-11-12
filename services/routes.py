import pandas as pd
from flask import render_template, jsonify, request
from services.loaders.loaders import load_model, load_scaler
from services.predictions import predictions
from config import Config

def init_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        # Afficher le formulaire
        return render_template('home.html')

    @app.route('/api/predict', methods=['POST'])
    def predict():
        if request.method == 'POST':
            # Récupérer les données du formulaire
            data = request.form
            # Transformer les données en dictionnaire
            data_dict = dict(data)
            # Transformer le dictionnaire en DataFrame
            df_data = pd.DataFrame([data_dict])

            model = load_model(Config.DUMP_MODEL_NAME)
            scaler = load_scaler(Config.DUMP_SCALER_NAME)
            y_prediction, y_prediction_prob = predictions(model, scaler, df_data)

            # Retourner le score nutriscore en JSON
            return jsonify({'prediction': y_prediction[0]})

