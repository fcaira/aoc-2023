import re


def parse_numerals_line(ln):
    matches = re.findall(r"\d", ln)
    return matches[0] + matches[-1]


def part1(i):
    return sum(int(parse_numerals_line(ln)) for ln in i)


def part2(i):
    vals = []
    digit_map = {
        d: d[0] + str(idx + 1) + d[1:]
        for idx, d in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        )
    }
    for ln in i:
        for old, new in digit_map.items():
            ln = ln.replace(old, new)
        vals.append(int(parse_numerals_line(ln)))
    return sum(vals)
