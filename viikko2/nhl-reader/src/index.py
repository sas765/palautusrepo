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
    search_type = io.search_type()
    while search_type != "":
        search_value = get_search_value(io, stats, search_type)
        players = get_players(io, stats, search_type, search_value)
        table = create_table(search_type, search_value, season)
        print_table(io, table, players)
        search_type = io.search_type()

def get_search_value(io, stats, search_type):
    if search_type == "n":
        return io.nationality(stats.nationalities)
    return io.team(stats.teams)

def create_table(search_type, search_value, season):
    filter_name = "nationality" if search_type == "n" else "team"
    table = Table(title=f"Season {season} players by {filter_name}: {search_value}")
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
        row = [str(player.name), str(player.team), str(player.goals), str(player.assists),
            str(player.points), str(player.games), str(format(player.points/player.games, ".2f"))]
        table.add_row(*row)

    io.console.print(table)

def get_players(io, stats: PlayerStats, search_type, search_value):
    if search_type == "n":
        return stats.top_scorers_by_nationality(search_value)
    if search_type == "t":
        return stats.top_scorers_by_team(search_value)
    how_many = io.how_many()
    return stats.top_goal_scorers(how_many)


if __name__ == "__main__":
    main()
