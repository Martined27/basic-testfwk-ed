import pytest
from config import APP_URL
from lib.comments import Comments



def test_get_all_comments(login_as_admin):
    response = Comments().get_all_comments(APP_URL, login_as_admin)
    assert response.ok
