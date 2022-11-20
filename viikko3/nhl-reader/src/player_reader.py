from player import Player
import requests

class PlayerReader:
    def __init__(self,osoite):
        self.osoite = osoite
        self.response = requests.get(osoite).json()

    
    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games'])
            
            players.append(player) 
        
        return players
    