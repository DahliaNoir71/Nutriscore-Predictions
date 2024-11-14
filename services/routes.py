import pandas as pd
from flask import render_template, jsonify, request
from services.loaders.loaders import load_model, load_scaler
from services.predictions import predictions
from services.database.models.nutriscore_prediction import NutriScorePrediction
from config import Config
from app import db

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

            # Créer une nouvelle instance de NutriScorePrediction
            prediction_record = NutriScorePrediction(
                energy_kcal_100g=df_data['energy_kcal_100g'].values[0],
                fat_100g=df_data['fat_100g'].values[0],
                saturated_fat_100g=df_data['saturated_fat_100g'].values[0],
                sugars_100g=df_data['sugars_100g'].values[0],
                fiber_100g=df_data['fiber_100g'].values[0],
                proteins_100g=df_data['proteins_100g'].values[0],
                salt_100g=df_data['salt_100g'].values[0],
                fruits_vegetables_nuts_estimate_from_ingredients_100g=df_data['fruits_vegetables_nuts_estimate_from_ingredients_100g'].values[0],
                predicted_score=y_prediction[0]
            )

            # Ajouter la nouvelle instance à la base de données
            db.session.add(prediction_record)
            db.session.commit()

            # Retourner le score nutriscore en JSON
            return jsonify({'prediction': y_prediction[0]})