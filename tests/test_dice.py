import pytest
from models.dice import Dice


@pytest.mark.parametrize("number_of_dice", [2, 3, 4])
@pytest.mark.parametrize("strategy", ["MAX", "MIN", "SUM"])
def test_dice_roll(number_of_dice, strategy):
    dice = Dice(number_of_dice, strategy)
    roll = dice.roll()
    if strategy == "MAX":
        assert roll <= 6
    elif strategy == "MIN":
        assert roll >= 1
    else:
        assert number_of_dice <= roll <= 6 * number_of_dice
