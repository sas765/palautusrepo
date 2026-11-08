from playerreader import PlayerReader, Player

def points(player: Player):
    return player.points

def get_teams(players):
    teams = set()
    t = []
    for p in players:
        t = p.team.split(", ")
        for team in t:
            teams.add(team)

    return list(teams)

def get_nationalities(players):
    nationalities = set()
    for p in players:
        nationalities.add(p.nationality)
    
    return list(nationalities)

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.get_players()
        self.teams = get_teams(self.players)
        self.nationalities = get_nationalities(self.players)

    def top_scorers_by_nationality(self, nationality: str):
        players = [p for p in self.players if p.nationality == nationality]
        results = sorted(players, key=points, reverse=True)

        return results

    def top_scorers_by_team(self, team: str):
        """Palauttaa joukkueen pelaajat pisteiden mukaan laskevassa järjestyksessä."""
        players = [p for p in self.players if team in p.team]
        results = sorted(players, key=points, reverse=True)

        return results

    def top_goal_scorers(self, how_many):
        """Palauttaa enintään how_many eniten maaleja tehnyttä pelaajaa."""
        results = sorted(self.players, key=lambda player: player.goals, reverse=True)[:how_many]

        return results
