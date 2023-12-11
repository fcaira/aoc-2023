from collections import deque
from math import inf
from typing import List, Tuple, Deque


CONVERSIONS = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]


def parse_map(raw_map: str):
    lines = raw_map.split("\n")
    conversion = lines[0].split()[0]
    range_map = deque(
        (range(src_start, src_start + range_len), dest_start - src_start)
        for ln in lines[1:]
        for dest_start, src_start, range_len in (map(int, ln.split()),)
    )
    return {conversion: range_map}


def parse_maps(raw_maps: List[str]):
    return {k: v for raw_map in raw_maps for k, v in parse_map(raw_map).items()}


def convert(category: int, conversion_map: Deque[Tuple[range, int]]):
    for range, diff in conversion_map:
        if category in range:
            new_val = category + diff
            return new_val
    new_val = category
    return new_val


def part1(i):
    seeds = set(int(num) for num in i[0].split()[1:])
    maps = parse_maps(i[1:])
    min_location = inf
    for seed in seeds:
        current_category = seed
        for conversion in CONVERSIONS:
            current_category = convert(current_category, maps[conversion])
        if current_category < min_location:
            min_location = current_category
    return min_location


def parse_seed_range(seeds_line: str):
    parsed_seeds: Deque = deque()
    seed_parts = deque(seeds_line.split()[1:])
    idx = 0
    while seed_parts:
        start = int(seed_parts.popleft())
        diff = int(seed_parts.popleft())
        parsed_seeds.append(range(start, start + diff))
        idx += 1
    return parsed_seeds


def find_overlap_type(range_a: range, range_b: range):
    if range_a.start in range_b and (range_a.stop - 1) in range_b:
        return "full"  #  [ conv ( cat ) ]
    elif range_a.start not in range_b and (range_a.stop - 1) in range_b:
        return "start"  # ( cat [ conv ) ]
    elif range_a.start in range_b and (range_a.stop - 1) not in range_b:
        return "end"  # [ conv ( cat ] )
    else:
        return "none"  # ( cat ) [ conv ]


def convert_ranges(cat_ranges: Deque[range], conv_map: Deque[Tuple[range, int]]):
    output_ranges: Deque = deque()

    while cat_ranges:
        cat_range = cat_ranges.pop()
        for conv_range, diff in conv_map:
            overlap_type = find_overlap_type(cat_range, conv_range)

            match overlap_type:
                case "none":
                    if conv_range == conv_map[-1][0]:  # last
                        output_ranges.append(cat_range)
                    continue

                case "full":
                    output_ranges.append(
                        range(cat_range.start + diff, cat_range.stop + diff)
                    )
                    break

                case "end":
                    output_ranges.append(
                        range(cat_range.start + diff, conv_range.stop + diff)
                    )
                    cat_ranges.appendleft(range(conv_range.stop, cat_range.stop))
                    break

                case "start":
                    output_ranges.append(
                        range(conv_range.start + diff, cat_range.stop + diff)
                    )
                    cat_ranges.appendleft(range(cat_range.start, conv_range.start))
                    break

    return output_ranges


def part2(i):
    seed_line = i[0].split("\n")[0]
    seed_range = parse_seed_range(seed_line)
    maps = parse_maps(i[1:])
    current_range = seed_range
    for conversion in CONVERSIONS:
        current_range = convert_ranges(current_range, maps[conversion])
    return min(r.start for r in current_range)
