import re

from collections import namedtuple
from math import prod

POI = namedtuple("POI", "loc, val")


def part1(i):
    width = len(i[0])
    ln_joined = "".join(i)
    digits = list(re.finditer(r"([0-9]+)", ln_joined))
    symbols = list(re.finditer(r"([^0-9.\s])", ln_joined))
    sum = 0
    for sym in symbols:
        loc = sym.span()[0]
        adj = (
            list(range((loc - width) - 1, (loc - width) + 2))
            + list(range((loc + width) - 1, (loc + width) + 2))
            + [loc + 1]
            + [loc - 1]
        )
        for d in digits:
            if any(idx for idx in range(*d.span()) if idx in adj):
                sum += int(d.group(0))
    return sum


def part2(i):
    width = len(i[0])
    ln_joined = "".join(i)
    digits = list(re.finditer(r"([0-9]+)", ln_joined))
    symbols = list(re.finditer(r"(\*)", ln_joined))
    sum = 0
    for sym in symbols:
        gear_parts = []
        loc = sym.span()[0]
        adj = (
            list(range((loc - width) - 1, (loc - width) + 2))
            + list(range((loc + width) - 1, (loc + width) + 2))
            + [loc + 1]
            + [loc - 1]
        )
        for d in digits:
            if any(idx for idx in range(*d.span()) if idx in adj):
                gear_parts.append(int(d.group(0)))
        if len(gear_parts) >= 2:
            sum += prod(gear_parts)
    return sum
