import pytest


from solutions.day03 import part1, part2
from tests.conftest import get_input

day = "03"
eg_input = get_input(f"solutions/example_inputs/{day}")
input = get_input(f"solutions/inputs/{day}")


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 4361),
        (input, 532428),
    ],
    ids=["eg", "ans"],
)
def test_part1(input: list[str], expected_output: int) -> None:
    assert part1(input) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 467835),
        (input, 84051670),
    ],
    ids=["eg", "ans"],
)
def test_part2(input: list[str], expected_output: int) -> None:
    assert part2(input) == expected_output
