class Player:
    def __init__(self, number, score = 0):
        self.number = number
        self.score = score

    def get_player_score(self):
        return self.score

    def won_point(self):
        self.score += 1

    def __str__(self):
        return f"Player {self.number}"