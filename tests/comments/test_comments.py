
from config import APP_URL, LOG
from lib.comments import Comments


def test_get_all_comments(login_as_admin):
    LOG.info("test_get_all_comments")
    response = Comments().get_all_comments(APP_URL, login_as_admin)
    LOG.info(response.json())
    assert response.ok


def test_cud_comment(login_as_admin):
    text = "first post"
    likes = 5
    updateText = "updated to second post"
    LOG.info("test_cud_comment")
    response = Comments().create_comment(APP_URL, login_as_admin, text)
    assert response.ok
    response_data = response.json()
    comment_id = response_data["id"]
    LOG.debug(response_data)
    assert response_data["comment_text"] == text

    response = Comments().update_comment(
        APP_URL, login_as_admin, comment_id,       
        message= updateText,
        likes= likes
        )
    assert response.ok
    response_data = response.json()
    LOG.debug(response_data)
    assert response_data["comment_text"] == updateText
    assert response_data["likes"] == likes

    response = Comments().delete_comment(APP_URL, login_as_admin, comment_id)
    assert response.ok
    response_data = response.json()
    LOG.debug(response_data)
    assert response_data["detail"] == f"Deleted comment {comment_id}"
