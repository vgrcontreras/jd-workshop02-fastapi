import pytest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_ola_mundo_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_ola_mundo_conteudo():
    response = client.get("/")
    assert response.json() == {"Olá": "Mundo"}