import pytest
from models.game import Game


@pytest.fixture
def game() -> Game:
    config = {
        "board_size": 10,
        "snakes": {"number_of_snakes": 1, "snake_position": [[14, 7]]},
        "ladders": {"number_of_ladders": 1, "ladder_position": [[15, 23]]},
        "players": {
            "number_of_players": 2,
            "player_names_and_positions": {"player1": 1, "player2": 1},
        },
        "crocodiles_positions": [12, 8],
        "number_of_dies": 1,
        "movement_strategy": "MAX",
    }
    return Game(config)


def test_check_for_overlapping(game):
    # if a players lands where there's already a player, then previous one goes to start
    player1 = game.players[0]
    player2 = game.players[1]

    player1.position = 6
    player2.position = 6
    game.check_for_overlapping(player2)
    assert player1.position == 1


def test_crocodiles_effect(game):
    # moves back 5 positions
    player = game.players[0]
    player.position = 8
    game.crocodiles_effect(player)
    assert player.position == 3

    player.position = 12
    game.crocodiles_effect(player)
    assert player.position == 7
