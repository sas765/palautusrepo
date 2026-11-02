import re

class PlayerIO:
    def __init__(self, default_season="2024-25"):
        self._valid_seasons = ["2018-19", "2019-20", "2020-21", "2021-22", 
                               "2022-23", "2023-24", "2024-25", "2025-26"]
        self._valid_nationalities = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS"
                                     "SLO", "FRA", "GBR", "SVK", "DEN", "NED",
                                     "AUT", "BLR", "GER", "SUI", "NOR", "UZB",
                                     "LAT", "AUS"]
        self.season = default_season if default_season in self._valid_seasons else "2024-25"
        
    def set_season(self):
        season = input(
            "Season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]: ")
        while season not in self._valid_seasons:
            season = input(
            "Set valid season [2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]: ")
        self.season = season

    def get_url(self):
        url = f"https://studies.cs.helsinki.fi/nhlstats/{self.season}/players"
        return url
    
    def nationality(self):
        nationality = input(f"Nationality {f"{self._valid_nationalities}".replace(", ", "/")}: ").upper()
        while nationality not in self._valid_nationalities:
            if nationality == "":
                return nationality
            nationality = input(f"Set valid nationality {f"{self._valid_nationalities}".replace(", ", "/")}: ").upper()
        return nationality