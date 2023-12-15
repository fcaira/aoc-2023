import pytest

from typing import List, Union

from solutions.day08 import parse_map, part1  # ,  part2,

from tests.conftest import get_input

day = "08"
eg_input_a = get_input(f"solutions/example_inputs/{day}_a")
eg_input_b = get_input(f"solutions/example_inputs/{day}_b")
input = get_input(f"solutions/inputs/{day}")


def test_parse_map():
    parsed_map = parse_map(eg_input_a)
    assert len(parsed_map) == 2
    assert parsed_map[0] == ("RL")
    assert parsed_map[1]["AAA"] == {"L": "BBB", "R": "CCC"}
    assert parsed_map[1]["ZZZ"] == {"L": "ZZZ", "R": "ZZZ"}


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input_a, 2),
        (eg_input_b, 6),
        (input, 18673),
    ],
    ids=["eg_a", "eg_b", "ans"],
)
def test_part1(input: List[str], expected_output: Union[str, int]):
    assert part1(input) == expected_output
