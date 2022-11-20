import requests

class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        return f"{self.name:22} {self.nationality}, team {self.team}, {self.goals} + {self.assists} = {self.goals + self.assists}"


class PlayerReader:
    def __init__(self, url):
        self.url = url
    
    def get_players(self):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
            )

            players.append(player)

        return players


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality:str):

        top_scorers = []

        for player in self.reader.get_players():
            if player.nationality == nationality:
                top_scorers.append(player)
        
        return sorted(top_scorers, key=lambda player: int(player.goals + player.assists), reverse=True)
