from math import inf

from typing import List, Tuple


def parse_map(raw_map):
    lines = raw_map.split("\n")
    conversion = lines[0].split()[0]
    range_map = [
        (range(src_start, src_start + range_len), dest_start - src_start)
        for ln in lines[1:]
        for dest_start, src_start, range_len in (map(int, ln.split()),)
    ]
    return {conversion: range_map}


def parse_maps(raw_maps: List[str]):
    return {k: v for raw_map in raw_maps for k, v in parse_map(raw_map).items()}


def convert(category: int, conversion_map: Tuple[range, int]):
    for range, diff in conversion_map:
        if category in range:
            return category + diff
    return category


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


def part2(i):
    return
