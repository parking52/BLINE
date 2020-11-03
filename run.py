from deck import Deck
from board import Board

deck = Deck()
deck.shuffle()

player1_hand = deck.draw(7)
player2_hand = deck.draw(7)

board = Board()

print(player1_hand)
print(board)
#board.insert(0, 5, Card(4,'red'))
#print(board)

for i in range(9*3):

    board.insert(0, i%9, player1_hand.pop())
    if len(deck.deck) > 0:
        player1_hand.append(deck.draw(1)[0])

    board.insert(1, i%9, player2_hand.pop())
    if len(deck.deck) > 0:
        player2_hand.append(deck.draw(1)[0])

print(board)
print(board.decide_winner())



