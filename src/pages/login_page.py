from selene.api import *

from src.pages.main_page import MainPage


class LoginPage(object):
    def __init__(self):
        self.username_input = s("#inputEmail3")
        self.password_input = s("#inputPassword3")
        self.login_btn = s("button[type='submit']")

    def open(self):
        browser.open_url("http://localhost:8086/")
        return self

    def login_as(self, user):
        self.username_input.set(user.name)
        self.password_input.set(user.password)
        self.login_btn.click()
        return MainPage()
