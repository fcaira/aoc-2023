import pytest

from typing import List, Union

from solutions.day07 import (
    part1,
    part2,
    add_ordering,
)
from tests.conftest import get_input

day = "07"
eg_input = get_input(f"solutions/example_inputs/{day}")
input = get_input(f"solutions/inputs/{day}")


def test_add_ordering():
    assert add_ordering(eg_input) == [
        ("32T3K", "765", [2, 2, 1, 9, 2, 12]),
        ("T55J5", "684", [4, 9, 4, 4, 10, 4]),
        ("KK677", "28", [3, 12, 12, 5, 6, 6]),
        ("KTJJT", "220", [3, 12, 9, 10, 10, 9]),
        ("QQQJA", "483", [4, 11, 11, 11, 10, 13]),
    ]


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
        (eg_input, 0),
        (input, 0),
    ],
    ids=["eg", "ans"],
)
def test_part2(input: List[str], expected_output: Union[str, int]):
    assert part2(input) == expected_output
