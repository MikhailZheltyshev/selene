from selene.api import *

from src.pages.users_page import UsersPage


class MainPage(object):
    def __init__(self):
        self.logo = s("a.navbar-brand")

    def go_to_users_tab(self):
        s("#users_link").click()
        return UsersPage()
