import unittest
from statistics import Statistics
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        player_reader_stub = PlayerReaderStub()
        self.statistics = Statistics(
            player_reader_stub
        )

    def test_statistics_returns_correct_player(self):
        player = self.statistics.search("Semenko")
        tulostus = str(player)
        self.assertEqual(tulostus,"Semenko EDM 4 + 12 = 16")

    def test_statistics_ei_toimi_virheellisella_pelaaja_nimella(self):
        player = self.statistics.search("Ronaldo")
        tulostus = str(player)
        self.assertEqual(tulostus, "None")
    
    def test_statistics_returns_correct_team(self):
        team = self.statistics.team("EDM")
        pelaajat = []
        for player in team:
            pelaajat.append(str(player.name))
        self.assertEqual(pelaajat,["Semenko", "Kurri", "Gretzky"])

    def test_statistics_returns_top_players_points(self):
        top_players = self.statistics.top(2,1)
        pelaajat = []
        for player in top_players:
            pelaajat.append(str(player.name))
        self.assertEqual(pelaajat,["Gretzky", "Lemieux", "Yzerman"])

    def test_statistics_returns_top_players_goals(self):
        top_players = self.statistics.top(1,2)
        pelaajat = []
        for player in top_players:
            pelaajat.append(str(player.name))
        self.assertEqual(pelaajat,["Lemieux", "Yzerman"])

    def test_statistics_returns_top_players_assists(self):
        top_players = self.statistics.top(1,3)
        pelaajat = []
        for player in top_players:
            pelaajat.append(str(player.name))
        self.assertEqual(pelaajat,["Gretzky", "Yzerman"])

    def test_statistics_returns_none_with_false_sort_by(self):
            top_players = self.statistics.top(1,0)
            self.assertEqual(top_players, None)