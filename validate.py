import pandas as pd
from sklearn.metrics import recall_score, precision_score, f1_score
import joblib

# Charger les données de validation
data = pd.read_csv('data/test_data.csv')
X_val = data[['Age', 'Account_Manager', 'Years', 'Num_Sites']]
y_val = data['Churn']

# Charger le modèle
model = joblib.load('data/churn_model_clean.pkl')

# Prédire sur les données de validation
predictions = model.predict(X_val)

# Calculer les métriques
recall = recall_score(y_val, predictions)
print(f"Recall: {recall:.2f}")
precision = precision_score(y_val, predictions)
print(f"Precision: {precision:.2f}")
f1_score = f1_score(y_val, predictions)
print(f"F1_Score: {f1_score:.2f}")

# Définir un seuil de performance
if recall < 0.6:
    raise ValueError("Le modèle ne satisfait pas le seuil de performance requis.")
