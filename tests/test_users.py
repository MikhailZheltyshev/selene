from selene.support.conditions import have

from src.domain.user import User
from src.pages.login_page import LoginPage


def test_can_add_new_user():
    (LoginPage()
     .open()
     .login_as(User(name="admin", password="admin"))
     .go_to_users_tab()
     .add_new_user(User(name="Mike", password="12345", email="test@example.com"))
     .table
     .user_names().should(have.text("Mike")))
