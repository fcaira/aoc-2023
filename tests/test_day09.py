import numpy as np
import pytest

from solutions.day09 import (
    extrapolate,
    part1,
    part2,
)
from tests.conftest import get_input

eg_input = get_input("solutions/example_inputs/09")
input = get_input("solutions/inputs/09")


def test_extrapolate() -> None:
    np.testing.assert_equal(
        extrapolate("0 3 6 9 12 15"),
        [
            np.array([0, 3, 6, 9, 12, 15]),
            np.array([3, 3, 3, 3, 3]),
            np.array([0, 0, 0, 0]),
        ],
    )


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[(eg_input, 114), (input, 2038472161)],
    ids=["eg", "ans"],
)
def test_part1(input: list[str], expected_output: int) -> None:
    assert part1(input) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[(eg_input, 2), (input, 1091)],
    ids=["eg", "ans"],
)
def test_part2(input: list[str], expected_output: int) -> None:
    assert part2(input) == expected_output
