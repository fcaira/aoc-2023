import pytest

from typing import List, Union

from solutions.day01 import part1, part2
from tests.conftest import get_input

eg_input_part1 = get_input("solutions/example_inputs/01_1")
eg_input_part2 = get_input("solutions/example_inputs/01_2")
input = get_input("solutions/inputs/01")


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[(eg_input_part1, 142), (input, 53194)],
    ids=["eg", "ans"],
)
def test_part1(input: List[str], expected_output: Union[str, int]):
    assert part1(input) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input_part2, 281),
        (
            ["sevenine", "sevennine", "sevennine5", "eightwo", "eighthree", "oneight"],
            79 + 79 + 75 + 82 + 83 + 18,
        ),
        (input, 54249),
    ],
    ids=["eg", "edge", "ans"],
)
def test_part2(input: List[str], expected_output: Union[str, int]):
    assert part2(input) == expected_output
