class Client:
    _id = 0
    _name = ""
    _pseudo = ""

    def __init__(name, pseudo):
        self._id += 1
        self._name = name
        self._pseudo = pseudo
