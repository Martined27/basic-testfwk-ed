import pytest
import requests


@pytest.fixture(scope="session")
def login_as_admin():
    response =  requests.post("http://localhost:8080/auth/login", data={"username": "admin", "password": "admin"})
    assert response.ok
    access_token = response.json()["access_token"]
    return access_token

# sometimes yield is better so below there  is more code to log out