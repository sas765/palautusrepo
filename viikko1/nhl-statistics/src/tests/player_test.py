import unittest

from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Joe", "MAMA", 6, 7)

    def test_constructor_name(self):
        self.assertEqual(self.player.name, "Joe")
    
    def test_constructor_team(self):
        self.assertEqual(self.player.team, "MAMA")

    def test_constructor_goals(self):
        self.assertEqual(self.player.goals, 6)
    
    def test_constructor_assists(self):
        self.assertEqual(self.player.assists, 7)
    
    def test_property_points(self):
        self.assertEqual(self.player.points, 13)
    
    def test_str(self):
        self.assertEqual(str(self.player), "Joe MAMA 6 + 7 = 13")