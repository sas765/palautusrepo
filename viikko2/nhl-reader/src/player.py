class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict["nationality"]
        self.assists = dict["assists"]
        self.goals = dict["goals"]
        self.team = dict["team"]
        self.games = dict["games"]
        self.id = dict["id"]
    
    def __str__(self):
        return f"""{self.name} {self.nationality}, Team: {self.team}, {self.goals} goals and {self.assists} assists in {self.games} games. id: {self.id}"""
