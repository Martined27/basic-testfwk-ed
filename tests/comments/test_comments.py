import pytest
import requests
from lib.utils import build_request_headers


def test_get_all_comments(login_as_admin):

    # Auth
    request_header= build_request_headers(login_as_admin)
    response = requests.get("http://localhost:8080/comments", headers=request_header)
    assert response.ok


