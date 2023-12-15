from math import sqrt, floor, ceil
from re import findall
from typing import List, Tuple, Iterable


def parse_races(raw_races: List[str]) -> Iterable[Tuple[int, int]]:
    return zip(
        *[
            [int(num) for num in findall(r"([0-9]+)", raw_races[idx])]
            for idx in range(2)
        ]
    )


def part1(i: List[str]) -> int:
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


def parse_single_race(raw_race: List[str]) -> Tuple[int, int]:
    return int("".join(findall(r"([0-9]+)", raw_race[0]))), int(
        "".join(findall(r"([0-9]+)", raw_race[1]))
    )


def part2(i: List[str]) -> int:
    """
    Part 2 ends up as a quadratic equation solve
    - we want the diff between the upper and lower bounds for winning.
    The number of ways we can win the race is given by the formula: x(t - x) > d
    where x = time the button is held for, t = total time, and d = distance threshold.
    We can rearrange this to look like -x^2 + tx - d = 0
    Solving with the quadratic formula... x = d +/- (sqrt(t^2 - 4d) / 2)
    """
    t, d = parse_single_race(i)
    x_lower = ceil(d + sqrt(t**2 - 4 * d) / -2)
    x_upper = floor(d - sqrt(t**2 - 4 * d) / -2)
    return x_upper - x_lower + 1  # plus one for counting a missing win
