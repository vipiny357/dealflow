from fastapi.testclient import TestClient
from app.main import app

def test_root():
    client = TestClient(app)

    # Test case 1 Checking response status code
    response = client.get("/")
    assert response.status_code == 200

    # Test case 2 Checking response JSON content
    expected_data = {"message": "Hello World, API Endpoint testing"}
    assert response.json() == expected_data

