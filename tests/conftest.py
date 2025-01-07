import pytest
from config import SESSION,APP_URL, ADMIN_USERNAME, ADMIN_PASSWORD


@pytest.fixture(scope="session")
def login_as_admin():
    response =  SESSION.post(f"{APP_URL}/auth/login", data={"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD})
    assert response.ok
    access_token = response.json()["access_token"]
    return access_token

# sometimes yield is better so below there  is more code to log out