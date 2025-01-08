import pytest
from config import APP_URL, LOG
from lib.comments import Comments


def test_get_all_comments(login_as_admin):
    LOG.info("test_get_all_comments")
    response = Comments().get_all_comments(APP_URL, login_as_admin)
    LOG.info(response.json())
    assert response.ok
