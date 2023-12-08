from collections import Counter

from typing import List, Dict


def first_order(hand: str):
    """
    Uses a count of each character to determine order
    e.g. "32T3K" results in {"3": 2, "2": 1, "T": 1, "K": 1}
    therefore the distinct set of values in the count result is {1, 2}
    This could be true for one or two pair, so the length of count results is checked
    Length is 4 (there are 4 distinct chars), so must be one pair; the order is 2
    """
    count = Counter(hand)
    set_count = set(count.values())
    if set_count == {5}:
        ord = 7  # Five of a kind (e.g. AAAAA)
    elif set_count == {1, 4}:
        ord = 6  # Four of a kind (e.g. AA8AA)
    elif set_count == {2, 3}:
        ord = 5  # Full house (e.g. 23332)
    elif set_count == {1, 3}:
        ord = 4  # Three of a kind (e.g. TTT98)
    elif set_count == {1, 2}:
        if len(count) == 3:
            ord = 3  # Two pair (e.g. 23432)
        else:
            ord = 2  # One pair (e.g. A23A4)
    elif set_count == {1}:
        ord = 1  # High card (e.g. 23456)
    return ord


def second_order(hand: str, translator: Dict[str, int]):
    """
    Converts hand into a list of ints for ordering
    e.g. "A" maps to 13; "2" maps to 1
    Therefore "32T3K" maps to [2, 1, 9, 2, 12]
    """
    return [translator[char] for char in hand]


def add_ordering(hands: List[str]):
    """
    Takes the list of hand-bet lines, creates a tuple,
    adding a list of orders (first, then second)
    e.g. "32T3K 765" turns into ("32T3K", 765, [2, 2, 1, 9, 2, 12])
    where the first int is the first order, and the subsequent 5 are the second order
    """
    labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    translator = dict(zip(labels, [num for num in range(len(labels), 0, -1)]))
    return [
        (hand, int(bet), [first_order(hand)] + second_order(hand, translator))
        for hand, bet in (ln.split() for ln in hands)
    ]


def part1(i: List[str]):
    """
    Adds ordering to the hand-bet lines, resulting in a list of tuples,
    then sorts the list of tuples according to the ordering
    then uses enumerate to find the rank (must start at 1!),
    and calculates the rank * bet
    """
    return sum(
        rank * bet
        for rank, (_, bet, _) in enumerate(
            sorted(add_ordering(i), key=lambda x: x[2]), start=1
        )
    )


def part2(i):
    return
