from card import Card
import random
import itertools

class Deck():

    def __init__(self):
        self.deck = [Card(c[0], c[1]) for c in itertools.product(range(1, 11), ['White', 'Yellow', 'Green', 'Red', 'Blue', 'Black'])]

    def shuffle(self):
        random.shuffle(self.deck)

    def display_deck(self):
        for card in self.deck:
            print(card.value, card.color)

    def draw(self, n):
        cards_drawn = []
        for i in range(n):
            cards_drawn.append(self.deck.pop())
        return cards_drawn

    def set_trump(self, card_color):
        for card in self.deck:
            if card.color == card_color:
                card.trump = True
            else:
                card.trump = False