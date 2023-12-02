import pytest

from typing import List, Union

from solutions.day02 import part1, part2
from tests.conftest import get_input

eg_input = get_input("solutions/example_inputs/02")
input = get_input("solutions/inputs/02")


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 8),
        (["Game 5: 12 red, 14 blue, 13 green", "Game 6: 13 red, 15 blue, 14 green"], 5),
        (input, 2593),
    ],
    ids=["eg", "edge", "ans"],
)
def test_part1(input: List[str], expected_output: Union[str, int]):
    assert part1(input) == expected_output
    # 200 too low


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 2286),
        (input, 54699),
    ],
    ids=["eg", "ans"],
)
def test_part2(input: List[str], expected_output: Union[str, int]):
    assert part2(input) == expected_output
