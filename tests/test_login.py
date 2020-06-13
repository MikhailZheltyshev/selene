from selene.support.conditions.have import text

from src.domain.user import User
from src.pages.login_page import LoginPage


def test_admin_can_login():
    (LoginPage()
     .open()
     .login_as(User(name="admin", password="admin"))
     .logo.should_have(text("Video service")))
