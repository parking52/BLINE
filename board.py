from card import Card
import random
import itertools
import numpy

class Board():

    def __init__(self):
        self.board = [
                        [
                            [],[],[],[],[],[],[],[],[]
                        ],
                        [
                            [],[],[],[],[],[],[],[],[]
                        ]
                        ]

    def insert(self, player_id, row, card):
            self.board[player_id][row].append(card)


    def __str__(self):
        return str(self.board)

    def decide_winner(self):
        results = [self.decide_winner_on_column(column) for column in range(9)]
        return results

    def check_same_color(self, formation):
        return int(len(set([card.color for card in formation])) == 1)

    def check_triple(self, formation):
        return int(len(set([card.value for card in formation])) == 1)

    def check_serie(self, formation):
        values = [card.value for card in formation]
        return int(set([value - min(values) for value in values]) == set([0,1,2]))

    def compute_value(self, formation):
        formation_sum = sum([card.value for card in formation])
        return f"{formation_sum:02}"

    def get_formation_code(self, formation):
        formation_same_color = self.check_same_color(formation)
        formation_serie = self.check_serie(formation)
        formation_serie_same_color = formation_same_color & formation_serie
        formation_triple = self.check_triple(formation)
        formation_value = self.compute_value(formation)
        formation_code = "{}{}{}{}{}".format(formation_serie_same_color, formation_triple, formation_same_color, formation_serie, formation_value)
        return formation_code


    def decide_winner_on_column(self, column):

        formation_0 = self.board[0][column]
        formation_0_code = self.get_formation_code(formation_0)

        formation_1 = self.board[1][column]
        formation_1_code = self.get_formation_code(formation_1)

        return formation_1_code > formation_0_code