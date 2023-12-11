from collections import deque
from loguru import logger
from math import inf
from typing import List, Tuple, Union, Set, Deque


def parse_map(raw_map):
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


def convert(category: int, conversion_map: Tuple[range, int]):
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


def parse_seeds(seeds_line: str):
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


def overlap(range_a: range, range_b: range) -> Union[range, None]:
    overlap_start = max(range_a.start, range_b.start)
    overlap_stop = min(range_a.stop, range_b.stop)
    if overlap_start <= overlap_stop:
        return range(overlap_start, overlap_stop)
    return None


def convert_pt2(
    category_ranges: Deque[range], conversion_map: Deque[Tuple[range, int]]
):
    expected_numbers = sum(len(r) for r in category_ranges)
    
    output_ranges = deque()
    # min_bound = inf
    # max_bound = 0
    # unmapped_ranges = set()
    # for idx, range in enumerate(category_ranges):
    #     if range.stop != range[idx+1].start:

    while category_ranges:
        category_range = category_ranges.pop()
        for conversion_range, diff in conversion_map:
            # ( cat ) [ conv  ]
            if (
                category_range.start not in conversion_range
                and category_range.stop not in conversion_range
            ):
                if conversion_range == conversion_map[-1][0]:
                    output_ranges.append(category_range)
                continue

            #  [ conv ( cat ) ]
            elif (
                category_range.start in conversion_range
                and category_range.stop in conversion_range
            ):
                output_ranges.append(
                    range(category_range.start + diff, category_range.stop + diff)
                )
                break

            # [ conv ( cat ] )
            elif (
                category_range.start in conversion_range
                and category_range.stop not in conversion_range
            ):
                output_ranges.append(
                    range(category_range.start + diff, conversion_range.stop + diff)
                )
                category_ranges.appendleft(
                    range(conversion_range.stop, category_range.stop)
                )
                break

            # ( cat [ ) conv ]
            elif (
                category_range.start not in conversion_range
                and category_range.stop in conversion_range
            ):
                category_ranges.appendleft(
                    range(category_range.start, conversion_range.start - 1)
                )
                output_ranges.append(
                    range(category_range.start, conversion_range.start + diff)
                )
                break

            # ( cat )[ conv ] //
            # elif (
            #     category_range.stop == conversion_range.start 
            # ):
            #     category_ranges.appendleft(
            #         range(category_range.start, conversion_range.start)
            #     )
            #     output_ranges.append(
            #         range(category_range.start, conversion_range.start + diff)
            #     )

            # # [ conv ]( cat )
            # elif conversion_range.stop == category_range.start
            #     # output_ranges.add(
            #     #     range(conversion_range.start + diff, category_range.stop + diff)
            #     # )

    # if sum(len(r) for r in output_ranges) != expected_numbers:
    #     raise Exception(f"Lengths don't match, should be {expected_numbers} numbers")
    return output_ranges


def part2(i):
    seed_line = i[0].split("\n")[0]
    seed_ranges = parse_seeds(seed_line)
    maps = parse_maps(i[1:])
    min_location = inf
    nums = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }
    for seed_range in seed_ranges:
        for idx, seed in enumerate(seed_range):
            logger.info(f"{seed} {seed_range}")
            # logger.info(idx)
            soil = convert(seed, maps["seed-to-soil"])
            nums["seed-to-soil"].append(soil)
            fertilizer = convert(soil, maps["soil-to-fertilizer"])
            nums["soil-to-fertilizer"].append(fertilizer)
            water = convert(fertilizer, maps["fertilizer-to-water"])
            nums["fertilizer-to-water"].append(water)
            light = convert(water, maps["water-to-light"])
            nums["water-to-light"].append(light)
            temperature = convert(light, maps["light-to-temperature"])
            nums["light-to-temperature"].append(temperature)
            humidity = convert(temperature, maps["temperature-to-humidity"])
            nums["temperature-to-humidity"].append(humidity)
            location = convert(humidity, maps["humidity-to-location"])
            nums["humidity-to-location"].append(location)
            if location < min_location:
                min_location = location

    logger.info(nums)
    return min_location


def part2_opt(i):
    seed_line = i[0].split("\n")[0]
    seed_range = set(parse_seeds(seed_line))
    maps = parse_maps(i[1:])
    soil_range = convert_pt2(seed_range, maps["seed-to-soil"])
    fertilizer_range = convert_pt2(soil_range, maps["soil-to-fertilizer"])
    water_range = convert_pt2(fertilizer_range, maps["fertilizer-to-water"])
    light_range = convert_pt2(water_range, maps["water-to-light"])
    temperature_range = convert_pt2(light_range, maps["light-to-temperature"])
    humidity_range = convert_pt2(temperature_range, maps["temperature-to-humidity"])
    location_range = convert_pt2(humidity_range, maps["humidity-to-location"])
    return min(num for num_range in location_range for num in num_range)
