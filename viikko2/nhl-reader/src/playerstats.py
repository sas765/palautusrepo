from playerreader import PlayerReader, Player

def points(player: Player):
    return player.points

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality: str):
        results = sorted([p for p in self.players if p.nationality == nationality],
                         key=points, reverse=True)

        return results
