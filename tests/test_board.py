import pytest
from models.board import Board


@pytest.mark.parametrize("size", [10, 15])
@pytest.mark.parametrize("snakes", [{"number_of_snakes": 2, "snake_position": [[14, 7], [5, 2]]}])
@pytest.mark.parametrize("ladders", [{"number_of_ladders": 2, "ladder_position": [[9, 4], [6, 10]]}])
def test_board(size, snakes, ladders):
    board = Board(size, snakes, ladders)
    assert board.size == size
    assert board.snakes == {14: 7, 5: 2}
    assert board.ladders == {4: 9, 6: 10}  # ladders are always from bottom to top
