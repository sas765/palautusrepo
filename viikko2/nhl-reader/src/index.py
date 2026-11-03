from player import Player
from playerreader import PlayerReader
from playerstats import PlayerStats
from playerio import PlayerIO

from rich.table import Table

def main():
    io = PlayerIO()
    io.set_season()
    season = io.get_season()
    url = io.get_url()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality = io.nationality()
    while nationality != "":
        table = Table(title=f"Season {season} players from {nationality}")
        table.add_column("Player", justify="left", style="cyan", no_wrap=True)
        table.add_column("Teams", style="magenta")
        table.add_column("Goals", style="green")
        table.add_column("Assists", style="green")
        table.add_column("Points", style="green")
        table.add_column("Games", style="blue")
        table.add_column("PPG", style="blue")

        players = stats.top_scorers_by_nationality(nationality)
        for player in players:
            table.add_row(str(player.name), str(player.team), str(player.goals),
                        str(player.assists), str(player.points), str(player.games), 
                        str(format(player.points/player.games, ".2f")))
        
        io.console.print(table)
        nationality = io.nationality()



if __name__ == "__main__":
    main()
