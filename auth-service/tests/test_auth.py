from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/api/v1/login", json={"username": "admin", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
