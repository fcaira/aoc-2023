import pytest

from typing import List, Union

from solutions.day04 import parse_cards, part1, part2
from tests.conftest import get_input

day = "04"
eg_input = get_input(f"solutions/example_inputs/{day}")
input = get_input(f"solutions/inputs/{day}")


def test_parse_cards():
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    card = parse_cards(eg_input)[0]
    assert card.id == 1
    assert card.win_nums == {41, 48, 83, 86, 17}
    assert card.our_nums == {83, 86, 6, 31, 17, 9, 48, 53}


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 13),
        (input, 26914),
    ],
    ids=["eg", "ans"],
)
def test_part1(input: List[str], expected_output: Union[str, int]):
    assert part1(input) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 30),
        (input, 13080971),
    ],
    ids=["eg", "ans"],
)
def test_part2(input: List[str], expected_output: Union[str, int]):
    assert part2(input) == expected_output
