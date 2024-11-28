from flask import Flask, request, jsonify
import joblib
import numpy as np

# Charger le modèle de régression logistique sauvegardé
model = joblib.load('data/churn_model_clean.pkl')

# Initialiser l'application Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Application is running", 200
# Définir la route principale pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    # Utiliser request.form pour extraire les données du formulaire HTML
    age = float(request.form['Age'])
    account_manager = int(request.form['Account_Manager'])
    years = float(request.form['Years'])
    num_sites = int(request.form['Num_Sites'])

    # Créer un tableau numpy pour les données de prédiction
    features = np.array([[age, account_manager, years, num_sites]])

    # Effectuer la prédiction
    prediction = model.predict(features)
    print(prediction)

    # Convertir la prédiction en un format compréhensible
    result = int(prediction[0])

    return jsonify({'churn_prediction': result})  # Le return doit être ici aussi dans une fonction

# Fonction pour lancer le serveur Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5012, debug=True)
