# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
import numpy as np


def extrapolate(history: str) -> list[np.ndarray[int]]:
    diff_array = np.array(history.split()).astype(int)
    extrapolation = [diff_array]
    while not np.all(diff_array == 0):
        diff_array = np.diff(diff_array)
        extrapolation.append(diff_array)
    return extrapolation


def part1(i: list[str]) -> int:
    return sum(sum(diff[-1] for diff in extrapolate(history)) for history in i)


def part2(i: list[str]) -> int:
    return 1
