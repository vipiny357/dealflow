from fastapi.testclient import TestClient
from app.main import app

client =TestClient(app)

def test_show_freelancers():
    # Test case 1 Checking response status code
    response = client.get("/freelancers")
    assert response.status_code == 200

    #  Test case 2 Checking len of response to acertain if only 2 results are shown when page size is 2
    response = client.get("/freelancers?page_number=1&page_size=2")
    assert response.status_code == 200
    assert len(response.json()) == 2

    # Test case 3 Checking response when page_size is negative
    response = client.get("/freelancers?page_number=1&page_size=-5")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Page number and page size must be positive integers."
    }

    # Test case 4 Checking response when page_number is negative
    response = client.get("/freelancers?page_number=-2&page_size=10")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Page number and page size must be positive integers."
    }

