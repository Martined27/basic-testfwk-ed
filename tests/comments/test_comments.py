import pytest
import requests


def test_get_all_comments(login_as_admin):

    # Auth
    request_header= {
        "Authorization": "Bearer " + str(login_as_admin), 
        "Accept": "application/json"
    }

    response = requests.get("http://localhost:8080/comments", headers=request_header)
    assert response.ok


# def test_create_comment():
#     # Auth
#     payload = {"username": "admin", "password": "admin"}
#     response = requests.post("http://localhost:8080/auth/login", data=payload)
#     assert response.ok
#     # Create Comment
#     access_token = response.json()["access_token"]
#     request_header= {
#         "Authorization": "Bearer " + access_token,
#         "Accept": "application/json"
#     }
#     payload = {"body": "test comment"}
#     response = requests.post("http://localhost:8080/comments", data=payload, headers=request_header)
#     assert response.ok