from selene.api import *


class UsersTable(object):
    def __init__(self):
        self.table = s("#users_table")

    def user_names(self):
        return self.table.find("tbody tr td:nth-child(2)")
