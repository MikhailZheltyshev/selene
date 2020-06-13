from selene.api import *

from src.components.users_table import UsersTable


class UsersPage(object):
    def __init__(self):
        self.username_input = s("#inputNewUserName")
        self.password_input = s("#inputNewUserPassword")
        self.email_input = s("#newUserEmail")
        self.add_btn = s("#add_new_user_btn")
        self.table = UsersTable()

    def add_new_user(self, user):
        self.username_input.set(user.name)
        self.password_input.set(user.password)
        self.email_input.set(user.email)
        self.add_btn.click()
        return self
