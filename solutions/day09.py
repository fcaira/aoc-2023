import numpy as np
from typing import Any


def extrapolate(history: str) -> list[np.ndarray[Any, np.dtype[Any]]]:
    diff_array = np.array(history.split()).astype(int)
    extrapolation = [diff_array]
    while not np.all(diff_array == 0):
        diff_array = np.diff(diff_array)
        extrapolation.append(diff_array)
    return extrapolation


def part1(i: list[str]) -> int:
    return sum(sum(diff[-1] for diff in extrapolate(history)) for history in i)


def part2(i: list[str]) -> int:
    total = 0
    for history in i:
        history_sum = 0
        for row in reversed(extrapolate(history)):
            history_sum = row[0] - history_sum
        total += history_sum
    return total
