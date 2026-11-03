class Player:
    def __init__(self, data):
        self.name = data['name']
        self.nationality = data["nationality"]
        self.assists = data["assists"]
        self.goals = data["goals"]
        self.team = data["team"]
        self.games = data["games"]
        self.points = self.goals + self.assists

    def __str__(self):
        return f"""{self.name:20}{self.team:15}{self.goals:3} +{self.assists:3} = {self.points}"""
