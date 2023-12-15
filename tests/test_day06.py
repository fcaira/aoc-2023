import pytest

from typing import List, Union, Tuple

from solutions.day06 import (
    parse_races,
    part1,
    parse_single_race,
    part2,
)
from tests.conftest import get_input

eg_input = get_input("solutions/example_inputs/06")
input = get_input("solutions/inputs/06")


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, [(7, 9), (15, 40), (30, 200)]),
        (input, [(41, 214), (96, 1789), (88, 1127), (94, 1055)]),
    ],
    ids=["eg", "ans"],
)
def test_parse_races(input: List[str], expected_output: List[Tuple[int, int]]):
    assert list(parse_races(input)) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[(eg_input, 288), (input, 4811940)],
    ids=["eg", "ans"],
)
def test_part1(input: List[str], expected_output: Union[str, int]):
    assert part1(input) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, [(71530, 940200)]),
        (
            input,
            [
                (41968894, 214178911271055),
            ],
        ),
    ],
    ids=["eg", "ans"],
)
def test_parse_single_race(input: List[str], expected_output: List[Tuple[int, int]]):
    assert list(parse_single_race(input)) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 71503),
        (input, 30077773),
    ],
    ids=["eg", "ans"],
)
def test_part2(input: List[str], expected_output: Union[str, int]):
    assert part2(input) == expected_output


4811940  # too low
