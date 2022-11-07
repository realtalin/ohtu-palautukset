import unittest
from statistics import Statistics
from player import Player
from sortby import SortBy

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
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_nimi_listassa(self):
        self.assertEqual(self.statistics.search("Kurri"), self.statistics._players[2])

    def test_search_nimi_ei_listassa(self):
        self.assertEqual(self.statistics.search("Sampo"), None)

    def test_team_pelaajat_joukkueessa(self):
        self.assertEqual(self.statistics.team("EDM"), [self.statistics._players[0], self.statistics._players[2], self.statistics._players[4]])

    def test_top_yksi_ilman_jarjestysta(self):
        self.assertEqual(self.statistics.top(0), [self.statistics._players[4]])

    def test_top_yksi_pisteissa(self):
        self.assertEqual(self.statistics.top(0, SortBy.POINTS), [self.statistics._players[4]])

    def test_top_yksi_maaleissa(self):
        self.assertEqual(self.statistics.top(0, SortBy.GOALS), [self.statistics._players[1]])

    def test_top_yksi_syotoissa(self):
        self.assertEqual(self.statistics.top(0, SortBy.ASSISTS), [self.statistics._players[4]])






