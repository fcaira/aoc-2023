from re import findall
from typing import Tuple, Dict


def parse_map(raw_map: Tuple[str, Dict[str, Dict[str, str]]]):
    directions = raw_map[0]
    map = {}
    for ln in raw_map[2:]:
        nodes = findall(r"[A-Z]{3}", ln)
        map.update({nodes[0]: {"L": nodes[1], "R": nodes[2]}})
    return directions, map


def part1(i):
    directions, map = parse_map(i)
    memo = {}
    node = "AAA"
    steps = 0
    turns_taken = ''
    while node != "ZZZ":
        dir = directions[steps % len(directions)]
        turns_taken += dir
        if turns_taken in memo:
            node = memo[turns_taken]
        else:
            node = map[node][dir]
            memo.update({turns_taken: node})
        steps += 1
    return steps
