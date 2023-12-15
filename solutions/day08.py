from math import lcm
from re import findall


def parse_map(raw_map: list[str] | str) -> tuple[str, dict[str, dict[str, str]]]:
    directions = raw_map[0]
    map = {}
    ln: str = ""
    for ln in raw_map[2:]:
        nodes = findall(r"[A-Z0-9]{3}", ln)
        map.update({nodes[0]: {"L": nodes[1], "R": nodes[2]}})
    return directions, map


def part1(i: list[str]) -> int:
    directions, map = parse_map(i)
    node = "AAA"
    steps = 0
    while node != "ZZZ":
        dir = directions[steps % len(directions)]
        node = map[node][dir]
        steps += 1
    return steps


def part2(i: list[str]) -> int:
    """
    Instead of trying to calculate routes starting at different nodes simultaneously,
    calculate steps per each route and find the lowest common multiple
    """
    directions, map = parse_map(i)
    starting_nodes = {node for node in map if node.endswith("A")}
    per_node_steps = []
    for node in starting_nodes:
        steps = 0
        while not node.endswith("Z"):
            dir = directions[steps % len(directions)]
            node = map[node][dir]
            steps += 1
        per_node_steps.append(steps)
    return lcm(*per_node_steps)
