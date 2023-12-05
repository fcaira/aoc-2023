from math import inf


def parse_map(raw_map):
    lines = raw_map.split("\n")
    conversion = lines[0].split()[0]
    map = {}
    max_src_start = 0
    for ln in lines[1:]:
        dest_start, src_start, range_len = (int(num) for num in ln.split())
        map.update(
            dict(
                zip(
                    range(src_start, src_start + range_len),
                    range(dest_start, dest_start + range_len),
                )
            )
        )
        if src_start > max_src_start:
            max_src_start = src_start

    return {conversion: map}


def parse_maps(raw_maps):
    maps = {}
    for raw_map in raw_maps:
        maps.update(parse_map(raw_map))
    return maps


def part1(i):
    seeds = i[0]
    maps = parse_maps(i[1:])
    min_location = inf

    for seed in (int(num) for num in seeds.split()[1:]):
        soil = maps["seed-to-soil"].get(seed, seed)
        fertilizer = maps["soil-to-fertilizer"].get(soil, soil)
        water = maps["fertilizer-to-water"].get(fertilizer, fertilizer)
        light = maps["water-to-light"].get(water, water)
        temperature = maps["light-to-temperature"].get(light, light)
        humidity = maps["temperature-to-humidity"].get(temperature, temperature)
        location = maps["humidity-to-location"].get(humidity, humidity)
        if location < min_location:
            min_location = location
    return min_location


def part2(i):
    return
