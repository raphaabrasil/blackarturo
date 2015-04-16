# coding: utf-8


class Player(object):

    def __init__(self, card1, card2):
        self.cards = []
        self.cards.append(card1)
        self.cards.append(card2)
        self.points = 0

    def get_points(self):
        for card in self.cards:
            self.points += int(card)
        return self.points

    def set_cards(self, cards):
        self.cards = cards
