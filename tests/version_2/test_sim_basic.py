import pytest

from tests.flo import diff
from ten_thousand.play_game import play 
from ten_thousand.game_logic import GameLogic


pytestmark = [pytest.mark.version_2]


def test_quitter():
    diffs = diff(play, path="tests/version_2/quitter.sim.txt")
    print("diffs are", diffs)
    assert not diffs, diffs


# @pytest.mark.skip("unskip when ready")
def test_one_and_done():
    diffs = diff(play, path="tests/version_2/one_and_done.sim.txt")
    assert not diffs, diffs


# @pytest.mark.skip("unskip when ready")
def test_single_bank():
    diffs = diff(
        play, path="tests/version_2/bank_one_roll_then_quit.sim.txt"
    )
    assert not diffs, diffs


# @pytest.mark.skip("unskip when ready")
def test_bank_first_for_two_rounds():
    diffs = diff(
        play, path="tests/version_2/bank_first_for_two_rounds.sim.txt"
    )
    assert not diffs, diffs
