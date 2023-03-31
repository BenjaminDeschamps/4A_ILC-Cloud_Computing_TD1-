import client


class Tweet:
    id = 0
    user = 0
    subject = ""
    text = ""
    date = ""

    def __init__(self, user, subject, text):
        self.id += 1
        self.user = user
        self.subject = subject
        self.text = text

    def get_user(self):
        return self._user

    def print_tweet(self):
        print(self.text)
