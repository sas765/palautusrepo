from rich.console import Console

class PlayerIO:
    def __init__(self, default_season="2024-25"):
        self.console = Console()
        self._valid_seasons = ["2018-19", "2019-20", "2020-21", "2021-22",
                               "2022-23", "2023-24", "2024-25", "2025-26"]
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

    def search_type(self):
        search_type = self.console.input(
"Search for most goals (g) or top points by nationality (n) or by team (t), leave empty to quit: "
        ).lower()
        while search_type not in ("g", "n", "t", ""):
            search_type = self.console.input(
    "Choose most goals (g) or top points by nationality (n) or by team (t), leave empty to quit: "
            ).lower()
        return search_type

    def nationality(self, nationalities):
        nationalities_print = f"{nationalities}".replace(", ", "/").replace("'", "")
        nationality = self.console.input(
            f"Nationality [magenta]{nationalities_print}: ").upper()
        while nationality not in nationalities:
            nationality = self.console.input(
            f"Enter valid nationality [magenta]{nationalities_print}: ").upper()
        return nationality

    def team(self, teams):
        teams_print = f"{teams}".replace(", ", "/").replace("'", "")
        team = self.console.input(
            f"Team [magenta]{teams_print}: ").upper()
        while team == "":
            team = self.console.input(
                f"Enter valid team [magenta]{teams_print}: ").upper()
        return team

    def how_many(self):
        limit = input("How many of the top scorers would you like to see: ")
        while isinstance(limit, str):
            try:
                limit = int(limit)
            except ValueError:
                limit = input("How many of the top scorers would you like to see: ")

        return limit
