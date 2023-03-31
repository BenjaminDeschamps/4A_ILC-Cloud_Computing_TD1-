class Client:
    id = 0
    pseudo = ""
    password = ""

    def __init__(self, pseudo, password):
        self.id += 1
        self.pseudo = pseudo
        self.password = password

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_pseudo(self):
        return self.pseudo

    def get_password(self):
        return self.password
