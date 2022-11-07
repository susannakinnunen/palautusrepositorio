
def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists




class Statistics:
    def __init__(self,player_reader):
        self.reader = player_reader

        self._players = self.reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by):
        if sort_by == 1:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )
            result = []
            i = 0
            while i <= how_many:
                result.append(sorted_players[i])
                i += 1

            return result
        
        if sort_by == 2:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_goals
        )
            result = []
            i = 0
            while i <= how_many:
                result.append(sorted_players[i])
                i += 1

            return result

        if sort_by == 3:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_assists
        )
            result = []
            i = 0
            while i <= how_many:
                result.append(sorted_players[i])
                i += 1

            return result
        
        else:
            return None