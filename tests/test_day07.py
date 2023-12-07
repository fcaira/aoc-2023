import pytest

from typing import List, Union

from solutions.day07 import part1, part2
from tests.conftest import get_input

day = "07"
eg_input = get_input(f"solutions/example_inputs/{day}")
input = get_input(f"solutions/inputs/{day}")


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 6440),
        (input, 0),
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
