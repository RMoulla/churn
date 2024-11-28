from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Charger le modèle
model = joblib.load('data/churn_model_clean.pkl')

# Initialiser l'application Flask
app = Flask(__name__)

# Route principale pour afficher l'interface utilisateur
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Route pour gérer les prédictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données du formulaire
        age = float(request.form['Age'])
        account_manager = int(request.form['Account_Manager'])
        years = float(request.form['Years'])
        num_sites = int(request.form['Num_Sites'])

        # Créer un tableau numpy pour les données
        features = np.array([[age, account_manager, years, num_sites]])

        # Effectuer la prédiction
        prediction = model.predict(features)
        result = int(prediction[0])

        # Retourner la réponse sous forme de JSON
        return jsonify({'churn_prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})

# Lancer l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012, debug=True)
