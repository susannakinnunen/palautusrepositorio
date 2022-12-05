from tennis_game import TennisGame
from player import Player


def main():
    player_1 = 1
    player_2 = 2
    game = TennisGame()

    print(game.get_score())

    game.won_point(player_1)
    print(game.get_score())

    game.won_point(player_1)
    print(game.get_score())

    game.won_point(player_2)
    print(game.get_score())

    game.won_point(player_1)
    print(game.get_score())

    game.won_point(player_1)
    print(game.get_score())


if __name__ == "__main__":
    main()
