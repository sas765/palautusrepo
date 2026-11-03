from rich.console import Console

class PlayerIO:
    def __init__(self, default_season="2024-25"):
        self.console = Console()
        self._valid_seasons = ["2018-19", "2019-20", "2020-21", "2021-22",
                               "2022-23", "2023-24", "2024-25", "2025-26"]
        self._valid_nationalities = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS",
                                     "SLO", "FRA", "GBR", "SVK", "DEN", "NED",
                                     "AUT", "BLR", "GER", "SUI", "NOR", "UZB",
                                     "LAT", "AUS"]
        self.season = default_season if default_season in self._valid_seasons else "2024-25"

    def set_season(self):
        seasons_print = f"{self._valid_seasons}".replace(", ", "/").replace("'", "")
        season = self.console.input(f"Season [magenta]{seasons_print}: ")
        while season not in self._valid_seasons:
            season = self.console.input(
            f"Set valid season [magenta]{seasons_print}: ")
        self.season = season

    def get_season(self):
        return self.season

    def get_url(self):
        url = f"https://studies.cs.helsinki.fi/nhlstats/{self.season}/players"
        return url

    def nationality(self):
        nationalities_print = f"{self._valid_nationalities}".replace(", ", "/").replace("'", "")
        nationality = self.console.input(
            f"Nationality [magenta]{nationalities_print}: ").upper()
        while nationality not in self._valid_nationalities:
            if nationality == "":
                return nationality
            nationality = self.console.input(
                f"Set valid nationality [magenta]{nationalities_print}: ").upper()
        return nationality
