import pandas as pd
from sklearn.metrics import recall_score, precision_score, f1_score
import joblib

# Charger les données de validation
data = pd.read_csv('data/test_data.csv')
X_val = data[['Age', 'Account_Manager', 'Years', 'Num_Sites']]
y_val = data['Churn']

# Charger le modèle
model = joblib.load('models/churn_model.pkl')

# Prédire sur les données de validation
predictions = model.predict(X_val)

# Calculer les métriques
accuracy = accuracy_score(y_val, predictions)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_val, predictions))

# Définir un seuil de performance
if accuracy < 0.8:
    raise ValueError("Le modèle ne satisfait pas le seuil de performance requis.")
