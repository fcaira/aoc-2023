from math import inf

from typing import Dict


def parse_map(raw_map):
    lines = raw_map.split("\n")
    conversion = lines[0].split()[0]
    map = {}
    for ln in lines[1:]:
        dest_start, src_start, range_len = (int(num) for num in ln.split())
        map.update({range(src_start, src_start + range_len): dest_start - src_start})
    return {conversion: map}


def parse_maps(raw_maps):
    maps = {}
    for raw_map in raw_maps:
        maps.update(parse_map(raw_map))
    return maps


def convert(category: int, map: Dict[range, range]):
    for range in map.keys():
        if category in range:
            return category + map[range]
    return category


def part1(i):
    seeds = i[0]

    maps = parse_maps(i[1:])
    min_location = inf

    for seed in (int(num) for num in seeds.split()[1:]):
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
