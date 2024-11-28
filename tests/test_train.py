import os
import joblib

def test_model_training():
    # Vérifie si le modèle est correctement généré
    os.system("python train.py")
    assert os.path.exists("data/churn_model_clean.pkl")
    model = joblib.load("data/churn_model_clean.pkl")
    assert model is not None
