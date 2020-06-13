class User(object):
    def __init__(self, name, password, email=None):
        self.name = name
        self.password = password
        self.email = email
