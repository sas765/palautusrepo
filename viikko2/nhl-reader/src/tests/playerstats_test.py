import unittest

from player import Player
from playerstats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Player A",
                "nationality": "FIN",
                "assists": 30,
                "goals": 20,
                "team": "BOS, NYR",
                "games": 50,
            }),
            Player({
                "name": "Player B",
                "nationality": "CAN",
                "assists": 11,
                "goals": 40,
                "team": "BOS",
                "games": 60,
            }),
            Player({
                "name": "Player C",
                "nationality": "FIN",
                "assists": 25,
                "goals": 15,
                "team": "NYR",
                "games": 55,
            }),
            Player({
                "name": "Player D",
                "nationality": "SWE",
                "assists": 20,
                "goals": 25,
                "team": "TOR",
                "games": 58,
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_teams_and_nationalities_are_collected(self):
        self.assertEqual(set(self.stats.teams), {"BOS", "NYR", "TOR"})
        self.assertEqual(set(self.stats.nationalities), {"FIN", "CAN", "SWE"})

    def test_top_scorers_by_nationality(self):
        results = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player.name for player in results], ["Player A", "Player C"])

    def test_top_scorers_by_team(self):
        results = self.stats.top_scorers_by_team("BOS")

        self.assertEqual([player.name for player in results], ["Player B", "Player A"])

    def test_top_goal_scorers_returns_requested_number(self):
        results = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in results], ["Player B", "Player D"])


if __name__ == "__main__":
    unittest.main()
