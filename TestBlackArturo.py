# coding: utf-8

import unittest
from BlackArturo import BlackArturo


class TestBlackArturo(unittest.TestCase):

    def setUp(self):
        self.jogo = BlackArturo()
        self.jogo.start()

    def test_get_players(self):
        self.assertEqual(2, self.jogo.get_players())


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.jogo = BlackArturo()
        self.jogo.start()

    def test_player_points(self):
        self.assertEqual(21, self.jogo.player1.get_points())

    def test_player1_wins(self):
        self.jogo.player1.set_cards(['7', '14'])
        self.jogo.player2.set_cards(['1', '2'])
        self.assertTrue(self.jogo.do_we_have_an_winner())

    def test_player2_wins(self):
        self.jogo.player1.set_cards(['7', '1'])
        self.jogo.player2.set_cards(['7', '14'])
        self.assertTrue(self.jogo.do_we_have_an_winner())

    def test_do_not_have_winner(self):
        self.jogo.player1.set_cards(['7', '1'])
        self.jogo.player2.set_cards(['6', '2'])
        self.assertFalse(self.jogo.do_we_have_an_winner())


class TestPlayerCards(unittest.TestCase):
    def setUp(self):
        self.jogo = BlackArturo()
        self.jogo.start()

    def test_player_cards(self):
        self.assertEqual(['14', '7'], self.jogo.player1.cards)
        self.assertEqual(['2', '9'], self.jogo.player2.cards)

    def test_get_points(self):
        self.assertEqual(21, self.jogo.player1.get_points())
        self.assertEqual(11, self.jogo.player2.get_points())


if __name__ == '__main__':
    unittest.main()
