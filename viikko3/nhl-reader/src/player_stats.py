

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def sort_by_points(self,player):
        return player.goals + player.assists 


    def top_scorers_by_nationality(self, nationality):
        nationality_list = []
        player_list = self.reader.get_players()
        for player in player_list:
            if player.nationality == nationality:
                nationality_list.append(player)

        nationality_list.sort(key=self.sort_by_points, reverse=True)

        return nationality_list

