class Player:
    def __init__(self, number):
        self.number = number
        self.score = 0

    def get_player_score(self):
        return self.score

    def won_point(self):
        self.score += 1



    def __str__(self):
        return f"Player {self.number}"