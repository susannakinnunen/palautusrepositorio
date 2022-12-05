from player import Player

class TennisGame:
    def __init__(self):
        self.player1 = Player(1)
        self.player2 = Player(2)

    def won_point(self, player_number):
        if player_number == self.player1.number:
            self.player1.won_point()
        else:
            self.player2.won_point()

    def get_score(self):
        if self.player1.get_player_score() == self.player2.get_player_score():
            score = self.get_tie()
        elif self.player1.get_player_score()  >= 4 or self.player2.get_player_score() >= 4:
            score = self.almost_a_win_or_win()
        else:
            score = self.not_a_tie()
        return score

    def get_tie(self):
        if self.player1.get_player_score() == 0:
            score = "Love-All"
        elif self.player1.get_player_score() == 1:
            score = "Fifteen-All"
        elif self.player1.get_player_score() == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score

    def almost_a_win_or_win(self):
        minus_result = self.player1.get_player_score() - self.player2.get_player_score()
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def not_a_tie(self):
        score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1.get_player_score()
            else:
                score = score + "-"
                temp_score = self.player2.get_player_score()

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score