from rich.table import Table

from playerreader import PlayerReader
from playerstats import PlayerStats
from playerio import PlayerIO

def main():
    io = PlayerIO()
    io.set_season()
    season = io.get_season()
    url = io.get_url()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    table_loop(io, stats, season)

def table_loop(io, stats, season):
    nationality = io.nationality()
    while nationality != "":
        table = create_table(nationality, season)
        players = get_players(stats, nationality)
        print_table(io, table, players)
        nationality = io.nationality()

def create_table(nationality, season):
    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Player", justify="left", style="cyan", no_wrap=True)
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", style="green")
    table.add_column("Assists", style="green")
    table.add_column("Points", style="green")
    table.add_column("Games", style="blue")
    table.add_column("PPG", style="blue")
    return table

def print_table(io: PlayerIO, table, players):
    for player in players:
        row = [str(player.name), str(player.team), str(player.goals),
                str(player.assists), str(player.points), str(player.games),
                str(format(player.points/player.games, ".2f"))]
        table.add_row(row)

    io.console.print(table)

def get_players(stats: PlayerStats, nationality):
    players = stats.top_scorers_by_nationality(nationality)
    return players



if __name__ == "__main__":
    main()
