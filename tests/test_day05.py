import pytest

from loguru import logger
from typing import List, Union

from solutions.day05 import parse_map, parse_maps, part1, part2
from tests.conftest import get_input

day = "05"
eg_input = get_input(f"solutions/example_inputs/{day}", split="\n\n")
input = get_input(f"solutions/inputs/{day}", split="\n\n")


def test_parse_map():
    seed_to_soil_map = parse_map("seed-to-soil map:\n50 98 2\n52 50 48")["seed-to-soil"]
    assert seed_to_soil_map[50] == 52
    assert seed_to_soil_map[51] == 53
    assert seed_to_soil_map[96] == 98
    assert seed_to_soil_map[97] == 99
    assert seed_to_soil_map[98] == 50
    assert seed_to_soil_map[99] == 51


def test_parse_maps():
    all_maps = parse_maps(
        [
            "seed-to-soil map:\n50 98 2\n52 50 48",
            "soil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15",
            "fertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4",
            "water-to-light map:\n88 18 7\n18 25 70",
            "light-to-temperature map:\n45 77 23\n81 45 19\n68 64 13",
            "temperature-to-humidity map:\n0 69 1\n1 0 69",
            "humidity-to-location map:\n60 56 37\n56 93 4",
        ]
    )
    for map in all_maps:
        assert "seed-to-soil" in all_maps
        assert "soil-to-fertilizer" in all_maps
        assert "fertilizer-to-water" in all_maps
        assert "water-to-light" in all_maps
        assert "light-to-temperature" in all_maps
        assert "temperature-to-humidity" in all_maps
        assert "humidity-to-location" in all_maps


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 35),
        (input, 0),
    ],
    ids=["eg", "ans"],
)
def test_part1(input: List[str], expected_output: Union[str, int]):
    assert part1(input) == expected_output


# @pytest.mark.parametrize(
#     argnames="input, expected_output",
#     argvalues=[
#         (eg_input, 0),
#         (input, 0),
#     ],
#     ids=["eg", "ans"],
# )
# def test_part2(input: List[str], expected_output: Union[str, int]):
#     assert part2(input) == expected_output
