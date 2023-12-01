import pytest

from typing import List, Any, Union

from tests.conftest import FileRetriever


f = FileRetriever("./solutions/inputs")
eg = FileRetriever("./solutions/example_inputs")


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[(eg.get_input("01_1"), 142), (f.get_input("01"), 53194)],
    ids=["eg", "ans"],
)
def test_day01_part1(input: List[str], expected_output: Union[str, int]):
    from solutions.day01 import part1

    assert part1(input) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg.get_input("01_2"), 281),
        (
            ["sevenine", "sevennine", "sevennine5", "eightwo", "eighthree", "oneight"],
            79 + 79 + 75 + 82 + 83 + 18,
        ),
        (f.get_input("01"), 54249),
    ],
    ids=["eg", "edge", "ans"],
)
def test_day01_part2(input: List[str], expected_output: Union[str, int]):
    from solutions.day01 import part2

    assert part2(input) == expected_output
