import unittest

from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
            )
    
    def test_search(self):
        self.assertEqual(str(self.stats.search("Kurri")), 
                         str(Player("Kurri",   "EDM", 37, 53)))
    
    def test_team(self):
        results = [str(p) for p in self.stats.team("EDM")]
        correct = [str(Player("Semenko", "EDM", 4, 12)), 
                   str(Player("Kurri",   "EDM", 37, 53)), 
                   str(Player("Gretzky", "EDM", 35, 89))]
        
        self.assertEqual(results, correct)
    
    def test_top(self):
        results = [str(p) for p in self.stats.top(2)]
        correct = [str(Player("Gretzky", "EDM", 35, 89)),
                   str(Player("Lemieux", "PIT", 45, 54)),
                   str(Player("Yzerman", "DET", 42, 56))]
        
        self.assertEqual(results, correct)
    
    def test_sort_goals(self):
        results = [str(p) for p in self.stats.top(2, SortBy.GOALS)]
        correct = [str(Player("Lemieux", "PIT", 45, 54)),
                   str(Player("Yzerman", "DET", 42, 56)),
                   str(Player("Kurri",   "EDM", 37, 53))]
        
        self.assertEqual(results, correct)
    
    def test_sort_assists(self):
        results = [str(p) for p in self.stats.top(2, SortBy.ASSISTS)]
        correct = [str(Player("Gretzky", "EDM", 35, 89)),
                   str(Player("Yzerman", "DET", 42, 56)),
                   str(Player("Lemieux", "PIT", 45, 54))]
        
        self.assertEqual(results, correct)
    
    def test_sort_points(self):
        results = [str(p) for p in self.stats.top(2, SortBy.POINTS)]
        correct = [str(Player("Gretzky", "EDM", 35, 89)),
                   str(Player("Lemieux", "PIT", 45, 54)),
                   str(Player("Yzerman", "DET", 42, 56))]
        
        self.assertEqual(results, correct)