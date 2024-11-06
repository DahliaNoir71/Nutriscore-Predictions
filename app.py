import subprocess
import pandas as pd
from flask import Flask, render_template, jsonify, request
from config import Config
from services.loaders.loaders import load_model, load_scaler
from services.testing.test_model import make_predictions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/run_clean_csv', methods=['POST'])
def run_clean_csv():
    # Exécuter le script clean_csv et capturer les sorties
    process = subprocess.Popen(
        ['python', 'scripts/csv/clean_csv.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Récupérer la sortie standard et l'erreur standard
    stdout, stderr = process.communicate()

    # Retourner la sortie au format JSON
    return jsonify({'output': stdout, 'error': stderr})

@app.route('/api/v1/predict', methods=['GET','POST'])
def predict():
    # Récupérer les données du JSON
    data = request.get_json()
    # Transformer les données en dictinnaire
    # Transformer le JSON en dictionnaire
    data_dict = dict(data)
    # transformer le dictionnaire en DataFrame
    df_data = pd.DataFrame([data_dict])

    model = load_model(Config.DUMP_MODEL_NAME)
    scaler = load_scaler(Config.DUMP_SCALER_NAME)
    df_predict = make_predictions(model, scaler, df_data)
    # Transformer le DataFrame en JSON
    json_predict = df_predict.to_json(orient='records')

    # Retourner le score nutriscore en JSON
    return jsonify({'prediction': json_predict})


if __name__ == "__main__":
    app.run()