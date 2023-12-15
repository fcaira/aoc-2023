from collections import deque
from re import findall
from typing import Tuple, Dict, List


def parse_map(raw_map: Tuple[str, Dict[str, Dict[str, str]]]):
    directions = raw_map[0]
    map = {}
    for ln in raw_map[2:]:
        nodes = findall(r"[A-Z0-9]{3}", ln)
        map.update({nodes[0]: {"L": nodes[1], "R": nodes[2]}})
    return directions, map


def part1(i: List[str]) -> int:
    directions, map = parse_map(i)
    node = "AAA"
    steps = 0
    while node != "ZZZ":
        dir = directions[steps % len(directions)]
        node = map[node][dir]
        steps += 1
    return steps
