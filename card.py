
class Card():

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __repr__(self):
        return str(self.value) + self.color

    def __str__(self):
        return str(self.value) + self.color
