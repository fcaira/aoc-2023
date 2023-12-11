from collections import deque
from loguru import logger
from math import inf
from typing import List, Tuple, Deque


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
            logger.info(f"{category} -> {new_val}")
            return new_val
    new_val = category
    logger.info(f"{category} -> {new_val}")
    return new_val


def part1(i):
    seeds = (int(num) for num in i[0].split()[1:])
    maps = parse_maps(i[1:])
    min_location = inf
    for seed in seeds:
        soil = convert(seed, maps["seed-to-soil"])
        fertilizer = convert(soil, maps["soil-to-fertilizer"])
        water = convert(fertilizer, maps["fertilizer-to-water"])
        light = convert(water, maps["water-to-light"])
        temperature = convert(light, maps["light-to-temperature"])
        humidity = convert(temperature, maps["temperature-to-humidity"])
        location = convert(humidity, maps["humidity-to-location"])
        if location < min_location:
            min_location = location
    return min_location


def parse_seed_range(seeds_line: str):
    parsed_seeds = deque()
    seed_parts = deque(seeds_line.split()[1:])
    idx = 0
    while seed_parts:
        logger.info(idx)
        start = int(seed_parts.popleft())
        diff = int(seed_parts.popleft())
        parsed_seeds.append(range(start, start + diff))
        idx += 1
    return parsed_seeds


def convert_ranges(
    category_ranges: Deque[range], conversion_map: Deque[Tuple[range, int]]
):
    output_ranges = deque()

    while category_ranges:
        category_range = category_ranges.pop()
        for conversion_range, diff in conversion_map:
            # ( cat ) [ conv  ]
            if (
                category_range.start not in conversion_range
                and (category_range.stop - 1) not in conversion_range
            ):
                if conversion_range == conversion_map[-1][0]:  # last
                    output_ranges.append(category_range)
                continue

            #  [ conv ( cat ) ]
            elif (
                category_range.start in conversion_range
                and (category_range.stop - 1) in conversion_range
            ):
                output_ranges.append(
                    range(category_range.start + diff, category_range.stop + diff)
                )
                break

            # [ conv ( cat ] )
            elif (
                category_range.start in conversion_range
                and (category_range.stop - 1) not in conversion_range
            ):
                output_ranges.append(
                    range(category_range.start + diff, conversion_range.stop + diff)
                )
                if conversion_range.stop != category_range.stop:
                    category_ranges.appendleft(
                        range(conversion_range.stop, category_range.stop)
                    )
                break

            elif (
                category_range.start not in conversion_range
                and (category_range.stop - 1) in conversion_range
            ):
                category_ranges.appendleft(
                    range(category_range.start, conversion_range.start)
                )
                output_ranges.append(
                    range(conversion_range.start + diff, category_range.stop + diff)
                )
                break

    return output_ranges


def part2(i):
    seed_line = i[0].split("\n")[0]
    seed_range = parse_seed_range(seed_line)
    maps = parse_maps(i[1:])
    soil_range = convert_ranges(seed_range, maps["seed-to-soil"])
    fertilizer_range = convert_ranges(soil_range, maps["soil-to-fertilizer"])
    water_range = convert_ranges(fertilizer_range, maps["fertilizer-to-water"])
    light_range = convert_ranges(water_range, maps["water-to-light"])
    temperature_range = convert_ranges(light_range, maps["light-to-temperature"])
    humidity_range = convert_ranges(temperature_range, maps["temperature-to-humidity"])
    location_range = convert_ranges(humidity_range, maps["humidity-to-location"])
    return min(r.start for r in location_range)
