# coding: utf-8

from Player import Player


class BlackArturo(object):

    def __init__(self):
        self._player1 = Player('14', '7')
        self._player2 = Player('2', '9')

    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player2

    def start(self):
        pass

    def get_players(self):
        return 2

    def do_we_have_an_winner(self):
        if self._player1.get_points() == 21 or \
           self._player2.get_points() == 21:
            return True
        return False
