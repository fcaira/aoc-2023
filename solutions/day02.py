import math
import re

from collections import namedtuple

Req = namedtuple("Req", "colour, thres")


def part1(i):
    poss_game_sum = 0
    for game in i:
        game_possible = True
        reveals = game.split(";")
        idx = 0
        while game_possible and idx < len(reveals):
            reveal = reveals[idx]
            for r in [Req("blue", 14), Req("red", 12), Req("green", 13)]:
                match = re.findall(r"([0-9]+) " + r.colour, reveal)
                if match:
                    if int(match[0]) > r.thres:
                        game_possible = False
            idx += 1
        if game_possible:
            poss_game_sum += int(re.findall(r"Game ([0-9]+)", game)[0])
    return poss_game_sum


def part2(i):
    total_game_powers = 0
    for game in i:
        max_colour_nums = []
        for c in ["blue", "red", "green"]:
            max_colour_nums.append(
                max(int(num) for num in re.findall(r"([0-9]+) " + c, game))
            )
        total_game_powers += math.prod(max_colour_nums)
    return total_game_powers
