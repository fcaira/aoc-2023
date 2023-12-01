from loguru import logger
from collections import namedtuple


def parse_numerals_line(ln):
    num1 = next(char for char in ln if char.isnumeric())
    num2 = next(char for char in reversed(ln) if char.isnumeric())
    return num1 + num2


def part1(i):
    vals = []
    for ln in i:
        vals.append(int(parse_numerals_line(ln)))
    return sum(vals)


def part2(i):
    vals = []
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for ln in i:
        for d in digits:
            if d in ln:
                ln = ln.replace(d, d[0] + str(digits.index(d) + 1) + d[1:])
        vals.append(int(parse_numerals_line(ln)))
    return sum(vals)
