from lib.users import Users
from lib.auth import Auth
from config import APP_URL, LOG


def test_user_permissions(login_as_admin):
    LOG.info("test_user_permissions")

    # Create new user and assign "user" role
    new_username = "rap"
    new_password = "solo"
    new_user_roles = "user"
    response = Users().create_user(
        APP_URL, 
        login_as_admin,
        new_username,
        new_password)
    
    assert response.ok
    response_data = response.json()
    new_user_id = response_data["id"]
    assert response_data["username"] == new_username
    assert response_data["roles"] == "user"

    # Login as the new user
    response = Auth().login(APP_URL, new_username, new_password)
    assert response.ok
    response_data = response.json()
    access_token = response_data["access_token"]

    # Check that the new user can retrieve its own user profile
    response = Users().get_current_user(APP_URL, access_token)
    assert response.ok
    assert response.json()["username"] == new_username
    assert response.json()["roles"] == new_user_roles

    # Check that the new user CAN NOT retrieve another user profile
    response = Users().create_user(APP_URL, access_token, "tony", "montana")
    assert not response.ok

    # Check that the new user CAN NOT retrieve another user profile
    # if the user does not have the "admin" role
    response = Users().delete_user(APP_URL, access_token, new_user_id)
    assert not response.ok

    # Delete the new user
    response = Users().delete_user(APP_URL, login_as_admin, new_user_id)
    assert response.ok
