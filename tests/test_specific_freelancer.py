from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)

def test_specific_freelancer():
    # Test case 1 Checking response status code for valid search
    response = client.get("/freelancers/search?first_name=Nala")
    assert response.status_code == 200
    assert len(response.json()) >= 0
    
    
    # Test case 2 Checking response status code for invalid search
    response = client.get("/freelancers/search?first_name=Nala1")
    assert response.status_code == 404
    assert response.json() == {
    "detail": "There is no user with the given query parameters. Try again."
    }

    #  Test case 3 Checking len of response to acertain if only 2 results are shown when page size is 2
    response = client.get("/freelancers/search?page_number=1&page_size=2&first_name=Nala")
    assert response.status_code == 200
    assert len(response.json()) == 2

    # Test case 4 Checking response when page_size is negative
    response = client.get("/freelancers?page_number=1&page_size=-5")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Page number and page size must be positive integers."
    }

    # Test case 5 Checking response when page_number is negative
    response = client.get("/freelancers?page_number=-2&page_size=10")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Page number and page size must be positive integers."
    }