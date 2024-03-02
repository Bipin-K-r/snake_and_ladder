import pytest
from models.player import Player
from models.board import Board

board = Board(
    10,
    {"number_of_snakes": 1, "snake_position": [[14, 7]]},
    {"number_of_ladders": 1, "ladder_position": [[15, 23]]},
)


@pytest.mark.parametrize("name", ["player1", "player2", "player3"])
@pytest.mark.parametrize("start_position", [1, 2, 3])
def test_player(name, start_position):
    player = Player(name, start_position)
    assert player.name == name
    assert player.position == start_position


@pytest.mark.parametrize("steps", [1, 2, 3])
def test_move(steps):
    player = Player("player1")
    player.move(steps, board)
    assert player.position == 1 + steps
