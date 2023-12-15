import pytest

from solutions.dayxx import (
    part1,
    part2,
)
from tests.conftest import get_input

eg_input = get_input("solutions/example_inputs/xx")
input = get_input("solutions/inputs/xx")


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[(eg_input, 0), (input, 0)],
    ids=["eg", "ans"],
)
def test_part1(input: list[str], expected_output: int) -> None:
    assert part1(input) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[(eg_input, 0), (input, 0)],
    ids=["eg", "ans"],
)
def test_part2(input: list[str], expected_output: int) -> None:
    assert part2(input) == expected_output
