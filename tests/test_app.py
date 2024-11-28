import pytest
from flask import Flask
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    # Envoyer une requête POST
    response = client.post('/predict', data={
        'Age': 25,
        'Account_Manager': 1,
        'Years': 2.5,
        'Num_Sites': 3
    })
    assert response.status_code == 200
    assert 'churn_prediction' in response.json

