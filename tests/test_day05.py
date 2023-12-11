import pytest

from collections import deque
from typing import List, Union
from solutions.day05 import (
    parse_map,
    parse_maps,
    convert,
    convert_pt2,
    part1,
    parse_seeds,
    overlap,
    part2,
    part2_opt,
)
from tests.conftest import get_input

day = "05"
eg_input = get_input(f"solutions/example_inputs/{day}", split="\n\n")
input = get_input(f"solutions/inputs/{day}", split="\n\n")


def test_parse_map():
    seed_to_soil_map = parse_map("seed-to-soil map:\n50 98 2\n52 50 48")
    assert set(seed_to_soil_map["seed-to-soil"]) == set(
        [
            (range(50, 98), +2),
            (range(98, 100), -48),
        ]
    )


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
    assert "seed-to-soil" in all_maps
    assert "soil-to-fertilizer" in all_maps
    assert "fertilizer-to-water" in all_maps
    assert "water-to-light" in all_maps
    assert "light-to-temperature" in all_maps
    assert "temperature-to-humidity" in all_maps
    assert "humidity-to-location" in all_maps


def test_convert():
    map = parse_map("seed-to-soil map:\n50 98 2\n52 50 48")["seed-to-soil"]
    assert convert(79, map) == 81
    assert convert(14, map) == 14
    assert convert(55, map) == 57
    assert convert(13, map) == 13


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 35),
        (input, 379811651),
    ],
    ids=["eg", "ans"],
)
def test_part1(input: List[str], expected_output: Union[str, int]):
    assert part1(input) == expected_output


def test_parse_seeds():
    assert parse_seeds("seeds: 79 14 55 13") == deque(
        [
            range(79, 93),
            range(55, 68),
        ]
    )


def test_overlap():
    assert overlap(range(30, 50), range(40, 60)) == range(40, 50)
    assert overlap(range(50, 70), range(10, 30)) == None


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 46),
        (input, 0),
    ],
    ids=["eg", "ans"],
)
def test_part2(input: List[str], expected_output: Union[str, int]):
    assert part2(input) == expected_output


@pytest.mark.parametrize(
    argnames="input, expected_output",
    argvalues=[
        (eg_input, 46),
        (input, 0),
    ],
    ids=["eg", "ans"],
)
def test_part2_opt(input: List[str], expected_output: Union[str, int]):
    assert part2_opt(input) == expected_output


@pytest.mark.parametrize(
    argnames="category_ranges, conversion_map, expected_output",
    argvalues=[
        (
            deque([range(55, 68), range(79, 93)]),
            deque([(range(50, 98), 2), (range(98, 100), -48)]),
            sorted(
                [
                    57,
                    58,
                    59,
                    60,
                    61,
                    62,
                    63,
                    64,
                    65,
                    66,
                    67,
                    68,
                    69,
                    81,
                    82,
                    83,
                    84,
                    85,
                    86,
                    87,
                    88,
                    89,
                    90,
                    91,
                    92,
                    93,
                    94,
                ]
            ),
        ),
        (
            deque([range(81, 95), range(57, 70)]),
            deque([(range(0, 15), 39), (range(15, 52), -15), (range(52, 54), -15)]),
            sorted(
                [
                    81,
                    82,
                    83,
                    84,
                    85,
                    86,
                    87,
                    88,
                    89,
                    90,
                    91,
                    92,
                    93,
                    94,
                    57,
                    58,
                    59,
                    60,
                    61,
                    62,
                    63,
                    64,
                    65,
                    66,
                    67,
                    68,
                    69,
                ]
            ),
        ),
        (
            deque([range(81, 95), range(57, 70)]),
            deque(
                [
                    (range(0, 7), 42),
                    (range(11, 53), -11),
                    (range(7, 11), 50),
                    (range(53, 61), -4),
                ]
            ),
            sorted(
                [
                    81,
                    82,
                    83,
                    84,
                    85,
                    86,
                    87,
                    88,
                    89,
                    90,
                    91,
                    92,
                    93,
                    94,
                    53,
                    54,
                    55,
                    56,
                    61,
                    62,
                    63,
                    64,
                    65,
                    66,
                    67,
                    68,
                    69,
                ]
            ),
        ),
        (
            deque([range(53, 57), range(81, 95), range(61, 70)]),
            deque([(range(18, 25), 70), (range(25, 95), -7)]),
            sorted(
                [
                    74,
                    75,
                    76,
                    77,
                    78,
                    79,
                    80,
                    81,
                    82,
                    83,
                    84,
                    85,
                    86,
                    87,
                    46,
                    47,
                    48,
                    49,
                    54,
                    55,
                    56,
                    57,
                    58,
                    59,
                    60,
                    61,
                    62,
                ]
            ),
        ),
        (
            deque([range(54, 63), range(74, 88), range(46, 50), range(95, 95)]),
            deque([(range(77, 100), -32), (range(45, 64), 36), (range(64, 77), 4)]),
            sorted(
                [
                    45,
                    46,
                    47,
                    48,
                    49,
                    50,
                    51,
                    52,
                    53,
                    54,
                    55,
                    78,
                    79,
                    80,
                    82,
                    83,
                    84,
                    85,
                    90,
                    91,
                    92,
                    93,
                    94,
                    95,
                    96,
                    97,
                    98,
                ]
            ),
        ),
        (
            deque([range(63, 63), range(82, 86), range(74, 45), range(90, 99), range(78, 80)]),
            deque([(range(69, 70), -69), (range(0, 69), 1)]),
            sorted(
                [
                    78,
                    79,
                    80,
                    46,
                    47,
                    48,
                    49,
                    50,
                    51,
                    52,
                    53,
                    54,
                    55,
                    56,
                    82,
                    83,
                    84,
                    85,
                    90,
                    91,
                    92,
                    93,
                    94,
                    95,
                    96,
                    97,
                    98,
                ]
            ),
        ),
        (
            deque([range(78, 80), range(90, 99), range(74, 1), range(82, 86), range(64, 64), range(74, -1)]),
            deque([(range(56, 93), 4), (range(93, 97), -37)]),
            sorted(
                [
                    82,
                    83,
                    84,
                    46,
                    47,
                    48,
                    49,
                    50,
                    51,
                    52,
                    53,
                    54,
                    55,
                    60,
                    86,
                    87,
                    88,
                    89,
                    94,
                    95,
                    96,
                    56,
                    57,
                    58,
                    59,
                    97,
                    98,
                ]
            ),
        ),
    ],
    ids=[
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ],
)
def test_convert_pt2(category_ranges, conversion_map, expected_output):
    result = convert_pt2(category_ranges, conversion_map)
    assert (
        sorted(num for num_list in (list(r) for r in result) for num in num_list)
        == expected_output
    )


# {'seed-to-soil': sorted([81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), 'soil-to-fertilizer': sorted([81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), 'fertilizer-to-water': sorted([81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66, 67, 68, 69]), 'water-to-light': sorted([74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 46, 47, 48, 49, 54, 55, 56, 57, 58, 59, 60, 61, 62]), 'light-to-temperature': sorted([78, 79, 80, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 96, 97, 98]), 'temperature-to-humidity': [78, 79, 80, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 96, 97, 98], 'humidity-to-location': sorted([82, 83, 84, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 60, 86, 87, 88, 89, 94, 95, 96, 56, 57, 58, 59, 97, 98])}
