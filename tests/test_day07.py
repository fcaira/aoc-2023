import pytest

from typing import List, Union

from solutions.day07 import (
    PART1_LABELS,
    PART2_LABELS,
    add_ordering,
    part1,
    part2,
)
from tests.conftest import get_input

day = "07"
eg_input = get_input(f"solutions/example_inputs/{day}")
input = get_input(f"solutions/inputs/{day}")


@pytest.mark.parametrize(
    argnames="input, labels, jokers, expected_output",
    argvalues=[
        (
            eg_input,
            PART1_LABELS,
            False,
            [
                ("32T3K", 765, [2, 2, 1, 9, 2, 12]),
                ("T55J5", 684, [4, 9, 4, 4, 10, 4]),
                ("KK677", 28, [3, 12, 12, 5, 6, 6]),
                ("KTJJT", 220, [3, 12, 9, 10, 10, 9]),
                ("QQQJA", 483, [4, 11, 11, 11, 10, 13]),
            ],
        ),
        (
            eg_input,
            PART2_LABELS,
            True,
            [
                ("32T3K", 765, [2, 3, 2, 10, 3, 12]),
                ("T55J5", 684, [6, 10, 5, 5, 1, 5]),
                ("KK677", 28, [3, 12, 12, 6, 7, 7]),
                ("KTJJT", 220, [6, 12, 10, 1, 1, 10]),
                ("QQQJA", 483, [6, 11, 11, 11, 1, 13]),
            ],
        ),
    ],
    ids=["pt1", "pt2"],
)
def test_add_ordering(input, labels, jokers, expected_output):
    assert add_ordering(eg_input, labels, jokers) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 6440),
        (input, 246912307),
    ],
    ids=["eg", "ans"],
)
def test_part1(input: List[str], expected_output: Union[str, int]):
    assert part1(input) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 5905),
        (input, 246894760),
    ],
    ids=["eg", "ans"],
)
def test_part2(input: List[str], expected_output: Union[str, int]):
    assert part2(input) == expected_output
