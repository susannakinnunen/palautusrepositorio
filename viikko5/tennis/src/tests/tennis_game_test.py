import unittest
from player import Player

from tennis_game import TennisGame

test_cases = [
    (0, 0, "Love-All"),
    (1, 1, "Fifteen-All"),
    (2, 2, "Thirty-All"),
    (3, 3, "Deuce"),

    (1, 0, "Fifteen-Love"),
    (0, 1, "Love-Fifteen"),
    (2, 0, "Thirty-Love"),
    (0, 2, "Love-Thirty"),
    (3, 0, "Forty-Love"),
    (0, 3, "Love-Forty"),
    (4, 0, "Win for player1"),
    (0, 4, "Win for player2"),

    (2, 1, "Thirty-Fifteen"),
    (1, 2, "Fifteen-Thirty"),
    (3, 1, "Forty-Fifteen"),
    (1, 3, "Fifteen-Forty"),
    (4, 1, "Win for player1"),
    (1, 4, "Win for player2"),

    (3, 2, "Forty-Thirty"),
    (2, 3, "Thirty-Forty"),
    (4, 2, "Win for player1"),
    (2, 4, "Win for player2"),

    (4, 3, "Advantage player1"),
    (3, 4, "Advantage player2"),
    (5, 4, "Advantage player1"),
    (4, 5, "Advantage player2"),
    (15, 14, "Advantage player1"),
    (14, 15, "Advantage player2"),

    (6, 4, "Win for player1"),
    (4, 6, "Win for player2"),
    (16, 14, "Win for player1"),
    (14, 16, "Win for player2"),
]


def play_game(p1_points, p2_points):
    game = TennisGame()
    for i in range(max(p1_points, p2_points)):
        if i < p1_points:
            game.won_point(1)
        if i < p2_points:
            game.won_point(2)
    return game


class TestTennis(unittest.TestCase):
    def setUp(self):
        self.player_number_1 = Player(1)
        self.player_number_2 = Player(2)

    def test_get_player_number(self):
        self.assertEqual(str(self.player_number_1), "Player 1")
        self.assertEqual(str(self.player_number_2), "Player 2")

    def test_get_player_points_in_the_beginning(self):
        self.assertEqual(self.player_number_1.get_player_score(), 0)
        self.assertEqual(self.player_number_2.get_player_score(), 0)

    def test_get_player_points_in_the_beginning(self):
        self.player_number_1.won_point()
        self.player_number_1.won_point()
        self.player_number_2.won_point()
        
        self.assertEqual(self.player_number_1.get_player_score(), 2)
        self.assertEqual(self.player_number_2.get_player_score(), 1)

    def test_score_love_all(self):
        test_case = [0, 0, "Love-All"]
        game = play_game(test_case[0], test_case[1])

        self.assertEqual(test_case[2],game.get_score())

    def test_score_fifteen_all(self):
        test_case = [1, 1, "Fifteen-All"]
        game = play_game(test_case[0], test_case[1])

        self.assertEqual(test_case[2],game.get_score())

    def test_advantage_player_one(self):
        test_case = [4, 3, "Advantage player1"]
        game = play_game(test_case[0], test_case[1])

        self.assertEqual(test_case[2],game.get_score())
    
    def test_fifteen_love(self):
        test_case = [1, 0, "Fifteen-Love"]
        game = play_game(test_case[0], test_case[1])

        self.assertEqual(test_case[2],game.get_score())

    def test_win_for_player2(self):
        test_case = [0, 4, "Win for player2"]
        game = play_game(test_case[0], test_case[1])

        self.assertEqual(test_case[2],game.get_score())

    def test_thirty_fifteen(self):
        test_case = [2, 1, "Thirty-Fifteen"]
        game = play_game(test_case[0], test_case[1])

        self.assertEqual(test_case[2],game.get_score())
