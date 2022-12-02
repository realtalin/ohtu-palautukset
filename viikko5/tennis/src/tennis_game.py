class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.game_status_deuce():
            return "Deuce"

        elif self.game_status_drawn():
            return self.translate_score(self.player1_score) + "-All"

        elif self.game_status_won():
            return "Win for " + self.player_with_higher_score()

        elif self.game_status_advantage():
            return "Advantage " + self.player_with_higher_score()

        else:
            return self.translate_score(self.player1_score) + "-" + self.translate_score(self.player2_score)

    def player_with_higher_score(self):
        if self.player1_score > self.player2_score:
            return self.player1_name
        else:
            return self.player2_name

    def translate_score(self, score):
        if score == 0:
            return "Love"
        if score == 1:
            return "Fifteen"
        if score == 2:
            return "Thirty"
        if score == 3:
            return "Forty"

    def score_difference(self):
        return abs(self.player1_score - self.player2_score)

    def game_status_deuce(self):
        if self.game_status_drawn() and self.player1_score >= 4:
            return True
        else:
            return False

    def game_status_drawn(self):
        if self.player1_score == self.player2_score:
            return True
        else:
            return False

    def game_status_won(self):
        if max(self.player1_score, self.player2_score) >= 4 and self.score_difference() >= 2:
            return True
        else:
            return False

    def game_status_advantage(self):
        if max(self.player1_score, self.player2_score) >= 4 and self.score_difference() == 1:
            return True
        else:
            return False
