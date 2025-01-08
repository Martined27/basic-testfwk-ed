import pytest
from config import SESSION,APP_URL, ADMIN_USERNAME, ADMIN_PASSWORD, LOG


@pytest.fixture(scope="session")
def login_as_admin():
    LOG.info("Logging in as admin")
    payload = {"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD}
    LOG.debug(f"Payload: %s, {payload}")
    response =  SESSION.post(f"{APP_URL}/auth/login", data=payload)
    assert response.ok
    access_token = response.json()["access_token"]
    return access_token

# sometimes yield is better so below there  is more code to log out