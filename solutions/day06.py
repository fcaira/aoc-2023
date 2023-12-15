from re import findall
from typing import List, Tuple, Iterable


def parse_races(raw_races: List[str]) -> Iterable[Tuple[int, int]]:
    return zip(
        *[
            [int(num) for num in findall(r"([0-9]+)", raw_races[idx])]
            for idx in range(2)
        ]
    )


def part1(i):
    total = 1
    for race in parse_races(i):
        total_time, dist_thres = race
        num_win_opts = 0
        for time_held in range(total_time):
            time_left = total_time - time_held
            dist_travelled = time_held * time_left
            if dist_travelled > dist_thres:
                num_win_opts += 1
        total *= num_win_opts
    return total


def parse_single_race(raw_race: List[str]) -> Iterable[Tuple[int, int]]:
    return zip(
        *[[int("".join(findall(r"([0-9]+)", raw_race[idx])))] for idx in range(2)]
    )


def part2(i):
    total = 1
    for race in parse_single_race(i):
        total_time, dist_thres = race
        num_win_opts = 0
        for time_held in range(total_time):
            time_left = total_time - time_held
            dist_travelled = time_held * time_left
            if dist_travelled > dist_thres:
                num_win_opts += 1
        total *= num_win_opts
    return total
