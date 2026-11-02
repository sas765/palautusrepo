from player import Player
from playerreader import PlayerReader
from playerstats import PlayerStats
from playerio import PlayerIO

def main():
    io = PlayerIO()
    io.set_season()
    url = io.get_url()
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality = io.nationality()
    while nationality != "":
        players = stats.top_scorers_by_nationality(nationality)
        for player in players:
            print(player)
        nationality = io.nationality()



if __name__ == "__main__":
    main()
